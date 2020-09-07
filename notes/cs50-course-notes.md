---
bibliography:
- 'references.bib'
---

CS50: Course notes <!--- {#cs50-course-notes .unnumbered .unnumbered} -->
==================

------------------------------------------------------------------------

<!-- \vspace{0.25in} -->
CS50 is offered by Harvard University. I started this course in Aug 2020
on the edX platform.

Course page: <https://cs50.harvard.edu/x/2020/>

Lecture 0: Computational thinking, Scratch {#lecture-0-computational-thinking-scratch .unnumbered .unnumbered}
==========================================

Computer science at it's most basic level is problem solving. A typical
workflow in CS takes an input and returns an output. Information in
computers is stored in bits (1, 0). 8 bits are equivalent to 1 byte.

-   $(11001)_2$ is equivalent to
    $1\times2^4 + 1\times 2^3 + 0\times2^2 + 0\times2^1 + 1\times 2^0 = (25)_{10}$

-   Representing 50 in binary will require 7 bits, 110010

-   Alphabets can also be represented in binary by creating a mapping.
    ASCII (American Standard Code for Information Interchange) was one
    of the first character encodings that used 8 bits to represent each
    alphabet, punctuation and digits. For example, 'A' is represented
    with the binary equivalent of 65. Unicode is a much more flexible
    encoding that uses 1-4 bytes for encoding. As of Mar 2020, it
    supports 140k+ characters including emojis.

-   Similarly, photos can be broken into pixel, and each pixel can be
    encoded as a tuple of 3 RGB values. Videos can be encoded as
    multiple pictures. Similarly, audio can also be digitally encoded
    taking into account pitch, note, volume, etc.

Phone directory search %{#phone-directory-search .unnumbered .unnumbered}
----------------------

Let's say we want to search for a particular name in the phone directory
($n$ pages), the brute force method of doing it is to go through each
page from start to finish or until we find the name. In the worst case,
we will need to visit $n$ pages before finding the name. A slight
improvement will be to traverse 2 pages at a time. So, we start with
page 2, then go to page 4, then page 6 and so on. If we happen to skip
over the name, then we can go back to the previous page and search for
it. With this approach, the worst case scenario will require visiting
$n/2$ pages.

We can extend this approach, and start at the middle of the phone book.
Then based on the names on the page, we will either search it in the
first half or the second. At each step we will keep splitting the search
space by half. Via this approach, we will need to visit $\log_2(n)$
pages in the worst case. If the book at 1,024 pages. Then the first
approach will require us to visit 1000 pages but with binary search
approach, we need to only look at 10 pages. If the phone book size
increased to 2048 pages, the binary search will only require us to look
at just ONE additional page.

### Binary search algorithm for phone book %{#binary-search-algorithm-for-phone-book .unnumbered .unnumbered}

1.  Open the book and go to the middle of the book

2.  If name found on the page: STOP

3.  Else if name is in the first half

4.  1.  Go to the middle of first half

    2.  Go to step 2

5.  Else if name if in the second half

6.  1.  Go to the middle of second half

    2.  Go to step 2

7.  Quit as name is not found

The key components of an algorithm are: a) functions, b) conditional
statements, c) boolean expressions, d) loops, and e) variables.

Homework %{#homework .unnumbered .unnumbered}
--------

The first homework was done using MIT's visual programming language
called Scratch. It is accessible at this location:
<https://scratch.mit.edu/>

Lecture 1: C %{#lecture-1-c .unnumbered .unnumbered}
============

The code that we write in a text-editor is called source code. Code
written in C needs to be converted to machine code before it can be
executed. To do this a compiler is needed. `clang` is an open-source
compiler for C language. Executing the command `$ clang program.c`
creates a new executable file called `a.out` which stands for assembly
output. This file is executable.

This lecture showed the basic programming constructs in C like printing
to screen, taking user input, data types, loops (for, do, while),
conditional statements (if-else), boolean expressions, etc. Few notes:

-   Do loop always executes once as it checks for the condition at the
    end of the first loop, whereas while loop checks the condition at
    the start.

-   Float precision[@floatingpoint]: in C takes up 4 bytes of space, and
    double takes 8 bytes. Float precision is the problem when

-   Numerical overflow: If [@einstein]

Lecture 2: Arrays %{#lecture-2-arrays .unnumbered .unnumbered}
=================

Lecture 3: Algorithms %{#lecture-3-algorithms .unnumbered .unnumbered}
=====================

Lecture 4: Memory %{#lecture-4-memory .unnumbered .unnumbered}
=================

Lecture 5: Data Structures %{#lecture-5-data-structures .unnumbered .unnumbered}
==========================

Lecture 6: Python %{#lecture-6-python .unnumbered .unnumbered}
=================

Lecture 7: SQL %{#lecture-7-sql .unnumbered .unnumbered}
==============

Lecture 9: Information %{#lecture-9-information .unnumbered .unnumbered}
======================

Tracks: Web %{#tracks-web .unnumbered .unnumbered}
===========

<!-- \bibliographystyle{ } -->
