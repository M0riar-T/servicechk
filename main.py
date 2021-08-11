# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import chk_service as cs

import sendanemail as mail
import chk_service_with_email as cse

# cs.chk_service('sshd','123.log','service sshd status')
out = cse.chk_service('freeswitch','456.log','/usr/local/freeswitch/bin/freeswitch -nc -core')
print(out)
# sentmail = mail.sendanemail("dark.pearl007@gmail.com","The service status was", "/home/jenish/PycharmProjects/my_modules/456.log")