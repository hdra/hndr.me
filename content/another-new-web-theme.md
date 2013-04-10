Title: Made another design for the blog
Date: 2013-04-10 09:02
Tags: programming, design


Recently I have been spending my time messing around with website front-end development.
Probably because of I have been trying to write a Pelican theme for my own website. For My own 
use, I wanted the website to have a landing page, and also another design for the blog index. 
I made another attempt at the design recently. Here is the landing page:

![Landing page design][sc1]

and here is the blog index:

![Blog index page design][sc2]

I also managed to made the design responsive. Kind of. I just made the sidebar go to the top
of the page when the window is resized to below 800 pixels of width. 

![Blog index version 2][sc3]

The design itself is currently still a static HTML page that I made on top of the pretty
cool [HTML5 Bootstrap][h5bp]. For some reason I got a feeling that I am not using it to its full 
potential, as I don't really utilizes anything from it beyond the basic page structure and the 
included `normalize.css`. Obviously I am doing something wrong. One thing that I notice in the 
main CSS file is this line:

    :::css
    @media only screen and (min-width: 35em) { }

I knew about the media query and used it before, but I used to use it with the `max-width` instead.
So, the idea here is to design for the mobile version first, then make the necessary changes for
the larger screen. I have heard about this mobile-first approach a lot before, and I am aware 
of the arguements for and against it, but I never really
gave it any thought, mostly because I am not doing any serious front-end stuff anyway, but I am 
thinking of trying this approach for my next try on web design. 

I am also planning to play around more with front-end development. The past few days trying to make
the HTML page to look exactly how I want it to look like made me realize that I don't really know much 
about front-end development. Most of the time, web-development for me consists of dealing with generating
HTML page from the server and maybe make a Javascript function to make a server call to change the 
page dynamically, but I never really go deep into HTML and CSS itself. Looking into more than
tools and frameworks that I can use to make the job easier.

Anyway, as mentioned before, the designs above are still in a static HTML form, and I think it 
is good enough for me to use. Maybe I'll turn it into a proper Pelican theme soon.

[sc1]: http://farm9.staticflickr.com/8254/8636534196_ac410cec50.jpg
[sc2]: http://farm9.staticflickr.com/8519/8636534164_497989410e.jpg
[sc3]: https://farm9.staticflickr.com/8248/8635873575_153dd6e05e.jpg
[h5bp]: http://html5boilerplate.com/