#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:14:51 2020

@author: saurabhsagar
"""

#here we will focus on file manipulation and working with dates and times
# also we will learn to run python program as a process in background

# The Domain Name System and its associated cache is your Mac's standard way of knowing how to 
# get to where it's going on the Internet, but there's another file that can be very useful.
# It's called the Hosts file,and it can be used to override the default DNS information

import time
from datetime import datetime as dt

host_temp_path = "hosts.txt"
host_path = "/private/etc/hosts"
redirect = "127.0.0.1"  #this is the ip address redirected when we try to access restricted website
website_list = ["www.youtube.com","youtube.com","www.primevideo.com","primevideo.com"] #this are the websites we want to block

while True:
    
    #by this if condition we are checking for time between 8 AM and 4PM on any given day
         #-----year-----,----month-----,-----day----,hrs)
    if dt(dt.now().year,dt.now().month,dt.now().day, 12) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 21):
        
        print("working hours")
        # r+ mode means we can write and append in our file
        with open(host_path,'r+') as file: # we are accessign temporary host file s
            content = file.read()
            
            for website in website_list: #taking each website we have given in website list
                if website in content:  #cheching the same website in content of hosts file and if its already present 
                    # then we pass and check for next element in the website lists
                    pass 
                else:
                    file.write(redirect+" "+ website +"\n")
    else:
       print("free time")
       with open(host_path,'r+') as file:
            content = file.readlines() #this will give the pointer at the end of the last line
            file.seek(0) #with this the read/write pointer will at the begging of the file and whatever... 
                         # we write will be written from there itself 
                        
            #we will compare all the files of content against the website
            for line in content:
                #if we found a line which does'nt contain any website from website list, we append it hour hosts line
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate() # this will delete everything written after writing the first block containing line without webstites from the website_lists
                    
    time.sleep(5) # every time this line is executed , THis process sleep for 5 seconds


# Now we have to run this python file as background process so we will use Crontab .e on terminal
# so if we write crontab .e then it will exeute the files which can be modified by the normal users in the background process
# but if we type sude crontab .e than we can execute files that can be modified by the super users in the background process
    # then after opening the crontab we write - @reboot python3 location_of_file with filename so this will execute the 
    #file in the backgroung process , @reboot tell computer to run this script when computer starts
        