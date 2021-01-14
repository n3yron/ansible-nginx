#!/bin/python2
import os, re, subprocess, shutil, getpass

def my_function():
	if getpass.getuser() == 'root':
		os.setuid(1000)
        print('yes')
    else:
        print('no')

        #need to became n3yron user
    proc = subprocess.Popen(['kubectl', 'get', 'pods'], stdout=subprocess.PIPE)
    output = proc.stdout.readlines()
    for line in output:
        if "nginx" in line:
            nginx_pod_re = re.findall(r'nginx-\w+-\w+', line)

    nginx_pod = ''.join(nginx_pod_re).strip()
    print("Your Nginx pod id is: "+nginx_pod)

    os.system('kubectl exec '+nginx_pod+' -- certbot --nginx -d aws.n3yron.ru --force-renewal -n')
    print(os.system('kubectl exec {} -- nginx -s reload'.format(nginx_pod)))

my_function()


#        print("Renew certs for hosts")
#        proc1 = subprocess.Popen(['docker', 'exec', '-d', nginx_container, 'certbot', '--nginx', '-d', 'aws.n3yron.ru', '-d', 'petclinic.n3yron.ru', '--force-renewal', '-n'], stdout=subprocess.PIPE)
#        output1 = proc1.stdout.readlines()
#        for line in output1:
#       	    print(line)
 #           print(output1)

#        print("Reloading Nginx")
#        print(os.system('docker exec -d {} nginx -s reload'.format(nginx_container)))
#    except:
#    	print("Something go wrong.")



#find nginx pod
#exec in nginx pod