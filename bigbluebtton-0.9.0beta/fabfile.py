#!/bin/python

from fabric.api import *


env.hosts = [ '115.68.184.117']
env.user= 'root'
env.password = prompt('PASSWORD:')

def before_install():
    run( 'cat /etc/default/locale')
    sudo("echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections")
    sudo(' apt-get -y install language-pack-en')
    sudo('update-locale LANG=en_US.UTF-8')

    machine = sudo('uname -m ')
    sudo('cat /etc/lsb-release')
    sudo('grep "multiverse" /etc/apt/sources.list')

def update_server():

    sudo(' echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty multiverse" | sudo tee -a /etc/apt/sources.list')

    sudo('apt-get -qq update ')
    run('apt-get dist-upgrade')

def install_ppa_libreoffice():
    sudo('apt-get -y install software-properties-common')
    sudo('yes | add-apt-repository ppa:libreoffice/libreoffice-4-3')

def install_key_for_bbb():
    sudo('wget http://ubuntu.bigbluebutton.org/bigbluebutton.asc -O- | sudo apt-key add -')
    sudo('echo "deb http://ubuntu.bigbluebutton.org/trusty-090/ bigbluebutton-trusty main" | sudo tee /etc/apt/sources.list.d/bigbluebutton.list')
    sudo('apt-get update')

def install_ffmpeg():
    put("install-ffmpeg.sh")
    run("chmod +x install-ffmpeg.sh")
    run("./install-ffmpeg.sh")
    run("ffmpeg -version")

def install_bbb():
    run("apt-get  update")
    run("apt-get -y install bigbluebutton")
    run("apt-get -y install bigbluebutton")
    run("apt-get -y install bbb-demo")

def enableWebRTCAudio():
    run("bbb-conf --enablewebrtc")
    run("bbb-conf --clean")
    run("bbb-conf --check")
    

def getConf():
    conf = [ '/opt/freeswitch/conf/vars.xml', '/opt/freeswitch/conf/sip_profiles/external.xml', '/usr/share/red5/webapps/sip/WEB-INF/bigbluebutton-sip.properties', '/etc/bigbluebutton/nginx/sip.nginx']
    for conf in confs:
        dst=conf
        src=basename(dst)
        get(dst, src)



def putConf():
    conf = [ '/opt/freeswitch/conf/vars.xml', '/opt/freeswitch/conf/sip_profiles/external.xml', '/usr/share/red5/webapps/sip/WEB-INF/bigbluebutton-sip.properties', '/etc/bigbluebutton/nginx/sip.nginx']
    for conf in confs:
        dst=conf
        src=basename(dst)
        put(src, dst)






def install():
    before_install()
    update_server()
    install_ppa_libreoffice()
    install_key_for_bbb()
    install_ffmpeg()
    install_bbb()
    enableWebRTCAudio()
    getConf()




