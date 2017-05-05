# Initial Setup

  mkvirtualenv blog
  pip install -r requirements.txt

Main configs are in `pelicanconf.py`, and `publishconf.py` include some override for
github publish (production config of some kind).

## To Publish

  make publish.github

## Generate HTML with relative URLs for local server

  make build
  make serve
