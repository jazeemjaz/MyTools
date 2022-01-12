import os
ip = "10.102.172."
for x in range(79,100):
	hostname = ip+str(x)
	response = os.system("ping -i 0.1 -c 1 " + hostname)

	#and then check the response...
	if response == 0:
  		print hostname, 'is up!'
	else:
 		 print hostname, 'is down!'
