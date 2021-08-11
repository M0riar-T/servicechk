# This is a sample Python script.


import chk_service as cs
import sendanemail as mail
import chk_service_with_email as cse

cs.chk_service('sshd','ssh_service_check.log','service sshd start')
out = cse.chk_service('freeswitch','/var/log/fs_chk.log','/usr/local/freeswitch/bin/freeswitch -nc -core')
print(out)
sentmail = mail.sendanemail("dark.pearl007@gmail.com","The service status was", "/home/jenish/PycharmProjects/my_modules/456.log")
