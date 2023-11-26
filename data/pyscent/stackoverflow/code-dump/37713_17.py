#!/bin/python3
import os
import glob
import datetime
import subprocess

def Copy_Logs():
    # Variable Declaration to get the month and Curr_date_month
    Info_month = datetime.datetime.now().strftime("%B")
    Curr_date_month = datetime.datetime.now().strftime("%b_%d_%y") 
    Sourcedir = "/data1/logs"
    Destdir = "/data2/logs/"
    ###### End of your variable section #######################
    # The result of the below glob _is_ a full path
    for filename in glob.glob("{2}/{0}/{1}/*.txt".format(Info_month, Curr_date_month, Sourcedir)):
        if os.path.getsize(filename) > 0:
            if not os.path.exists(Destdir + os.path.basename(filename)):
                subprocess.call(['rsync', '-avz', '--min-size=1', filename, Destdir ])

if __name__ == '__main__':
    Copy_Logs()
