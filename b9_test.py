#!/usr/bin/env python
import libbal9 as b9
import libbaltcalc as btcalc
from libbaltcalc import btint


def conversion_tests(intval):
	intval=int(intval)
	print("Decimal: " + str(intval))
	print("Balanced Ternary: " + btcalc.DECTOBT(intval))
	print("Balanced Nonary (balanced base 9): " + b9.inttob9(intval))
	print("convert to Balanced Nonary and back:" + str(b9.b9toint(b9.inttob9(intval))))
	print("------------------")
	return


conversion_tests(1000)
conversion_tests(-1000)
conversion_tests(27)
conversion_tests(-27)
conversion_tests(9841)
conversion_tests(-9841)
conversion_tests(19683)
conversion_tests(-19683)
conversion_tests(4)
conversion_tests(-4)