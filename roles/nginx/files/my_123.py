#!/bin/python2
import os, re, subprocess, shutil

#proc = subprocess.Popen(['docker', 'ps'], stdout=subprocess.PIPE)
#output = proc.stdout.readlines()
#for line in output:
#    if "nginx" in line:
#        print(line[0:12])
 #       nginx_container = line[0:12]

#print(nginx_container)

print(os.system('docker exec -d {} nginx -s reload'.format(nginx_container)))