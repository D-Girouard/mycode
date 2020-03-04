#!/usr/bin/env python3
  
loginsuccess = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    for line in kfile:
        if "v3/auth/tokens" in line:
            loginsuccess += 1

print("The number of successful log ins is", loginsuccess)


