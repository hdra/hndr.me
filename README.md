HNDR.ME
=======

This is the content website of hndr.me, currently built with Pelican.

To start re-using, install all of the requirements, and change the configurations as necessary.
Setup the required themes.

To generate the blog:

    pelican -s configurations.py

The content will be generated at `output`. To deploy, just use any static webserver.
To deploy to Heroku, just add an `.htaccess` file with the content:

    php_flag engine off

and also, add an file named `index.php` to the root directory. This will cause the server to consider the appication as a PHP application, but with the php engine turned off, will serve the static HTML instead. 

or of course, set up whatever server neccesary.

## Heroku Hosting state
currently, the site is hosted on Heroku, in other words, the generated output are tracked with git. So if the content were to be wiped, the Output needs to be cloned in order to have be tracked to the same repository.