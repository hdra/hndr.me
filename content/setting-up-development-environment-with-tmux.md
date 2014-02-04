Title: Setting up Development Environment with tmux
Date: 2013-07-09 16:02
Tags: programming

I recently just finished up my bachelor studies, and as I wait for the the convocation, I find myself not knowing what to work on. So,  between tying up loose ends with my scholarship sponsor, trying to score a freelance projects, and wasting time watching TV series, I spent my time playing around with various web front-end frameworks and libraries without any particular aims. In doing this I ended up creating a bunch of throw-away projects, and I switch around between them randomly quite often. Often, I would have to run several commands to get everything up and running again, which would be easy if it involves only starting up an editor, but most of the time, I would have to type the same commands many times when I start working on a project. Of course, this doesn't only apply to this particular situation of me experimenting around with various tools, even when working on a more "serious" project, I can benefit from automating the setup of the development environment.

The first idea that came to my thought is simply write a batch script to start the tools that I need, but I realize that this won't work well, since most of the tools that I are long running processes, such as a web server, or maybe CSS pre-compiler set to watch for changes in my project. Also, the log messages that these tools produce on the terminal are things that I would prefer to see. So, I would need a something that can help me to manage several terminal processes easily. The first thing that came to mind is [GNU Screen][screen].

I read about terminal multiplexer and their use before, but this is the first time I thought of a use for them myself. So, I read around trying to look for how to use `screen` to do the things I need, and it seems like there is a superior alternative to screen, which is [tmux][tmux], so I switched my focus to it instead.

So, what tmux does is basically it allows me to easily run multiple programs in a single shell session , switch between them, and manage them from the parent terminal. It is almost like a terminal emulator within your terminal. Perfect for what I needed.

In most of my experiment projects, I usually have at least python web server, compass watch, and livereload server running. Instead of starting the one by one, with tmux, I automate it, and at the same time have them arranged neatly in their own window/ pane. I can start a new tmux session, label it, and detach from it with `tmux new-session -s my-dev -d`. I can also pass a new command for it to run. For example, I want it to create a new v-split pane and run `top` in it, I can just enter `tmux split-window -v -t my-dev "top"`. Awesome. For example, to create a tmux session with the setup consisting of python web server, livereload server, etc I mentioned above, I can just run these script:

    tmux new-session -s my-dev -d "python -m SimpleHTTPServer 8899"
    tmux split-window -v -t my-dev "compass watch"
    tmux split-window -v -t my-dev "guard"
    tmux select-layout -t my-dev tiled

And I would have all these 3 process running inside a detached tmux session in the background. If I ever need to see the log messages, I just run `tmux attach` and have this shown to me:

<a href="http://www.flickr.com/photos/hendra2392/9247967451/" title="Tmux screenshot">
    <img src="https://farm4.staticflickr.com/3694/9247967451_6169fb7941_c.jpg" width="800" height="433" alt="Tmux">
</a>

Of course, If you prefer stay inside tmux, you can just leave out the `-d` flag. You can also start a new editor inside it, create an empty tab for you run other commands on, almost anything that you can do on a terminal, automated.

That is awesome. But, you can automate it even further, and make your life even easier. [Tmuxinator][mux] is a tool that allows you to create and manage tmux session easily. You create project with `mux new project-name`, and open the config with `mux open project-name` (`mux` is an alias for tmuxinator). The config will look something like this:

    # ~/.tmuxinator/project-name.yml

    project_name: project-name
    project_root: ~/project/project-name
    tabs:
      - editor: vim
      - logs:
            layout: even-vertical
            panes: 
                - python -m SimpleHTTPServer
                - compass watch
                - guard
      - shell: #empty, run plain shell

I am sure I don't need to explain that file. It stores the configuration of the environment in an easy to write (and read) format, and you can start it with `mux project-name` and it will create the session you need with the layout you need. You can read more about it in the project's README file. Tmuxinator obviously make something that make our job easier, even easier, but there is one caveat though. As you probably have noticed, tmuxinator is written in Ruby, and that means the tmux session it create will be a child process of Ruby, instead of your shell. You can read more what does this means [here][cav].

Obviously, tmux is powerful tools that can be used for more than just automating environment setup, I myself am still in discovering its capabilities. Search around for more information on customizing and using it, and of course, the `man` page of the tmux itself is a great source of information.

[tmux]: http://tmux.sourceforge.net/
[screen]: http://www.gnu.org/software/screen/
[mux]: https://github.com/aziz/tmuxinator
[cav]: http://natedickson.com/blog/2013/05/10/from-the-desk-of-captain-obvious-tmuxinator-vs-scripted-configurations/