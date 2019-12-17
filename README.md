# SWI-TS-reader

Authors: Christoph Paulik, Bernhard Bauer-Marschallinger

Sample code for reading in a specific Discrete Global Grid cell of the 
Soil Water Index Time Series (SWI-TS) product and plotting values for a specific grid point.

The first step is finding the location id of the grid point (GP) you are interested in. 
Assuming you know the latitude and longitude of the GP you want to read you can use the DGG grid point locator
hosted at 
http://rs.geo.tuwien.ac.at/dv/dgg/ 
to find and export all location id’s of a country or region.
Note that location id’s are called Point ID’s in the viewer. 
The DGG grid is called Copernicus SWI TS in the web application. 

After you have found the id and the cell number of the GP you are interested in, 
this code sample opens and reads the corresponding SWI-TS cell file, then extracts
the SWI values for T=20 and plots the time series.

For more sample code on reading in the SWI products from Copernicus Global Land Service, 
please see TU-Wien's GitHub repository ascat at
https://github.com/TUW-GEO/ascat/
