Title: Setting up my Linux to be less ugly
Slug: making-my-new-linux-less-ugly
Date: 2013-06-1 14:57

As I [decided][lin] to setup a new Linux installation that is lightweight, customizable to my taste,
can be made look pretty, and of course, usable, I started looking around for the suitable 
setup.

First thing I need to decide on is which Linux distribution to use. I can either look for something
bare bone like the Arch, and then build up everything I need, or I can just take something that
is ready to use, like Ubuntu, and take out whatever I don't need and replace anything I don't like.
I am tempted to take the former approach, but looking at some youtube videos on the stuffs I would
need to do, there seems to be just way too many things to do before I can even do anything. Even 
for basic things like network access needs to be setup. So, well, no thanks. Maybe next time.

I ended up deciding on the distribution I am familiar with, Linux Mint 13 XFCE. Now, even as it is,
the XFCE distribution is lightweight enough for me to use smoothly. It doesn't look bad, and it
is very customizable. I was tempted to settle on it, but for some reason, I had frequent crashes
during my use with it. Anyway, it is good enough for me to use as a base. 

I had been read a lot about tiling window manager, and has been wanting to try it out. [XMonad][l1] 
seems to be the one that is mentioned most frequently, but setting it up seems like a pain. Not to 
mention the  500MB I am supposed to download with it. I found another option, [i3][l2]. And it seems 
to be a lot easier to setup and use. The configuration is done with plain text file instead of 
a scripting language like Haskell as is the case with XMonad. People had good things to say
about how easy it is to use as well. Once I saw the video demo, I am sold.

<iframe width="480" height="360" src="http://www.youtube.com/embed/Wx0eNaGzAZU" frameborder="0" allowfullscreen></iframe>

## Installing i3
Installing i3 is easy enough. It is listed in the Ubuntu package repository, so it is also available
for Linux Mint that is based on Ubuntu, but I find the version available in the repository to be
severely outdated and have some problem with rendering some fonts, so installing the latest 
stable version from i3's repository is recommended. The instruction on their download page is easy 
enough to follow:

    # echo "deb http://debian.sur5r.net/i3/ $(lsb_release -c -s) universe" >> /etc/apt/sources.list
    # apt-get update
    # apt-get --allow-unauthenticated install sur5r-keyring
    # apt-get update
    # apt-get install i3

One thing to take notice here is the first line, which is used to add the repository to our
sources. Only problem is, the `lsb_release -c -s` in my system will output `maya`, since that is
indeed what my system is. That will cause the link to return me an 404, since, of course, the 
repository was meant for Ubuntu, and there is not Ubuntu version code named `maya`. Since I 
know Linux Mint 13 was build on Ubuntu Precise, I can just replace it with that.

    # echo "deb http://debian.sur5r.net/i3/ maya universe" >> /etc/apt/sources.list

After the installation is done, I log out, log in again, this time selecting i3 in the session
manager, and I am in.


## Making it less ugly
Out of the box, i3 looks pretty hideous. I didn't take any screenshot because at that point
I haven't even figured out how to take a screenshot yet. But it is just a black screen with a 
little black bar at the bottom anyway. In any case, it is time to to do some makeover. The 
documentation for the i3 is really clear and nice to read. So, there wasn't much problem to 
figure out what to do. The configuration file is stored at `~/.i3/config`. First thing to change
is the color. I don't know much about design, but I do know when to avoid using the pure black and
pure white color. Thing #1 to change: the window title color.

    client.focused          #3F8AC2 #096BAA #00BAA7 #00DA8E
    client.focused_inactive #333333 #5F676A #ffffff #484e50
    client.unfocused        #333333 #424242 #888888 #292d2e
    client.urgent           #C10004 #900000 #ffffff #900000

Next, the status bar. I prefer mine on top of the screen. Also, the color.

    bar {
        position top
        status_command i3status
        tray_output LVDS
        colors{
            background #232323
            statusline #DCDCDC
        }
    }

Next thing, time to change that 80s font face.

    font pango: Ubuntu Mono 10

By now, it looks much better. Next is the wallpaper. I use `feh` to set my wallpaper.

    exec --no-startup-id feh --bg-fill /home/hdra/Pictures/Wallpapers/city.jpg

This is how the 'desktop' looks like right now.

![Desktop][p1]


# Setting up GTK
By now my desktop doesn't look half bad, but if I open any gtk-based application, especially
gtk3 application, it looks like complete crap. So, next thing to deal with is the gtk theme
and icons. The configuration file for gtk2 is located at `~/.gtkrc-2.0`, while for gtk3 is located
at `~/.config/gtk-3.0/settings.ini`. I want the applications to look consistent, so I had to
look for one that can provide similar looks for both. There are some of the built-in theme that can
do this, but I want something else. I decided on the MediterraneanLight from [gnome-look][l3].
I also picked up an icon set from there. Next thing to do is to change the font. I never liked
how fonts in Linux OS are always unnecessarily big. So, I switched to a lower font size.

Here is my gtk2 configuration:

    gtk-theme-name = "MediterraneanLight"
    gtk-font-name = "Open Sans 8"
    gtk-icon-theme-name = "Faenza-Dark"

And here is the gtk3 configuration:

    [Settings]
    gtk-theme-name = MediterraneanLight
    gtk-font-name = Open Sans 8
    gtk-fallback-icon-theme = Mint-X
    gtk-icon-theme-name = Faenza-Dark

And now here is how it looks like:

![File Manager][p2]

Here is some more screenshots with the tiling in action:

![Tiling 1][p3]

![Tiling 2][p4]

Next is on setting it up to be more usable!

[p1]: https://farm4.staticflickr.com/3665/8910945270_db72193fae.jpg
[p2]: https://farm6.staticflickr.com/5459/8910222885_22f206f546.jpg
[p3]: https://farm6.staticflickr.com/5444/8901017483_1e29ac330a.jpg
[p4]: https://farm4.staticflickr.com/3724/8901630850_57c45b5fd2.jpg
[l1]: http://www.xmonad.org
[l2]: http://www.i3wm.org
[l3]: http://www.gnome-look.org
[lin]: (|filename|linux-again.md)