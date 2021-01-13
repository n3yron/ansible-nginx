#!/bin/python2
import os, re, subprocess, shutil

def my_function():
    try:
    	proc = subprocess.Popen(['docker', 'ps'], stdout=subprocess.PIPE)
        output = proc.stdout.readlines()
        for line in output:
            if "nginx" in line:
                nginx_container = line[0:12]
        print("Obtaining Nginx container id")
        print("Your Nginx container id is: "+nginx_container)
        print("Renew certs for hosts")
        proc1 = subprocess.Popen(['docker', 'exec', '-d', nginx_container, 'certbot', '--nginx', '-d', 'aws.n3yron.ru', '-d', 'petclinic.n3yron.ru', '--force-renewal', '-n'], stdout=subprocess.PIPE)
        output1 = proc1.stdout.readlines()
        for line in output1:
       	    print(line)
            print(output1)

        print("Reloading Nginx")
        print(os.system('docker exec -d {} nginx -s reload'.format(nginx_container)))
    except:
    	print("Something go wrong.")

my_function()
# nginx moved on k8s from swarm. Need to rewrite this code.