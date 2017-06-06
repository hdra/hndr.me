Title: Threading in C#
Date: 2012-05-31 23:05
Tags: C#, programming


Well, this time, I am going to talk about thread, the concept of thread
is pretty simple to understand, so I wont explain the here, but you can
read more about it in this [wiki page][link1]. Threading are used quite
extensively in most modern computer programs, for example separating
threads to handle button clicks on a GUI button from the one that
handles data processing, or in chatting programs, where it separates
threads to send messages from the one that handles incoming messages and
display it on the screen.

In .NET, threading is handled by the `Thread` class, which lives in
the `System` namespace, so to use it, you need to add this first:

    :::csharp
    using System.Threading;

To create a new thread, we need to create a new Thread instance, which
takes a [delegate][link3] of type `ThreadStart` (remember that delegate is
like a pointer to a method? this would mean that the thread will run the
method that the delegate parameter points to.). ThreadStart itself is a
delegate that does not return any value or accept any parameter. Here is
an example:

    :::csharp
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    using System.Threading;

    namespace ConsoleApplication1
    {
        class Program
        {
            static void Main(string[] args)
            {
                ThreadStart someCode = delegate() { for (int i = 0; i < 5;i++)Console.WriteLine(i); };
                Thread t1 = new Thread(someCode);
                Thread t2 = new Thread(someCode);
                Thread t3 = new Thread(someCode);

                t1.Start();
                t2.Start();
                t3.Start();

                someCode();
                Console.Read();
            }
        }
    }

You will see that the each number will be printed 4 times, but in no
particular order, the operating decides which threads gets run at any
given time, but you can see that the same method is being run in 4
different threads. The three threads that we created with the Thread
class, and the main thread of the program itself.

In the example above, the threads are all accessing local variables,
that is, they don’t share any data between them. This makes things
pretty simple, but there are times where the threads are accessing a
shared data, and this may cause a problem known as [race condition][link2]. To
prevent, that, we need a way sync the data by locking the data to a
thread during a section of the program that may cause a race condition.
In .NET, the Threading namespace provides us with a Monitor class that
we can use to lock an object. Here is an example.

    :::csharp
    var sharedData = new SomeClass();

    // lock the sharedData
    Monitor.Enter(sharedData);

    // Write the critical codes here.
    // Codes between the Enter and Exit can only be performed by one thread
    // at a time,

    // release the sharedData
    Monitor.Exit(sharedData);

Thread synchronization is pretty complicated topic, I think will cover
them in another post some time later, when I got a better understanding
of it. [Here][link4] is an MSDN article on the topic.

The Thread class provides several methods to control the execution of
the thread, here are some of them:

    :::csharp
    // these examples are called from within the execution of another thread
    // e.g. t2

    // Pausing the current thread execution for 2 seconds
    Thread.Sleep(1000);

    // Wait for t1 thread to finish executing
    t1.Join();

    // stop the execution of a thread
    t1.Abort();

    // pause the thread
    t1.Suspend();

    // resume the thread
    t1.Resume();

    // accessing the thread state
    t1.ThreadState

C# also provides some methods to control the execution of another
process via the `Process` class in the `System.Diagnostics` namespace,
but I’m not too concerned about that for now, so this post ends here.

## References:
* <http://msdn.microsoft.com/en-us/library/aa645740(v=vs.71).aspx>
* <http://www.albahari.com/threading/>
* <http://www.c-sharpcorner.com/uploadfile/mgold/multithreadingintro10062005000439am/multithreadingintro.aspx>

[link1]: http://en.wikipedia.org/wiki/Thread_(computing)
[link2]: http://en.wikipedia.org/wiki/Race_condition
[link3]: http://www.myblog.name/2012/05/delegates-in-c-and-a-tiny-bits-of-events/
[link4]: http://msdn.microsoft.com/en-us/library/ms173179.aspx