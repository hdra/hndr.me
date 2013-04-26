from fabric.api import *
import configurations as conf


output_dir = conf.OUTPUT_PATH
remote_git = 'git@github.com:hdra/hndr.me.git'
activate = 'env\\Scripts\\activate.bat'


def init():
    local('mkdir {0}'.format(output_dir))
    with lcd(output_dir):
        local('git clone -b gh-pages {0} .'.format(remote_git))


def pub(commit_msg='Post update'):
    # Update master branch
    local('git add -A')
    local('git commit -m "{0}"'.format(commit_msg))
    local('git push origin master')
    # Generate posts
    with prefix(activate):
        local('pelican -s configurations.py -v')
    # Update gh-pages branch
    with lcd('output'):
        local('git add -A')
        local('git commit -m "{0}"'.format(commit_msg))
        local('git push origin gh-pages')
