# This module will return 0 if the service was not running and it will be started
# if the service was already running it will return any non zero value
# this will also create / or log in the existing log files with the returned output of the cmd
# RUN THIS AS A ROOT NO OTHER USER CAN RUN AND WRITE LOGS FOR THIS SCRIPT

import os
import logging
import subprocess
from logging.handlers import RotatingFileHandler
import traceback
import sendanemail as mail

def chk_service(service,logfile,run_cmd,emailid):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(logfile, maxBytes=20000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    check = 'ps aux | grep {} | grep -v grep | wc -l'.format(service)
    output = int(os.popen(check).read())

    if output == 0:
        cmd = subprocess.run([run_cmd], shell=True, capture_output=True, text=True)
        logger.debug('{} is NOT running, Starting it now :: \n%s :: \n%s\n :: Detailed Exception - %s'.format(service),cmd.stdout, cmd.stderr,traceback.format_exc())
        sentmail = mail.sendanemail(emailid, "The {} status was : {}".format(service, output),logfile)

    return output
