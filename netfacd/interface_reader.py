#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())
for i in netiface.interfaces():    
    print('\n*********Details of interface - ' + i + ' *********')
    try:
        print('MAC: ', end=''0
        print((netifaces.ifaddresses(I)[netifaces.AF_LINK)[0]['addr']
        print('IP: ', and='')
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
    except:
        print('Could not collect adapter information')

        



