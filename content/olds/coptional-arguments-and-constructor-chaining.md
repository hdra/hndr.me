Title: C#–Optional Arguments and Constructor Chaining
Date: 2012-05-22 23:19
Tags: C#, programming


Learned something new about C# today, first thing is Constructor
Chaining.  Constructor chaining enables constructors to call another
overloaded constructor, with it, the amount of duplicate code can be
reduced significantly, here is an example:

    :::csharp
    class Person{
        string name;
        int age;
        string address;

        public Person(string name):this(string.Empty,0,string.Empty)
        {    }
        public Person(string name):this(name,0,string.Empty)
        {    }

        public Person(string name, int age):this(name,age,string.Empty)
        {    }

        public Person(string name, int age, string address)
        {
            this.name=name;
            this.age=age;
            this.address=address;
        }
    }

    // It can be used to call the base class' constructor as well, with the
    // base keyword

    class AwesomePerson:Person{
        int awesomenessLevel;

        public AwesomePerson(string name, int age, string address, int level):base(name,age,address)
        {
            this.awesomenessLevel = level;
        }

        public AwesomePerson(int level):this(string.Empty,0,string.Empty,level)
        {    }

    // and so on...
    }

With that, I can reduce the amount of code in the constructors, and
still get the options of passing only the argument that I need to the
constructors. There is another way to do this, starting with C# 4.0, it
introduced optional arguments that is common in dynamic languages, and
it is pretty awesome, and it can be combined with the constructors
chaining above for more power!

    :::csharp
    class Person
    {
        string name;
        int age;
        string address;

        public Person(string name = string.Empty, 
                      int age=0, 
                      string address = string.Empty)
        {
            this.name=name;
            this.age=age;
            this.address=address;
        }

    }

    // To create the instances:
    Person a = new Person();
    Person b = new Person("Joe");
    Person c = new Person(age:19,address:"Somewhere");
    Person c = new Person("John",23);

## References:
* <http://stackoverflow.com/questions/199761/how-can-you-use-optional-parameters-in-c>  
* <http://msdn.microsoft.com/en-us/library/dd264739.aspx>
