#!/usr/bin/python
#This script was written by Darren Tapp and optimized by thephez

from decimal import Decimal
from math import log
from math import factorial as fac

def binom(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom


###This function takes inputs and outputs the probability
#of sucess in one trial
#pcalc is short for probability calculation
def pcalc(masternodes,quorumsize,attacksuccess,Byznodes):
    SampleSpace = binom(masternodes,quorumsize)
    pctemp=0
    for x in range(attacksuccess, quorumsize+1):
        pctemp = pctemp + binom(Byznodes,x)*binom(masternodes-Byznodes,quorumsize-x)
    #at this junctiure the answer is pctemp/SampleSpace
    #but that will produce an overflow error.  We use logarithims to
    #calculate this value
    return 10 ** (log(pctemp,10)- log(SampleSpace,10))

##We evauate the function pcalc(10,5,3,4)
##print pcalc(10,5,3,4)
##as a test vector
##The answer would be [binom(3,4)*binom(2,6)+(binom(4,4)*binom(1,6)]/binom(10,5)
##[4*15+1*6]/252 = 66/252
##print float(66)/252

##quorum size for ChainLocks
qs = 400
##Number of masternodes
mn = 5000

##Number of Byzintine nodes assuming 5000 nodes
Bft = [500,1000,1500]

##Threshold out of quorum of 400
thresh = 160

for j in range(0,3):
    print "For ", mn, " masternodes with ", Bft[j],"Byzintine the chance of withholding a chainlock in one trial is ", pcalc(mn,qs,thresh,Bft[j])

##Now change the # threshold
thresh = 240

for j in range(0,3):
    print "For ", mn, " masternodes with ", Bft[j],"Byzintine the chance of producing a malicious chainlock is ", pcalc(mn,qs,thresh,Bft[j])


#In the case of a smaller number of masternodes
mn=2000

##Number of Byzintine nodes assuming 2000 nodes
Bft = [240,400,600]

##Threshold out of quorum of 400
thresh = 160

for j in range(0,3):
    print "For ", mn, " masternodes with ", Bft[j],"Byzintine the chance of withholding a chainlock in one trial is ", pcalc(mn,qs,thresh,Bft[j])

##Now change the # threshold
thresh = 240

for j in range(0,3):
    print "For ", mn, " masternodes with ", Bft[j],"Byzintine the chance of producing a malicious chainlock is ", pcalc(mn,qs,thresh,Bft[j])
