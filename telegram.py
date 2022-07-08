# This module will return 0 if the service was not running and it will be started
# if the service was already running it will return any non zero value
# this will also create / or log in the existing log files with the returned output of the cmd
# RUN THIS AS A ROOT NO OTHER USER CAN RUN AND WRITE LOGS FOR THIS SCRIPT


import os
import logging
import subprocess
from logging.handlers import RotatingFileHandler
import traceback
import smtplib
from logging.handlers import TimedRotatingFileHandler
import re        
import telegram_send



def chk_service(cmd,logfile):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler(logfile,  when='midnight', backupCount=8)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    check = '/usr/local/freeswitch/bin/fs_cli -x "{}" '.format(cmd)
    output = str(os.popen(check).read())
    count = re.findall('\d+', output.split()[0])
    ccount = int(count[0])
    print ('calls:', ccount)



    if ccount == 0:
        print("Calls are {}".format(ccount))
        telegram_send.send(messages=["CRITICAL!! Calls are 0!!"])


    elif count < 101:
        print("Calls are {}".format(ccount))
        telegram_send.send(messages=["WARNING!! Calls are less than 100!!"])

    logger.debug('{}'.format(output))

    return output



out = chk_service('show channels count','/home/jenish/fs_call_count.log')
print(out)