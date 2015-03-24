# -*- coding:utf-8 -*-
from __future__ import with_statement
import time

from fabric.api import run, cd, sudo
from fabric.operations import env

from settings import *

env.hosts = HOST_LIST

def archive():
    timestamp = '%d' % time.time()
    backup_filename = 'save.%s.tar.gz' % timestamp

    with cd(ARCHIVE_DIR):
        # Create a temporary wordpress dir's copy
        sudo('cp -rf %s wordpress.old' % WORDPRESS_DIR)
        # Don't save the uploads dir (static will be moved to the new wordpress)
        sudo('rm -rf wordpress.old/uploads')
        # Then create the tgz file
        sudo('tar cvfz %s wordpress.old' % backup_filename)
        # And remove the wordpress.old temporary copy
        sudo('rm -rf wordpress.old')

def update():
    """Update your wordpress blog.
    """

    # Archive your actual wordpress blog 
    archive()

    # Get the latest, create the new dir, and use it to replace the old one!
    with cd('~'):
        # Get the latest version of wordpress
        run('wget %s/%s' % (WORDPRESS_URL, WORDPRESS_TGZ))
        # Extract and remove tar.gz
        run('tar xvzf %s' % WORDPRESS_TGZ)
        run('rm -rf %s' % WORDPRESS_TGZ)
        # Remove wp-content and sample config
        run('rm -rf wordpress/wp-content wordpress/wp-config-sample.php')
        # Copy uploads and wp-content dir from the backup wordpress blog
        run('cp -rf %s/uploads wordpress/uploads' % WORDPRESS_DIR)
        run('cp -rf %s/wp-content wordpress/wp-content' % WORDPRESS_DIR)
        run('cp -rf %s/wp-config.php wordpress/wp-config.php' % WORDPRESS_DIR)
        # Remove current wordpress blog
        sudo('rm -rf %s' % WORDPRESS_DIR)
        # Deploy the new wordpress blog
        sudo('mv wordpress %s' % WORDPRESS_DIR)
        # Set the good right on files.
        sudo('chown -R %s:%s %s' % (SERVER_USER, SERVER_GROUP, WORDPRESS_DIR))
        sudo('chown -R %s:%s %s/uploads' % (HTTP_USER, HTTP_GROUP, WORDPRESS_DIR))

def update_plugin(plugin):
    """Update a plugin of your wordpress blog. 
    """
    if(PLUGINS[plugin]):
        (url, extract_command) = PLUGINS[plugin] 
        run('wget %s' % url)
        run(extract_command)
        with cd(WORDPRESS_DIR):
            timestamp = '%d' % time.time()
            plugin_archive_dir = '%s/plugins/%s.%s' % (ARCHIVE_DIR, plugin, timestamp)
            c_cp = 'cp -rf %s/%s %s' % (PLUGINS_DIR, plugin, plugin_archive_dir)
            sudo(c_cp)
            
        sudo('rm -rf %s/%s && cp -rf %s %s/%s' % (PLUGINS_DIR, plugin,
                                      plugin, PLUGINS_DIR, plugin))
        with cd('~'):
            run('rm -rf %s' % plugin)
    else:
        print u'Aucun plugin "%s" dans la configuration.' % plugin


def install():
    """Update your wordpress blog.
    """

    # Archive your actual wordpress blog 
    archive()

    # Get the latest, create the new dir, and use it to replace the old one!
    with cd('~'):
        # Get the latest version of wordpress
        run('wget %s/%s' % (WORDPRESS_URL, WORDPRESS_TGZ))
        # Extract and remove tar.gz
        run('tar xvzf %s' % WORDPRESS_TGZ)
        run('rm -rf %s' % WORDPRESS_TGZ)
        # Remove wp-content and sample config
        run('rm -rf wordpress/wp-content wordpress/wp-config-sample.php')
        # Copy uploads and wp-content dir from the backup wordpress blog
        run('cp -rf %s/uploads wordpress/uploads' % WORDPRESS_DIR)
        run('cp -rf %s/wp-content wordpress/wp-content' % WORDPRESS_DIR)
        run('cp -rf %s/wp-config.php wordpress/wp-config.php' % WORDPRESS_DIR)
        # Remove current wordpress blog
        sudo('rm -rf %s' % WORDPRESS_DIR)
        # Deploy the new wordpress blog
        sudo('mv wordpress %s' % WORDPRESS_DIR)
        # Set the good right on files.
        sudo('chown -R %s:%s %s' % (SERVER_USER, SERVER_GROUP, WORDPRESS_DIR))
        sudo('chown -R %s:%s %s/uploads' % (HTTP_USER, HTTP_GROUP, WORDPRESS_DIR))

def install_plugin(plugin):
    """Update a plugin of your wordpress blog. 
    """
    if(PLUGINS[plugin]):
        (url, extract_command) = PLUGINS[plugin] 
        run('wget %s' % url)
        run(extract_command)
        with cd(WORDPRESS_DIR):
            timestamp = '%d' % time.time()
            plugin_archive_dir = '%s/plugins/%s.%s' % (ARCHIVE_DIR, plugin, timestamp)
            c_cp = 'cp -rf %s/%s %s' % (PLUGINS_DIR, plugin, plugin_archive_dir)
            sudo(c_cp)
            
        sudo('rm -rf %s/%s && cp -rf %s %s/%s' % (PLUGINS_DIR, plugin,
                                      plugin, PLUGINS_DIR, plugin))
        with cd('~'):
            run('rm -rf %s' % plugin)
    else:
        print u'Aucun plugin "%s" dans la configuration.' % plugin
