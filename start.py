
import os, sys, time
import boto
import boto.vpc 
import boto.vpc.vpc 
import paramiko 
import urllib2
def startInstance(ami_instance, securitygroup, sshkeyfilename, keylocation, vpcid, delete):
    instance_type = 't2.micro'
    os.chdir(keylocation) # require path for pem file 
    ec2 = boto.connect_ec2() 
    ec2=boto.ec2.connect_to_region('us-west-1')
    vpccon = boto.vpc.connect_to_region('us-west-1')
    vpc = vpccon.get_all_vpcs(vpc_ids=[vpcid])[0] 
    sn=vpccon.get_all_subnets(filters={'vpc-id':[vpc.id]})[0]
    group = ec2.get_all_security_groups(group_ids=[securitygroup])[0]
    key = ec2.get_all_key_pairs(keynames=[sshkeyfilename])[0]
    reservation = ec2.run_instances(ami_instance,instance_type=instance_type, security_group_ids=[group.id],subnet_id=sn.id,key_name=key.name)
    instance = reservation.instances[0]
    while instance.state!= 'running':
        instance.update()

    return instance.ip_address + "," + instance.id

if __name__ =='__main__':
    count = 1
    ami_instance = 'ami-165a0876'
    #change security group-id and keypair to match what you have
    securitygroup = 'sg-3f8d5f58'
    keypair = 'MadhanMohanEC2'
    #change path to key folder to what is on your machine
    keylocation = '/Users/Happy/Downloads' 
    vpcid='vpc-b5f335d1'
    delete = False
    ip = startInstance(ami_instance, securitygroup, keypair, keylocation,vpcid, delete)
    sys.stdout.write(ip)
