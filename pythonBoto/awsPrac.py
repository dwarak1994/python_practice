import boto
import boto.ec2
import boto.ec2.elb
"""
conn=boto.ec2.connect_to_region("us-east-2")
#conn.run_instances('ami-0cd3dfa4e37921605')
rs=conn.get_all_security_groups()
for r in rs:
	print(r)

print(rs[17].rules)
"""

regions=boto.ec2.elb.regions()
#print(regions)
elb=boto.ec2.elb.connect_to_region('us-east-2')
print(elb.get_all_load_balancers())
