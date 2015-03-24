HOST_LIST = ['my_http_server_name_or_ip',]

WORDPRESS_URL = 'http://wordpress.org'
WORDPRESS_TGZ = 'latest.tar.gz'
WORDPRESS_DIR = '/var/www/my_blog.tld/htdocs'
ARCHIVE_DIR = '/var/www/my_blog.tld/archives'
PLUGINS_DIR = '/var/www/my_blog.tld/htdocs/wp-content/plugins'

""" { 'plugin_name' : ('url', 'extract_command_line'), }
    There are two plugins I use on my wordpress, but feel free to remove
    them of this list!
"""
PLUGINS = {'akismet': ('http://downloads.wordpress.org/plugin/akismet.zip',
                       'unzip akismet.zip && rm akismet.zip'),
           'BigBlueButton' : ('http://download.wordpress.org/plugin/bigbluebutton-1.4.0.zip' ,
                           'unzip bigbluebtton-1.4.0.zip && rm bigbluebutton-1.4.0.zip'),
           'Easy Content Templates' : ('http://download.wordpress.org/plugin/eazy-content-templates.zip' ,
                           'unzip eazy-content-template.zip && rm eazy-content-templates.zip'),
           'Register Plus Redux' : ('http://download.wordpress.org/plugin/register-plus-redux.zip' ,
                           'unzip eazy-content-template.zip && rm register-plus-redux.zip'),
           'bad-behavior': ('http://downloads.wordpress.org/plugin/bad-behavior.zip',
                            'unzip bad-behavior.zip && rm bad-behavior.zip')}

SERVER_USER = 'root'
SERVER_GROUP = SERVER_USER
HTTP_USER = 'www-data'
HTTP_GROUP = HTTP_USER
