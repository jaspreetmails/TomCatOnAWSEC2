#!/usr/bin/env python2 
# _*_ coding: utf-8 _*_"""

import os, sys, time
import paramiko 
import urllib2
import boto
import boto.vpc
def terminate(instnaceID):
    conn = boto.vpc.connect_to_region('us-west-1')
    ec2 = boto.ec2.connect_to_region('us-west-1')
    vpcid='vpc-b5f335d1'
    security_group= 'sg-3f8d5f58'
    ec2.terminate_instances(instance_ids=[instnaceID])


if __name__ =='__main__':
    
    
    instId=sys.argv[1]
    sys.stderr.write('terminating instance {0} \n'.format(instId))
    time.sleep(100)
    terminate(instId)
    exit(0)
    
