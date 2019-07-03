This week, we're going to create tuples. Not just tuples, but *magic* tuples.  And not just magic tuples, but an iterator that creates magic tuples.

What's a magic tuple?  It's actually a term that I came up with. I see it as analogous to a magic square, the nxn square in which each element contains a number, and each row/column/diagonal adds up to the same number.

In the same (but simpler) way, our tuples are magic in that they all add up to the same sum.  For example, the following magic tuples contain the numbers up to 9, and all add up to the number 10:
    (1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)

Notice that each tuple contains two integers, that the digits add up to 10, and that (1,9) isn't the same as (9,1).

The challenge is to write a function, magic_tuples, that takes two positive integers. The first argument indicates the total to which each tuple should sum. The second number is one more than the maximum number that can appear in any tuple.

So if we call magic_tuples(10, 10), we should get the tuples displayed above. If we call magic_tuples(10, 8), then we'll get a subset of the above:
    (3, 7), (4, 6), (5, 5), (6, 4), (7, 3)

The return value should be an iterator -- so that if we call magic_tuples(100000, 100000), we're not going to be overwhelmed by a huge list. Rather, I want to be able to retrieve my magic tuples one at a time.

So if we invoke:
    for t in magic_tuples(5,4):
        print(t)

The output should be:
    (2, 3)
    (3, 2)

Although if the order changes, I won't worry about it too much.
