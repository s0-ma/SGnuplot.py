SGnuplot.py
===================

OVERVIEW
--------
SGnuplot.py is a simplest python interface for gnuplot.

HOW TO USE
----------
    import SGnuplot  
    gnuplot = SGnuplot.SGnuplot()  
    gnuplot.write("a = 3.14")  
    gnuplot.write("plot a*x")  
    gnuplot.write("print a")  
    print gnuplot.read()  
    gnuplot.close_window()  

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
This program is free; you can redistribute and/or modify it.

AUTHOR
------
Tatsuya Soma: s0-ma
