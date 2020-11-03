#!/usr/local/bin/python

# Complete Kubernetes network automationscript
# Goal: Make it as easy as possible to set up a fully working Kubernetes cluster
# Kubeauto 0.0.1 // Adrian Beck | github.com/adrianbeckdev
# Doesn't work at the moment  but maybe some day!
# Designed for Ubuntu Server 20.04 LTS
# Making use of Vagrant and weaveworks

import ansible
import socket
import proxy
import os


# Set Variables

PROXY=""
PORT=""
POD_IP_RANGE = ""
MASTER_COUNT = ""
WORKER_COUNT = ""
MASTER_IP= ""
WORKER_IPS =""
MASTER_PLAYBOOK = open("master.yaml",r+)
WORKER_PLAYBOOK = open("worker.yaml",r+)


class main:
    print("Changing Proxy configs needed")

    def __init__(self):
        self.proxy = PROXY
        self.port = PORT
        self.pod_range = POD_IP_RANGE
        self.master_count = MASTER_COUNT
        self.worker_count = WORKER_COUNT
        self.master_ip = MASTER_IP
        self.worker_ips = WORKER_IPS


    def change_proxy_config(self):

        #Reading in Proxysetting from different files

        try:
            system_conf = open("/etc/evironment/proxy.conf",r+)
            docker_conf = open("~/.docker/config.json",r+)


        except:
            print("Did not found config files")
            

        #Change Docker

        docker_conf.write("{
 "proxies":
 {
   "default":
   {
     "httpProxy": +"https://" + "PROXY" + ' ' + "PORT" + '' ,
     "httpsProxy": + "http://" , + "PROXY" + ':' + "PORT" + '' 
     
   }
 }
}  "


    #Adding system Proxy 

    sytem_conf.write("
{ "httpProxy": +"https://" + "PROXY" + ' ' + "PORT" + '' ,
     "httpsProxy": + "http://" , + "PROXY" + ':' + "PORT" + ''} ")   
                                                                


        
    def change_firewall(self):
            
            system.os("swapoff -a")
            





class Master:
    

    start




class Worker:


