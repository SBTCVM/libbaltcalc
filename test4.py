#!/usr/bin/env python
import libbaltcalc
from libbaltcalc import btint 

import time
int1=btint(30)
print "string-based, zero padding/right-to-left truncation."
print int1.bttrunk(7)
print int1.bttrunk(6)
print int1.bttrunk(5)
print int1.bttrunk(4)
print int1.bttrunk(3)
print int1.bttrunk(2)
print int1.bttrunk(1)
print int1
print "decimal, (mpi/mni based truncation)"
print int1.dectrunk(5)
print int1.dectrunk(4)
print int1.dectrunk(3)
print int1.dectrunk(2)
print "test copy and changeval"
#note: copy will create a new btint class object from the internal value, so
#changes in the copy will not affect the first btint object.
int2=int1.copy()
print int1
print int2
print "change copy to 3"
print int2
#note: changeval can accept the same inputs as new btint objects, but changes
#the internal value, so any part of a program that has a pointer to that btint
#will be affected by the change.
int2.changeval("+0")
print int2
int3=btint(3)
int2.changeval(int3)
print int2
int2.changeval(3)
print int2
print "result:"
print int2
print int1

#simple comparison operators.
print "compare (-3, +3)"
int5=btint(-3)
int6=btint(3)
print int5==int6
print int5!=int6
print int5>int6
print int5<int6
print int5<=int6
print int5>=int6

#

print int5
print ~int5
print +int5
print -int5
#len returns the length of the integer in trits.
print len(int5)
