Title: Still Working 
Date: 2013-04-03 17:16
Tags: personal


It has been a few weeks since I decided to start blogging again, but well, as usual not much has been done on it. For starter, I initially planned to host it on Heroku, following the tricks outline [here][l1], and it is super simple to setup. I had created a new Heroku app, generated the blog, and pushed the generated content to Heroku in just a few minutes. In another minute, and I had setup the custom domain and had everything working nicely.

Problem is, even though the site itself is just a bunch of static files, the first time I visited the site, it took a few seconds to load the content, but when I visit it again for the second time, it served the site almost immediately. At first, I thought it was because of the site is cached by the browser, so it loads much quicker, but even when I cleared the browser cache, it still loads the same way. After a bit of googling, I [found][l2] out that Heroku will turn off the dyno after an hour of inactivity, so everytime I visit the site after a period of idling, the dyno will need to be started again at that time. Not much of a problem, considering I am not even paying for the amazing service that Heroku provide, and there [ways][l3] to get around it anyway. I probably won't be using it, since I am still playing around with the hosting options around anyway.

Other popular service that people use to host their static site seems to be [Github Pages][l4]. After looking around on how to set it up, seems like it is pretty easy to set it up. The Pelican makefile even includes a build option for this setup. The site will be hosted in a repository just like any other git repo, but the site index will need to be on the `gh-pages` branch. In other words, the content of the site will be open source. Not a problem though, since any webpage that are publicly accessible are basically open source anyway. Maybe I'll move the site here after I am done setting the website itself.

On building the site itself, I just converted some of my old wordpress posts to Markdown, which should be published along with this post. The automatic converter doesn't work too well, since many of posts contains some really badly formed markups, so I ended up manually converting the most of posts. I also took the chance to just remove many of the rants/silly posts, not saying that there aren't any silly posts left anyway.

I am still playing around with the pelican configurations and options, on how to setup different static pages, building a theme, etc. Speaking about the theme, I drafted a theme of my own.

<a href="http://www.flickr.com/photos/hendra2392/8615163439/" title="Snap 2013-04-01 at 11.50.50 by p.hdra, on Flickr"><img src="http://farm9.staticflickr.com/8394/8615163439_30ea63f405_c.jpg" width="800" height="788" alt="Screenshot"></a>

Initially I liked it quite a bit, but after leaving it there for a few days, when I came back to work on it again, I found it to be not very attractive anymore. So, no need to say, I scrapped it, and started working from scratch. This time, planning the overall sites, starting from the landing page, static pages, comments, and of course the blog itself. Of course, it won't be around anytime soon. For the time being, the default Pelican theme seems more than good enough for me.


[l1]: http://kennethreitz.org/exposures/static-sites-on-heroku-cedar
[l2]: https://devcenter.heroku.com/articles/dynos
[l3]: http://stackoverflow.com/questions/5480337/easy-way-to-prevent-heroku-idling
[l4]: http://pages.github.com/