#!/usr/bin/python
from decimal import Decimal
from math import log

def binom(n, m):
    b = [0] * (n + 1)
    b[0] = 1
    for i in xrange(1, n + 1):
        b[i] = 1
        j = i - 1
        while j > 0:
            b[j] += b[j - 1]
            j -= 1
    return b[m]

#Totoal number of masternodes
mns=5000
#Quarum size used for ChainLocks
qsz=400
#Number of nodes in a LLMQ needed for a CHainLock
qmaj=240

print "Assume ", mns," masternodes in total"

print "The number of masternodes in a quourm:  ", qsz

numb = binom(mns,qsz)
print "Total number of LLMQs:" 

print numb

#Number of attacking nodes
y = 500

print "Assume ", y, " of MNs are Byzintine"

temp = 0

for x in range(qmaj,qsz+1):
    print "Number of LLMQs with ", x," Byzinetine nodes:"
    temp = temp + binom(y,x)*binom(mns-y,qsz -x)
    print binom(y,x)*binom(mns-y,qsz-x)
    #line below was in here for trouble shooting
    #print temp


print "Total number of Byzinetine Quorums" 
print temp

print "Log base 10 of above:"

print log(temp,10)

print "Total number of LLMQs"
print numb

print "Log base 10 of above:"

print log(numb,10)

print "Probabilty of malious ChainLock" 

print 10 ** (log(temp,10)-log(numb,10))

