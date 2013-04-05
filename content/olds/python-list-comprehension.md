Title: Python List Comprehension
Date: 2012-02-25 22:51
Tags: programming, python

Ok, been wanting to write about this for a while, in case i forgot, but
seems like I almost forgot about it. It's about a a feature of Python
that I don't really see in other languages i use such as C#, so I wanted
to write about this in case i forgot.

Ok, so the list comprehension is a python feature that, as the name
suggest, create a new list based on an existing list. Well, I think it's
much easier for me to just write an example, this post is meant for
myself anyway.

    :::python
    #basically, to use list comprehension, surround the expression in square brackets
    aList = [1,2,3,4,5,6]

    # create a new list of even numbers, the conditional operation is optional though.
    evens  = [x for x in aList if x%2==0]
