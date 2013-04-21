GnuplotInterface.py
===================

OVERVIEW
--------
GnuplotInterface.py is a simple gnuplot controller from python.

HOW TO USE
----------

import GnuplotInterface as gi
gnuplot = gi()
gnuplot.write("a = 3.14")
gnuplot.write("plot a\*x")
gnuplot.write("print a")
print gnuplot.read()
gi.close\_window()

DOCUMENTS
---------
See `docs/`, if you could read Japanese.

LICENCE
-------
This program is free software; you can redistribute and/or modify it.

AUTHOR
------
Tatsuya Soma: s0-ma
