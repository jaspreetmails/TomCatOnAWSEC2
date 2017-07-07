#!/usr/bin/env python2 
# _*_ coding: utf-8 _*_"""

import os, sys, time
import paramiko 
import urllib2
def install2(ip_address,sshkeyfilename,keylocation):

    sshuser = 'ec2-user'
    os.chdir(keylocation)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sys.stderr.write('ip='+ip_address)
    ssh.connect(hostname=ip_address, username=sshuser, key_filename=sshkeyfilename)
    stdin,stdout,stderr = ssh.exec_command("sudo yum -y install tomcat6 tomcat6-webapps")
    stdin.flush()
    data=stdout.read().splitlines()
    print data[-1]
    stdin,stdout,stderr=ssh.exec_command('sudo service tomcat6 start')
    stdin.flush()
    data=stdout.read().splitlines()
    print data[-1]
    stdin,stdout,stderr=ssh.exec_command('sudo service tomcat6 status')
    stdin.flush()
    data=stdout.read().splitlines()
    print data[-1]





if __name__ =='__main__':
    sys.stderr.write('sleeping\n')
    time.sleep(20)
    sys.stderr.write('wake up\n')
    ip=sys.argv[1]
    keypairfile = 'MadhanMohanEC2.pem'
    #change path to key folder to what is on your machine
    keylocation = '/Users/Happy/Downloads' 
    
    install2(ip, keypairfile, keylocation)
    exit(0)
    
