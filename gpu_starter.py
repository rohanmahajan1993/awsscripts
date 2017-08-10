import boto
import boto.ec2

#good tutorial http://boto.readthedocs.io/en/latest/ec2_tut.html
conn = boto.ec2.connect_to_region('us-west-2')

# starts a new instance
def start_instance(ami):
   conn.run_instances('ami-ffe15c9f')

#terminate all instance
def terminate_instances():
   # reservations is any command that starts one or multiple instances
   reservations = conn.get_all_reservations()
   for reservation in reservations: 
        for instance in reservation.instances:
	   conn.terminate_instances(instance_ids=[instance.id]) 
