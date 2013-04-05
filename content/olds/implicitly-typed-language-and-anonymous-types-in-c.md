Title: Implicitly Typed Language and Anonymous Types in C#
Date: 2012-05-30 23:16
Tags: C#, programming

In C#, there is this `var` keyword, which allows you to declare a
variable without explicitly specifying its data type. It is important to
note, that this doesn’t mean that it is dynamically typed, it simply
means that the compiler will infer the data type for you, and it is also
important to note, that it is strongly typed. So, this code below, will
simply create a variable called x, with the data type of string.

    :::csharp
    var x = "Hello";

Since `x` is a strongly typed `string`, if you try to assign `x` to an
`int`, it will throw an error. Even though it may seems inflexible, it
is necessary when we are using anonymous types.

Anonymous Types allows you to query a set of data, without having to
create a class/struct to hold it. For example, if I wanted to to query a
Car database, if I want to put it in a proper data structure,
I can either put it in a hash table object, or I would have to declare
a class first.

    :::csharp
    class Car
    {
        int year;
        double price;
        string model;
    }

With anonymous type, we can do something like this:

    :::chsarp
    var myCar = {year=1990,price=100000,model="unknown"};

Behind the scene, the compiler will actually generate a class for us,
with all of the necessary properties with it. This can be especially
useful if we need to query just a subset of the properties, and creating
the new objects without all of its properties isn’t very feasible.

## References:
* <http://msdn.microsoft.com/en-us/library/bb397696>