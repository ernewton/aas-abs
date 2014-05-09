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
import pickle
import urllib2



def parse_AAS_like_a_boss():
    AAS_num = []
    AAS_session_num = []
    AAS_session_title = []
    
    for i in range(182,208):
        file1 = open('AAS'+str(i)+'.txt','r')
        #Different files have different formats because fuck everything

        #Case 1
        if i < 187:
            #For these files, the format is:
            #...... >Session #</A>: <B>SESSION TITLE</B>
            session_num_to_find = 1
            found = False
            for line in file1:
                garbage,phrase_to_find,after = line.partition('>Session '+str(session_num_to_find)+'</A>: <B>')
                if after != '':
                    the_name,parser,blank = after.partition('</B>')
                    AAS_num.append(str(i))
                    AAS_session_num.append(str(session_num_to_find))
                    AAS_session_title.append(the_name)
                    session_num_to_find = session_num_to_find+1

        #Case 2
        if i > 186 and i < 193:
            #For these files, the format is:
            #Sess###>SESSION TITLE</A><DD>
            session_num_to_find = 1
            for line in file1:
                if session_num_to_find < 10:
                    garbage,phrase_to_find,after = line.partition('Sess00'+str(session_num_to_find)+'>')
                    if after !='':
                        the_name,parser,blank = after.partition('</A><DD>')
                        AAS_num.append(str(i))
                        AAS_session_num.append(str(session_num_to_find))
                        AAS_session_title.append(the_name)
                        session_num_to_find = session_num_to_find+1

                if session_num_to_find > 9 and session_num_to_find < 100:
                    garbage,phrase_to_find,after = line.partition('Sess0'+str(session_num_to_find)+'>')
                    if after !='':
                        the_name,parser,blank = after.partition('</A><DD>')
                        AAS_num.append(str(i))
                        AAS_session_num.append(str(session_num_to_find))
                        AAS_session_title.append(the_name)
                        session_num_to_find = session_num_to_find+1
                 
                if session_num_to_find > 100:
                    garbage,phrase_to_find,after = line.partition('Sess'+str(session_num_to_find)+'>')
                    if after !='':
                        the_name,parser,blank = after.partition('</A><DD>')
                        AAS_num.append(str(i))
                        AAS_session_num.append(str(session_num_to_find))
                        AAS_session_title.append(the_name)
                        session_num_to_find = session_num_to_find+1

        #Case 3
        if i > 193:
            #For these files, the format is:
            #.... Session #. ..... S#0.htm">Session Title</A>
            session_num_to_find = 1
            for line in file1:
                garbage,phrase_to_find,after = line.partition('S'+str(session_num_to_find)+'0.htm">')
                if after != '':
                    the_name,parser,blank = after.partition('</A>')
                    AAS_num.append(str(i))
                    AAS_session_num.append(str(session_num_to_find))
                    AAS_session_title.append(the_name)
                    session_num_to_find = session_num_to_find+1
                                        

    pickle.dump([AAS_num,AAS_session_num,AAS_session_title], open("AAS_Lists.pickle","wb"))


    return(0)




def main():
    dummy_variable = parse_AAS_like_a_boss()

    










if __name__ == '__main__':
    main()
