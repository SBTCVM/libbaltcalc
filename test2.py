#!/usr/bin/env python
import libbaltcalc
from libbaltcalc import btint 
int1=btint(libbaltcalc.mni(4))
int2=btint("+")
while int(int1) != libbaltcalc.mpi(4):
	print(int1)
	print(int(int1))
	int1=(int1 + int2)
print(int1)
print(int(int1))
