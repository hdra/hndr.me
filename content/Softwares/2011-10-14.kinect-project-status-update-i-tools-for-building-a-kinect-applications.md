Title: Kinect Project Status Update I - Tools for building a Kinect Applications
Date: 2011-10-14 12:24
Tags: kinect, programming
Summary: Update on my attempts on working with Kinect.

<a href="http://www.flickr.com/photos/hendra2392/6266069590/" title="Kinect by p.hdra, on Flickr"><img src="http://farm7.staticflickr.com/6177/6266069590_5f69b81c46_b.jpg" width="1024" height="681" alt="Kinect"></a>

Previously, I wrote about testing the water with Kinect, and well, it
seems like I am drowning now. The development process is much more
complicated that I thought.

To begin with, there are several drivers available for the Kinect, the
most commonly used are the official [Kinect for Windows SDK from
Microsoft][link1], the [OpenNI][link2] from PrimeSense, and the community maintained
[OpenKinect][link3] (libfreenect). So, the first problem is choosing which one
to install on your system, sounds easy enough, but it is not. All of
them have their own pro and cons, and they can't be installed on the
same system side by side, so let's talk about them one by one.

First, the Kinect for Windows SDK from Microsoft, as expected, this SDK
only support Windows systems, so its pretty straight forward to use it.
The installation is pretty simple as well, download the installer, and
run it on your computer, then you are ready to develop your own Kinect
applications. The development process is also straight forward, open up
Visual Studio, add the reference to the Kinect libraries, and start
using it. Microsoft also provided us with a series of [quick start
videos][link5], making it even easier for us get started. Developers also have
the choice to program in either C# or C++. For the time being this is
the one installed in my Windows system.

But, there are several downsides to this, the SDK is still relatively
new, so there are limited 3rd party libraries and projects, in addition,
the license agreement that come with the SDK is pretty restricting,
added with the fact the the source are not available, the aren't many
hackers out there are experimenting with it compared with the other two
options. Another catch is that it has a minimum range of 850mm from the
sensor for the depth camera to work, this is very important, as I think
there is a possibility that I am going to deal with finger gestures
pretty often, the distance would make it difficult to track the fingers.
I also haven't seen any libraries for gesture recognition provided for
this, even the AForge.NET libraries only support the libfreenect. But
then, the SDK is still in its beta stage, so I hope Microsoft can get
the official release out soon, with more features and less restricting
license agreement.

Next up is the PrimeSense's OpenNI. PrimeSense is the company who
developed the Kinect hardware for Microsoft. The are three primary
components of the driver they provide. They are the OpenNI library
itself, the NITE libraries, and the Sensor Driver. The Sensor Driver are
used so that the computer can recognize the sensor hardware (the OpenNI
doesn't only support the Microsoft Kinect, but it also support other
PrimeSense compliant hardware, such as Asus's Xtion), an alternative to
this is the [avin's Sensor Kinect][link4] which is a fork of the OpenNI's
Sensor driver. Next is the NITE libraries, the NITE libraries is an
optional component, it provides the algorithms for skeletal tracking and
other functionalities, and this library is not open source. Last, is the
OpenNI library itself, this component provides the functionality so that
the computer can consume the audio, color video, and depth video data
from the sensor.

OpenNI has been around for quite a while, and there are a lot of
projects developed using it, it is also cross-platform. There are many
software components that are built for it, such as the Point Cloud
Library, and OpenCV and many others. Of course, those libraries can also
be used for other drivers, but it would take quite a lot of work to do
it. The main language used in this SDK is C, but there are wrappers for
other languages provided. The driver is open source, and the license
provide quite a lot of freedom for the developers, so there are a lot of
projects built on it.

There is a installer wizard for Windows provided, but since I already
installed the Kinect for Windows SDK, I can't install it on my Windows
system. Since I also have Ubuntu installed on my laptop, I tried to
install it on it, but it is not as easy as I thought, after several
build errors and other stuff, I downloaded the binaries of all three
components, and installed it, but when i try to run any of the samples,
bit it gives me this error:

    InitFromXml failed: Failed to set USB interface!

I tried to build manually from the source, same error. Tried to built
with the RedistMaker provided with the source, same error. So, I haven't
been able to try it out.

Last but not least, is the OpenKinect. This one is open source as well,
and since it was one of the first Kinect hack available, there aren't
any shortage of project samples and 3rd party software components, the
AForge.NET framework also support this driver. Like the OpenNI,
OpenKinect is also a cross platform sofware, so we can install it on
Windows, Linux, or Mac OSX. The installation is much more
straightforward compared to OpenNI, there are only one component to
install, which is the libfreenect. The other dependencies can be easily
found as well. The one of the optional component is the
libfreenect-demos, which provides you with several sample project. Just
like the OpenNI, i tried to install it on my Ubuntu system. Tried to run
the sample, an error:

    Could not claim interface on camera: -6
    Could not open device

So, I haven't been able to run this one either.

So for now, I only have access to the Kinect for Windows SDK, I guess I
should just meddle with the Kinect SDK for now, and keep looking for
solutions on the other two alternatives.

[link1]: http://research.microsoft.com/en-us/um/redmond/projects/kinectsdk/
[link2]: http://www.openni.org
[link3]: http://www.openkinect.org
[link4]: https://github.com/avin2/SensorKinect
[link5]: http://channel9.msdn.com/coding4fun/kinect/Getting-started-with-the-Kinect-for-Windows-SDK-quickly-with-the-Kinect-Quickstarts
