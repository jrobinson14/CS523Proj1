This project uses Python 3.8 and was tested on Windows 10 and MacOS mojave machines. Use of any other versions of python seems to cause problems with matplotlib and graphing. There seem to be some problems running Matplotlib and Pylab on the CS Linux machines. Some graphs do not appear. 

# TimeSeries.py

Creates a time series of logisitc map. Can be manipulated for different values of r to see attractors -> chaos

Currently creates two figures. Figure 1 shows two periodic time series with differing initial conditions and the same r value of 2.9. You can see that they eventually converge on the same value. Figure 2 shows 2 chaotic series that start with the same behavior but eventually diverge. 

To run the file, navigate to the folder containing "TimeSeries.py" and use the python command (python TimeSeries.py). This should bring up the graphs seen in Figures 1 and 2 in the paper. 

R values and intial conditions are currently hard coded so no input is needed.


# Data Files

data generated is stored in two files: dataChaotic.txt and dataNonChaotic.txt

# Walker2.0

Implementation of equation used as model in Walker paper to get fig 4 and 5. Graphs return map for all values used in Walker paper. To run: python Walker2.0.py
