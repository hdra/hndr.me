Title: More fun with Linux
Date: 2013-06-11 13:04
Tags: linux

#Terminal
The best feature of a Linux system is its CLI tools, so of course, the terminal is an important tool to have. My first choice was [urxvt][l3], it was lightweight, supports unicode, have quite an active community with various customization with it, and it doesn't have a menu bar, which is perfect for the i3wm I am using. Copy and pasting aren't as straightforward as I hoped, as I need to setup some script to get the basic function working, but I could live with that. The deal breaker problem is that it for some weird reason produces weird text artifacts when I resizes the window, which is really important to me, since one of the main the reason I am using a tiling window manager is for the flexibility and ability to quickly resize windows using keyboard.

So, I settled for Terminator. It wasn't ideal, it was rather packed with features I don't really need, such as tabs and split windows. I have no need for these features, as I am already using a tiling window manager anyway. But at least it works, and it got a bad ass name.

There isn't much of a terminal to customize, so I only set the font type, hid the title bar, and changed the color scheme. I wrote a [script][l4] to convert iTerm color schemes to the terminator palettes, since seems like the iTerm users enjoy a great list of color schemes around.

##Shell
To be honest, I don't really need to change my shell to anything other than what was provided as the default (that is, bash). Its not like I have overgrown bash and need something more powerful anyway. But, since all the cool people are saying [how][l6] [awesome][l7] it is, so I jumped on the [ZSH][l5] bandwagon anyway. And it turns out, it really is cool, among other things, one that I enjoy the most is its autocompletion. Just awesome. I was about to dive deeper and have fun customizing almost every aspects of it, but somewhere along the way, I realized:

<a href="http://www.flickr.com/photos/hendra2392/9014788639/" title="its a trap by p.hdra, on Flickr"><img src="http://farm9.staticflickr.com/8275/9014788639_93815e99c4_o.jpg" width="197" height="256" alt="its a trap"></a>

I am about to spend too much time customizing the system again. So, I simply turned to the awesome [oh-my-zsh][l8] package, the default is more than good enough for me, all I need to do is to just add a couple of extra lines to the `.zshrc` file to set some alias and environment variables.


#Text Editor
The last few times I tried to work in Linux, I never really tried to setup a nice text editor to use. Big mistake. IMO the text editor is the most important tool in a programmer's pocket. Last time, I settled with something way too simple, such as gedit, or something way too complex to get to work, vim. No need to say, I never even got any real productivity working in it.

This time, the I have a wonderful text editor that I have been using from Windows. Yep, [Sublime Text 2][l9]. It really is the best text editor I have ever used. The plugins, the themes and color schemes, and the community around it are simply awesome. Even without any plugin, it is still a solid text editor, with its command palette, multi-cursor, and many others. Best thing of all? It is cross-platform, available on all 3 major OSes, not the Mono or Java kind of cross platform, but a native application all way through.

Installing it in Linux, it is pretty straightforward, downloading it from the website, extracting it, and thats it. For those who are too lazy to go to the website and download the archive, there is this command that you can use:

    cd ~
    wget http://c758482.r82.cf2.rackcdn.com/Sublime Text 2.0.1 x64.tar.bz2
    tar vxjf Sublime\ Text\ 2.0.1\ x64.tar.bz2

There is also an unofficial repository maintained by the people at webupd8:

    sudo add-apt-repository ppa:webupd8team/sublime-text-2
    sudo apt-get update
    sudo apt-get install sublime-text-2

Next thing, adding the the executable to path so that it can be easily started:

    sudo ln -s ~/Sublime\ Text\ 2/sublime_text /usr/bin/subl

There is a problem with the script above though. Running the command on the terminal will make the shell to wait for the program to exit, making us unable to do anything else on that terminal. So, to fix that, I made a little script to run it in the background, independent of the terminal.

    #!/bin/bash
    (subl "$*" &> /dev/null &)

All I got to do left is to install the packages that I have been using on Windows. Installing my packages from Windows aren't that hard, since I installed my sublime text extras from the [Package Control][l10], all of my installed packages are listed in the `Package Control.sublime-settings`, and the only thing left I need to do was to copy all my other configurations over, and just modify a little from the hotkey configuration.


#LAMP Stack
I still do a lot of PHP development, however uncool that may be nowadays. From messing around with WordPress and general web development, I still find PHP irreplaceable. I even intend to pick up [Laravel][l1] to see what it can do.

So, easiest way to do it is of course, the combination of Apache web server, MySQL, and the PHP stack. On Windows, I have been spoiled with ease of setup that is [XAMPP][l2]. Good thing is, it is also available on Linux, but this time, I would like to take the opportunity to do it differently. I want to the parts manually so that I know how they work together. Fortunately, it is not that hard to setup on Linux, as most of the packages needed are readily available on the software repository.

So, here are the packages needed, first of all, is the Apache web server.

    sudo apt-get install apache2

By now, visiting `localhost` on your web browser should give you something to be happy about. Next thing to install is the MySQL.

    sudo apt-get install mysql-server

When the install is finished, you should get asked to perform the initial setup for the MySQL server, including setting up the user authentication and stuffs. Now the last piece of the stack is to install php.

    sudo apt-get install php5

Now, for them to work together, there are a couple more packages to be installed.

    sudo apt-get install libapache2-mod-php5 libapache2-mod-auth-mysql php5-mysql phpmyadmin

Now, restart apache with `sudo /etc/init.d/apache2 restart`, and try to put some PHP code in `/var/www` and navigate to the address to see if it executed properly. Also, add this line to `/etc/php5/apache2/php.ini`: `extension=mysql.so` to get PHP to work with MySQL. Also, add the line `Include /etc/phpmyadmin/apache.conf` to `/etc/apache2/apache2.conf` so that the server know where to find phpmyadmin. Restart the server again, and the server is set to go.

Now, the server is ready to use, but there are still a few things to do to make it pleasant to use. One is the document root of the apache web server is located at the not so easy to access location of `/var/www`, so its better to move that to somewhere inside the home directory. To do that. the file to edit is `/etc/apache2/sites-available/default`. It should be pretty obvious which lines to edit once you open that file. Also, while this might not be necessary, you can create an alias for `/etc/init.d/apache2` so that it can be easily accessed.



[l1]: http://laravel.com/
[l2]: http://sourceforge.net/projects/xampp/
[l3]: http://software.schmorp.de/pkg/rxvt-unicode.html
[l4]: https://github.com/hdra/itermcolors2terminator
[l5]: http://www.zsh.org/
[l6]: http://fendrich.se/blog/2012/09/28/no/
[l7]: http://mikegrouchy.com/blog/2012/01/zsh-is-your-friend.html
[l8]: https://github.com/robbyrussell/oh-my-zsh
[l9]: http://www.sublimetext.com/
[l10]: http://wbond.net/sublime_packages/package_control