#!/usr/bin/env python
import libbaltcalc as btcalc
from libbaltcalc import btint






def test_tritchop(trit_string, splitpoint):
	print("-----------TEST TRITCHOP-------------")
	print("Input      : " + trit_string + " , Split Point: " + str(splitpoint))
	trits=btcalc.tritchop(btcalc.BTTODEC(trit_string), splitpoint)
	print("First Part : " + btcalc.DECTOBT(trits[0]))
	print("Second Part: " + btcalc.DECTOBT(trits[1]))


def test_tritmerge(upperint_string, lowerint_string, lower_length):
	print("-----------TEST TRITMERGE-------------")
	print("Input Upper: " + upperint_string)
	print("Input Lower: " + lowerint_string + " , lower length: " + str(lower_length))
	print("Output: " + btcalc.DECTOBT(btcalc.tritmerge(btcalc.BTTODEC(upperint_string), btcalc.BTTODEC(lowerint_string), lower_length)))
	

test_tritchop("---+++---", 3)
test_tritchop("---+++---", 6)
test_tritchop("---+++---", 9)
test_tritchop("---+++---", 12)

test_tritmerge("++-", "0", 1)
test_tritmerge("---+++---", "+++---+++", 9)


