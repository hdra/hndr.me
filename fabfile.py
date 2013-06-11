from fabric.api import *
import publishconf as conf

output_dir = conf.OUTPUT_PATH
remote_git = 'git@github.com:hdra/hndr.me.git'
activate = 'workon hndr.me'


def init():
    local('mkdir {0}'.format(output_dir))
    with lcd(output_dir):
        local('git clone -b gh-pages {0} .'.format(remote_git))
    if 'does not exist.' in local(activate, capture=True):
        local('mkvirtualenv hndr.me')
        with prefix(activate):
            local('pip install -r requirements.txt')


def update(commit_msg='update'):
    if 'nothing to commit' not in local('git status', capture=True):
        local('git add -A')
        local('git commit -m "{0}"'.format(commit_msg))
        local('git push origin master')
        local('git push bitbucket master')
        print "Success updating source"
    else:
        print "No changes on source"


def pub(commit_msg='Post update'):
    # Update master branch
    update(commit_msg)
    # Generate posts
    with prefix(activate):
        local('pelican -s publishconf.py -v')
        print "Site generated successfully"
    # Update gh-pages branch
    with lcd('output'):
        local('git add -A')
        local('git commit -m "{0}"'.format(commit_msg))
        local('git push origin gh-pages')
        print "Site published successfully"
