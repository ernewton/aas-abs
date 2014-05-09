# ==================================================================================================
# FindKeywordsInSessions
# ----------------------
#
# Parse a 'pickle' file containing arrays of AAS Number, AAS Session Number, AAS Session Title
# Convert AAS Number to years, and count the number of keyword occurrences per year, in session titles
#
# ------------------
# Luke Zoltan Kelley
# LKelley@cfa.harvard.edu
# ==================================================================================================

import os
import shutil
import pickle

import numpy as np

import matplotlib
import matplotlib.pyplot as plt

# Hardcode keywords for now, each session title is searched for each
keywords = [ "supernova" , "dark matter" , "planet" , "dark energy" , "star", "galax"]




def loadPickle(fname="AAS_Lists.pickle"):
    '''
    Load the Pickle of AAS Data.  Must be 3 arrays:
    AAS Number, AAS Session Number, Session Title

    returns dictionary with keys 'num', 'snum', 'title'
    '''

    dat = pickle.load( open(fname, 'r') )
    return { "num":dat[0] , "snum":dat[1] , "title":dat[2] }



def aasNumToYear(num):
    '''
    Convert from AAS Number to year.

    returns years float
    '''
    return 1993.0 + (np.float(num)-182.0)/2.0


def counter(indat, regex):
    '''
    Count the number of occurrences of 'regex' in the given AAS data (from a pickle)

    Returns years and counts per year
    '''

    outcount = []; outyears = []; outnorms = []
    # Extract arrays from data
    n = indat['num']
    s = indat['snum']
    t = indat['title']

    # Convert AAS Numbers to years
    years = [ aasNumToYear(num) for num in n ]
    lastyear = None #years[0]
    count = 0.0
    norm  = 0

    # Iteratire through all entries
    for it in range(len(years)):
        thisyear  = years[it]
        thistitle = t[it]

        # If this is a new year, start new entry
        if( thisyear != lastyear ):
            outcount.append(0)
            outyears.append(thisyear)
            outnorms.append(0)
            lastyear = thisyear


        temp = thistitle.upper().count( regex.upper() )
        if( temp > 0 ): outcount[-1] += 1                                                           # Count titles matching
        outnorms[-1] += 1                                                                           # Count total number of sessions


    return outyears, outcount, outnorms




def main():

    aas = loadPickle()
    nums = len(aas)

    years = []; counts = []; norms = []
    # Iterate through each keyword and count matches
    for it in range(len(keywords)):
        yrs, cnts, nms = counter(aas, keywords[it])
        years.append(yrs)
        counts.append(cnts)
        norms.append(nms)


    numkeys = len(keywords)    
    plt.clf()
    # For each keyword, report results, and plot
    for ii in range(numkeys):
        print " - Keyword = '%s' " % (keywords[ii])
        for jj in range(len(years[ii])):
            print " - - %f %d" % (years[ii][jj], counts[ii][jj])

        plt.plot(years[ii], counts[ii], label=keywords[ii])


    # Pretty plot
    plt.legend(loc='upper left')
    ax = plt.gca(); ax.grid()
    ax.set_xlabel('Year'); ax.set_ylabel('Count')
    plt.savefig('aas-trend.png')                                                                    # Save plot
    

if __name__ == '__main__':
    main()
