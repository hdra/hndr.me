Title: A Tiny bit on Firefox Extension
Date: 2013-08-20 14:33
Tags: Programming

I stumbled on [this][l1] article on creating Chrome extension, and really, it seems really
simple to do build an extension for the browser. So, I thought what would it take to build
the same thing for Firefox?

It turns out, it is pretty simple as well, but when you are just getting started, find out
where to get started aren't really straightforward. The getting started documents aren't
exactly well organized. To start with, there are two different ways to build an add-on for Firefox.
The XUL tool set, and also, the new Add-on SDK. The [add-ons developer page][l3] highlights the
Add-on SDK, but the links below mostly deal with the XUL tools. The difference between the two
can be found on [this page][l4]. Basically, the Add-on SDK is the one that is simpler, the
documentation can be found [here][l2].

Anyway, once you found the documentation, everything should be pretty easy to follow. Mozilla
provides [Add-on Builder][l5], a web-app that allows you to build add-ons for Firefox, but 
I prefer to download the SDK to my computer and use my preferred text editor. The SDK
is basically a python environment setup with everything you need to build an add-on, so you
would need to have python installed on your computer. Whichever method you chose, the method
are basically the same.

## Building the Add-on
So, moving on to building actual add-on. Like the example in the post linked above, it is 
a  simple add-ons that adds a context menu that allows you to search MDN for the selected text. 
To be honest, I am not sure what to write in this post, because it is much more simpler than 
I thought. 

Like the Chrome extension, a Firefox add-on is built with HTML/CSS and Javascript. There is a
`package.json` that contains the meta-data of the add-on that is a generated for you anyway.
Your code will mainly goes to the `main.js` file in the `lib` folder of your add-on directory.
You can put your extra data, such as to the CSS files, extra javascript libraries, images, etc
in the `data` folder. All these folders are generated automatically with the initialization of the
add-on, along with a `doc` and `test` folder, which pretty much describe themselves.

Here is the whole code for the add-on:

    :::javascript
    var contextMenu = require("sdk/context-menu");
    var tabs = require("sdk/tabs");

    var script = 'self.on("context", function(){'+
                 "    return 'Search MDN for \"'+window.getSelection().toString()+'\"';"+
                 '});'+
                 'self.on("click", function(){'+
                 '   self.postMessage(window.getSelection().toString());'+
                 '});';


    var menuItem = contextMenu.Item({
        label: "Search on MDN",
        context: contextMenu.SelectionContext(),
        contentScript: script,
        onMessage: function(selectionText){
            var url = "https://google.com/search?btnI&q=site:developer.mozilla.org "+selectionText;
            url = url.replace(" ", "+");
            tabs.open(url);
        }
    });

As you can see there, there isn't much to do. The first two lines are the import statement
to access some of the browser feature. Skip the `script` variable for now. Next, the we create
a new context menu, give it a label, and we declare the context so that the item only shows
up when there is a something selected.

Next, we pass the `contentScript` argument, which defines the behavior of the menu item even 
further. Many things can be done through the `contentScript`, such as to scope down the
context even further, set the click behaviour, etc. The argument takes a string, and we passed
the `script` variable as the argument. In this case, the `context` event is
are fired just before the context menu is displayed, and we change the label further to add
the selected text. We also handles the `click` event, and with it, we call the `postMessage`
to pass the the selected text, which we handle with the function passed to the `onMessage` 
argument, and in it, we open a new tab with the search URL.

As you might imagine, passing the script that defines the behavior of the add-on as a string
literal isn't really nice when script is something a little more complicated. You can pass
external javascript files to the `contentScriptFile` argument to accomplish the same thing.
Although there are several differences in the way the script is executed, but I won't go into
it too much in this post. More on it [here][l6].

There is a lot more you can do with the add-on. You can scan through more features available
on the documentation. There are more examples on the add-ons SDK's [Github][l7] repository.
By the way, the add-on mentioned above is available on [Github][l8] as well. Also, 
the add-on we built here is just a simple plugin to show the basics of the Firefox plugin API,
not really meant for actual use. It doesn't handle plenty of use cases, and it also relies 
on Google's Feeling Lucky version to directly open the first search first result. so 
I don't really recommend you actually using it for anything serious.


[l1]: http://coryg89.github.io/technical/2013/08/13/how-to-create-your-own-chrome-extensions/
[l2]: https://addons.mozilla.org/en-US/developers/docs/sdk/latest/dev-guide/index.html
[l3]: https://addons.mozilla.org/developers/
[l4]: https://addons.mozilla.org/en-US/developers/docs/sdk/latest/dev-guide/guides/sdk-vs-xul.html
[l5]: https://builder.addons.mozilla.org/
[l6]: https://addons.mozilla.org/en-US/developers/docs/sdk/latest/dev-guide/guides/content-scripts/loading.html 
[l7]: https://github.com/mozilla/addon-sdk
[l8]: https://github.com/hdra/ff-MDNSearch