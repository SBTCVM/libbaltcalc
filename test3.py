#!/usr/bin/env python
import libbaltcalc
from libbaltcalc import btint 

import time
int1=btint(3)
int2=btint(2)
print(int1.bt())
print(int2.bt())
#print int1
while int(int1)<1000000:
	print(int1)
	print(int(int1))
	int1=(int1 * int2)
print(int1)
print(int(int1))