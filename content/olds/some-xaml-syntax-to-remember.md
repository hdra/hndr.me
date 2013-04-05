Title: Some XAML syntax to remember
Date: 2012-08-14 14:17
Tags: programming, xaml, c#

After developing for WPF/ Silverlight for a while, most people will be
familiar with using XAML to declare UI elements, but even though I have
been comfortable with XAML for quite a while, I don’t really know what
is going on behind the stage. Reading Programming Windows by Charles
Petzold shed some lights on it for me, so this post is here again so
that I won’t forget.

One important thing I didn't know before is that XAML file more or less is just
another way to express the C# code, and the XAML elements in it are
actually .NET objects, and anything that can be declared in XAML can be
done in C# as well. Most page consists of two files, a `.xaml` file and a
`.xaml.cs` file, as the partial keyword in the C# file suggest, the
`.xaml.cs` file only consist a part of the class declaration. As we can
guess, the rest are declared in the XAML file. If we look at the
`obj/Debug` folder of the Project, we can see there are several files with
the name of `PageName.g.cs` and `PageName.g.i.cs`. During compile time, the
XAML file is parsed to get the elements and other information declared
in it to generate the intermediate C# file, which will then be compiled
together with our `.xaml.cs` file to generate the class declaration for a
particular page. In the `PageName.g.i.cs` file, we can actually see the
declaration for the `InitializeComponent` method that we always call in
the constructor of our `.xaml.cs` file. The method basically initiates all
objects declared in the XAML file, which is why if we try to get to
access an element declared in the XAML before the method is called, we
would get a `NullReferenceException`.

That’s enough for the backstage stuff, lets move on to the syntax. Most
XAML pages looks similar to this:

    :::xml
    <Page
        x:Class="App2.MainPage"
        IsTabStop="false"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:local="using:App2"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        mc:Ignorable="d">

        <Grid Background="{StaticResource ApplicationPageBackgroundThemeBrush}">
        </Grid>

    </Page>

As mentioned before, a XAML declaration can be expressed in C#, since
the elements in XAML file are .NET objects. The Page declaration above
basically declare an instance of `MainPage` in the `App2` namespace which is
a subclass from the `Page` class. The `xmlns` statements are standard xml
namespace inclusion which would allows us to use various elements.
Similarly, with these declaration:

    :::xml
    <Page
        x:Class="App2.MainPage"
        IsTabStop="false"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:local="using:App2"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        mc:Ignorable="d">
        <Grid Background="CadetBlue">
            <TextBlock Text="Hello"
                FontSize="96"
                Foreground="BlanchedAlmond"
                HorizontalAlignment="Center"
                VerticalAlignment="Center"/>
        </Grid>
    </Page>

The same result can be produced with these C# code:

    :::csharp
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
            Grid contentGrid = new Grid()
            {
                Background = new SolidColorBrush(Windows.UI.Colors.CadetBlue)
            };

            TextBlock txtBlk = new TextBlock()
            {
                Text = "Hello",
                FontSize = 96,
                Foreground = new SolidColorBrush(Windows.UI.Colors.BlanchedAlmond),
                HorizontalAlignment = HorizontalAlignment.Center,
                VerticalAlignment = VerticalAlignment.Center
            };
            contentGrid.Children.Add(txtBlk);
            this.Content = contentGrid;
        }
    }

As we can see, the XAML element properties are just another way to set
the values of the member variables of the objects. As we can see on the
C# code above, the the Foreground property of a TextBlock is of type
`SolidColorBrush` (or any subclass of the `Brush` class actually), but in
the XAML syntax, it seems like we are assigning a string to it. This is
because the compiler will parse and assign the appropriate attribute for
us.

The XAML code above shows two ways of setting a property of an XAML
element, namely the usual property attributes syntax, and the other one
is one known as the Property Element syntax. The property-element syntax
can be used to define some more complex attributes such as defining a
gradient background that requires defining more than one colours and
points. For example, the `TextBlock` above can be defined as such with the
property-element syntax:

    :::xml
    <TextBlock>
        <TextBlock.Foreground>
            <SolidColorBrush>
                Black
            </SolidColorBrush>
        </TextBlock.Foreground>
        <TextBlock.Text>
            Hello
        </TextBlock.Text>
        <TextBlock.FontSize>
            96
        </TextBlock.FontSize>
        <TextBlock.HorizontalAlignment>
            Center
        </TextBlock.HorizontalAlignment>
        <TextBlock.VerticalAlignment>
            Center
        </TextBlock.VerticalAlignment>
    </TextBlock>

Here we see that we defined the properties of the `TextBlock` by creating
another elements for each of them, and on for the Foreground property,
we explicitly defined a `SolidColorBrush` as the value of the property.
This is entirely optional, we can put the value inside the `Foreground`
tag and it would still work, just like we did with the other properties.
We don’t need to explicitly create a element of type `Double` for the
`FontSize`, nor we need to create another elements for the enumeration of
the alignment properties. We are still relying on the compiler to
actually recognize that the `Black` inside the tag is actually referring
to the colour enumeration, but there are times where would need to
explicitly define the property with the usual property-attributes
syntax.

In the previous example, we explicitly define what are the properties
and its value, but as we see on most XAML we see, there are many cases
where we don’t do that. For example, we didn’t explicitly define the
`rootGrid` element of our page is the value for the Content property of
the page, nor we need to explicitly define that our `TextBlock` is a
member of the `Children` property of the `Grid`. This is because every
classes referenced in XAML can have one and only one property that is
defined as its `ContentProperty`, where for these properties, the property
element tags are not required. So, instead of writing

    :::xml
    <Page>
        <Page.Content>
            <Grid>
                <Grid.Children>
                    <TextBlock/>
                    <TextBlock/>
                    <TextBlock/>
                </Grid.Children>
            </Grid>
        </Page.Content>
    </Page>

We can simply write:

    :::xml
    <Page>
        <Grid>
            <TextBlock/>
            <TextBlock/>
            <TextBlock/>
        </Grid>
    </Page>

And it would produce the same result. For the same reason, we can use
the same thing to define the `Text` property of a `TextBlock` without
creating property element tag for it, So,

    :::xml
    <TextBlock Text="Hello"/>

    <!-- Is the same as: -->

    <TextBlock>
        <TextBlock.Text>
            Hello
        </TextBlock.Text>
    </TextBlock>

    <!-- and -->

    <TextBlock>
        Hello
    </TextBlock>


I guess thats enough for now. Learning about all this made me realise 
that XAML is a very flexible and powerful language and can
be used for many things that can be done with C#, so knowing it would hopefully
be very useful in developing for the some of the latest Microsoft platforms (Win 8, WP 8, etc).
But of course, it is still a markup language, and it has several limitations, 
such as lack of logic processing, and inability to create instances of objects that requires
parameters in its contructor.
