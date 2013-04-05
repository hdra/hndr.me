Title: Python Learning Progress–Part 4
Date: 2012-01-26 11:21
Rags: programming, progress

Last time I talked about getting input and a little about conditional
statement and looping that should’ve enabled you to start creating the
basic application and implement some basic algorithm in Python. This
time, I am going to do a review on some of the basic data structures in
Python.

The basic data structures in Python are: list, tuples, and dictionaries.

Let me start with dictionaries. Dictionaries basically defines a
one-to-one relationship between a key and a value, just like an ordinary
dictionary, where a word is associated with its definition. To define a
dictionary in Python, the code are:

    :::python
    # to define a dictionary, declare a
    # variable with its value enclosed
    # between two curly braces '{}', and declare the 'entries' with
    # the syntax, {key:value}, and separate each entry with a comma,
    # as you can see, the key and value can be mixed of any data type
    dict = {'name':'John','age':20,'sex':'male',1:'number'}

    # to access it, call the variable name with the key in a bracket '[]'
    print dict['name'] #will print John
    print dict['age'] #will print 20
    print dict[1] #will print number

    # to change or delete the value, use the same method
    dict['name'] = 'jack'
    del dict['age']

Some things to note about dictionary are, dictionary keys are
case-sensitive, and it is unordered.

Next is the list. Lists are, well, lists, like dictionary, a list
contains an array of items. It is like the array list of other
programming languages. To define a list, declare the contents of the
list within a square brackets and separate it with commas.

    :::python
    # declare a list of fruits
    ls = ["apple", "orange", "banana", "pear"]

    # to access it, use the index, starting from 0
    print ls[0] #apple
    print ls[2] #banana

    # enter a negative index to access the list from the last element
    print ls[-1] #pear
    print ls[-2] #banana

    # accessing a subset of the list (known as slicing)
    print ls[0:3] #access the list from index 0-2
    print ls[1:4] #access the list from index 1-3
    print ls[:4] #access the list from the beginning until index 3
    print ls[1:] #access the list from index 1 until the last element

    # to change it, use the same syntax
    ls[0] = "mango"

    # or to delete it
    del ls[3]

    # to add an element to the end of the list, use append() method
    ls.append("tomato")

    # to extend the list with another list, use the extend() method
    ls.extend(["strawberry","grapes"])

    # to insert an element into the list, use the insert() method, which
    # takes the index of the list to insert, and the item to insert
    ls.insert(1,"lemon") #insert lemon into index #1

In addition to these basic operation, a list provides a lot of other
functions as well, one of them is the function to search for an element
inside a list.

    :::python
    li = ["apple","banana","pear","mango"]

    # to search for an index of an element
    li.index("banana") #will return 1
    li.index("orange") #will throws an exception, because orange isnt in the list

    # to check if an element is inside a list
    "apple" in li #return true
    "orange" in li #return false

There are several variations in removing an item from a list:

    :::python
    li = ['apple','banana','orange','pear','grape']

    # the basic del operation, which will remove an element at a specified index
    del li[0] #will remove apple

    # the remove() method, which will remove the first occurance of an element
    # this statement will remove the first occurance of banana
    # if there are more than one occurance of banana, only the first one will be removed
    # if there isnt any banana inside the list, it will raise an exception
    li.remove('banana')

    # the pop() method, which will remove the last value from the list,
    # and at the same time return that value
    li.pop() # will return grape, and remove it from the list

There are other operations on a list as well,

    :::python
    li = [1,2,3,4]
    ls = [5,6,7,8]

    # this will return the list[1,2,3,4,5,6,7,8]
    # similar to the extend() method, but it returns a new list
    # instead of directly performing the operation on the list
    li = li+ls

    # this will repeat the list 3 times, so the content of li
    # will be [1,2,1,2,1,2]
    li = [1,2]*3

Next is the tuple, a tuple is basically a list that cant be changed. It
has almost the same function the same functions as a list, but the
content can’t be changed, so a tuple doesn’t have the `remove()`, `pop()`,
`append()` or any other method that make changes to a list. Tuples are
usually used to create a constant list, whose values wont change. In
general, tuples are faster than lists, and there are also other specific
uses of a tuples that will be explored later. To create a tuple, the
syntax is similar to a list, but instead of a square bracket, a tuple is
declared with ordinary brackets.

    :::python
    tp = ('a','b','c')
    # it can be accessed the same way
    tp[0] #a
    tp[-1] #c
    tp.pop() #will throw an error

Those are the basic data structures in Python, each of those are kind of
similar to each other, but they have specific purposes that are unique
to each of them. For example, a tuple can contain a list of another
list, and a list can also nest several level of lists.
