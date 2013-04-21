GnuplotInterface.py
===================

OVERVIEW
--------
GnuplotInterface.py is a simplest gnuplot controller for Python.

HOW TO USE
----------
    import GnuplotInterface  
    gnuplot = GnuplotInterface.GnuplotInterface()  
    gnuplot.write("a = 3.14")  
    gnuplot.write("plot a*x")  
    gnuplot.write("print a")  
    print gnuplot.read()  
    gi.close_window()  

If you want to use "fit" command, please use it as follows:

    gnuplot.write("set fit errorvariables")  
    gnuplot.write("fit a*x "data.dat" via a")  
    gnuplot.write("print a,a_err")  
    print gnuplot.read()  

DOCUMENTS
---------
Now prepearing. Please see the script itself.

LICENCE
-------
This program is free software; you can redistribute and/or modify it.

AUTHOR
------
Tatsuya Soma: s0-ma
