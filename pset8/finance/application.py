import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    data = db.execute("""SELECT symbol, name,
    sum(case when action="buy" then shares else -shares end) as totalshares
    FROM
    transactions where id = ? group by symbol, name having totalshares > 0""", session["user_id"])

    for row in data:
        symbol = row["symbol"]
        info = lookup(symbol)
        row["price"] = info["price"]
        row["shares"] = row["totalshares"]
        row["total"] = row["price"] * row["shares"]

    grandtotal = sum([row["total"] for row in data])

    return render_template("home.html", grandtotal=grandtotal, data=data)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("Symbol cannot be empty")

        if not shares.isdigit() or (shares.isdigit() and int(shares) <= 0):
            return apology("Shares has to be a positive integer")

        shares = int(shares)

        data = lookup(symbol)
        if not data:
            return apology("Symbol doesn't exist")

        cost = shares * data['price']
        balance = db.execute("select cash from users where id = ?", session["user_id"])[0]["cash"]

        if cost > balance:
            return apology("You are out of money")

        db.execute("INSERT INTO transactions (id, action, symbol, shares, price, name) VALUES (?, ?, ?, ?, ?, ?)",
                session["user_id"],
                "buy",
                data["symbol"],
                shares,
                data["price"],
                data["name"],
        )

        db.execute("UPDATE users SET cash = ? where id = ?", balance - cost, session["user_id"])

        return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    data = db.execute("""SELECT symbol, case when action='buy' then shares else -shares end as shares, price, timestamp from transactions
    where id = ?""", session["user_id"])

    return render_template("history.html", data=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Symbol cannot be empty")

        data = lookup(symbol)
        if data:
            return render_template("quoted.html", data=data)
        else:
            return apology("Symbol doesn't exist")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Username is required")

        if (not password) or (not confirmation):
            return apology("Password fields cannot be empty")

        if (password != confirmation):
            return apology("Passwords don't match")

        rows = db.execute("SELECT * from users where username = ?", username)
        if len(rows) > 0:
            return apology("Username already exists")

        password_hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password_hash)

        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        return render_template("sell.html")
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("Symbol cannot be empty")

        if not shares.isdigit() or (shares.isdigit() and int(shares) <= 0):
            return apology("Shares has to be a positive integer")
        shares = int(shares)

        user_shares = db.execute("SELECT sum(case when action='buy' then shares else -shares end) as shares from transactions where id=? and symbol=?", session["user_id"], symbol)[0]
        print(user_shares)
        if user_shares["shares"] is None:
            return apology(f"You don't own {symbol}")

        if user_shares["shares"] < shares:
            return apology("You don't own enough shares")

        data = lookup(symbol)
        if not data:
            return apology("Symbol doesn't exist")

        value = shares * data['price']

        db.execute("INSERT INTO transactions (id, action, symbol, shares, price, name) VALUES (?, ?, ?, ?, ?, ?)",
                session["user_id"],
                "sell",
                data["symbol"],
                shares,
                data["price"],
                data["name"],
        )

        balance = db.execute("select cash from users where id = ?", session["user_id"])[0]["cash"]
        db.execute("UPDATE users SET cash = ? where id = ?", balance + value, session["user_id"])

        return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
