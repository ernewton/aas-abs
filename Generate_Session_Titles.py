import os
from os import path
from itertools import izip
import shutil
from multiprocessing import Pool
from math import pi
import math
import csv
import operator
import pickle
import time

import numpy as np
from scipy.optimize import leastsq

#import pyfits
#from pywcs import WCS
#from ephem import Equatorial, Ecliptic

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plot

import urllib2



def make_lists_like_a_boss():
    #base_command = 'http://www1.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/meetingsvc/meetings?year='
    base_command_1 = 'http://aas.org/archives/BAAS/v'
    base_command_2 = '/SessionList.html'
    base_command_3 = '/SL.htm'
    

    for aas_num in range(182,193):
        print "On AAS meeting: "+str(aas_num)
        print "Finding the session lists and the right files................like a boss \n"
        for num1 in range(25,40):
            
            for num2 in range(0,10):
                website = base_command_1+str(num1)+'n'+str(num2)+'/aas'+str(aas_num)+'/SessionList.html'
                try:
                    urllib2.urlopen(website)
                    print "Found website, stealing data..........like a boss \n"
                    command = 'curl -O AAS'+str(aas_num)+'.txt '+website+' >  AAS'+str(aas_num)+'.txt'
                    os.system(command)

                except urllib2.HTTPError:
                    dummyvar=0



    for aas_num in range(193,223):
        print "On AAS meeting: "+str(aas_num)
        print "Finding the session lists and the right files................like a boss \n"
        for num1 in range(25,40):
            
            for num2 in range(0,10):
                website = base_command_1+str(num1)+'n'+str(num2)+'/aas'+str(aas_num)+'/SL.htm'
                try:
                    urllib2.urlopen(website)
                    print "Found website, stealing data..........like a boss \n"
                    command = 'curl -O AAS'+str(aas_num)+'.txt '+website+' >  AAS'+str(aas_num)+'.txt'
                    os.system(command)

                except urllib2.HTTPError:
                    dummyvar=0




def main():
    dummy_variable = make_lists_like_a_boss()

    










if __name__ == '__main__':
    main()
