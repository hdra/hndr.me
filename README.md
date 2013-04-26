# Initial Setup
After cloning the repo, setup the whatever theme necessary, set the virtualenv
path, run:

    fab init

to clone the gh-pages branch. If there is no gh-pages branch in the remote repo, then
set one up.

# Update
    fab update:"commit msg"

Only update the master repository without generating new posts

# Publish
Run:

    fab pub:"commit msg"

This will push the updates to remote repos, generate the new posts,
and publish to gh-pages.

