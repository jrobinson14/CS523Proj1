This project uses Python 3.8 and was tested on Windows 10 and MacOS mojave machines. Use of any other versions of python seems to cause problems with matplotlib and graphing. There seem to be some problems running Matplotlib and Pylab on the CS Linux machines. Some graphs do not appear, this seems to be an issue on at least some versions of Ubuntu Linux. Some resources on the issue: 

https://stackoverflow.com/questions/7534453/matplotlib-does-not-show-my-drawings-although-i-call-pyplot-show

https://www.pyimagesearch.com/2015/08/24/resolved-matplotlib-figures-not-showing-up-or-displaying/

# TimeSeries.py

Creates a time series of logisitc map. Can be manipulated for different values of r to see attractors -> chaos

Currently creates two figures. Figure 1 shows two periodic time series with differing initial conditions and the same r value of 2.9. You can see that they eventually converge on the same value. Figure 2 shows 2 chaotic series that start with the same behavior but eventually diverge. 

To run the file, navigate to the folder containing "TimeSeries.py" and use the python command (python TimeSeries.py). This should bring up the graphs seen in Figures 1 and 2 in the paper. 

R values and intial conditions are currently hard coded so no input is needed.


# Data Files

Data generated on periodic and chaotic time series is stored in two files: dataChaotic.txt and dataNonChaotic.txt. These files are created in the local directory when TimeSeries.py is run. 

Data files for part 3 are located in directories named correspinding to each epsilon value. 


# Walker2.0

Implementation of equation used as model in Walker paper to get fig 4 and 5. Graphs return map for all values used in Walker paper. To run: python Walker2.0.py

# WalkerFig4

Used to generate data for part 4. Uses 1,000 populations over 1,000 time steps, randomly sampling 3 populations and comparing them to the Mn value for that time step. Writes reults to file in specified directory in local directory. 


