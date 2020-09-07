function toggleImage() {
    var filters = [
        "blur(1px)",
        "brightness(50%)",
        "saturate(50%)",
        "grayscale(100%)",
        "hue-rotate(180)",
        "opacity(20%)",
        "invert(100%)",
        "sepia(100%)"
    ]

    const random = Math.floor(Math.random() * filters.length);
    console.log(random);
    console.log(filters[random]);

    var img = document.getElementById('myimage');
    img.style.filter = "none";
    img.style.filter = filters[random];
}

function randomPicture() {
    let totalPictures = 6;
    const random = Math.floor(Math.random() * totalPictures);
    var img = document.getElementById('photo');
    img.src = "images/picture-0" + random + ".jpg";
}