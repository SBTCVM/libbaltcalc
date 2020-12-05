#!/usr/bin/env python
import libbal27 as b27
import libbaltcalc as btcalc
from libbaltcalc import btint


def conversion_tests(intval):
	intval=int(intval)
	print("Decimal: " + str(intval))
	print("Balanced Ternary: " + btcalc.DECTOBT(intval))
	print("balanced Heptavigesimal/Septemvigesimal (balanced base 27): " + b27.inttob27(intval))
	print("convert to base 27 and back:" + str(b27.b27toint(b27.inttob27(intval))))
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
conversion_tests(13)
conversion_tests(-13)