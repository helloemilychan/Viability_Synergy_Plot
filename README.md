# Viability Synergy Plot
 Author: Yunkai Zhang

## Features
* Create a 3D plot of cell viability against combinations of two drugs
* Create a contour of cell viability against combinations of two drugs
* Create a contour of Bliss-method predicted contour from viability of two drugs

## Data Input
### Experimental Design
Cells should be treated in a matrix of two drugs (Drug A and Drug B) at concentration gradient
An example of 3\*3 concentration gradient:

Drug A (conc_0) + Drug B (conc_0) | Drug A (conc_1) + Drug B (conc_0) | Drug A (conc_2) + Drug B (conc_0)
Drug A (conc_0) + Drug B (conc_1) | Drug A (conc_1) + Drug B (conc_1) | Drug A (conc_2) + Drug B (conc_1)
Drug A (conc_0) + Drug B (conc_2) | Drug A (conc_1) + Drug B (conc_2) | Drug A (conc_2) + Drug B (conc_2)
### Data Preparation
Viability data from the above matrix

## Data Processing
### 3D Plot
The real viability data will be ploted as scatter.
The predicted viability data will be calculated from the solely viability of Drug A and Drug B using Bliss method
> Effects of combination (%) = Effects of Drug A (%) * (1 - Effects of Drug B (%))
> Viability of combination (%) = 1 - Effects of combination (%)

If Drug A synergises with Drug B, then the scatter point will be below wireframe. They will be connected via *red* lines.
If Drug A antagonizes with Drug B, then the scatter point will above wireframe. *blue* connection.

### 2D Plot
Same method will be used to calcuate 2D contour of 'Synergy Z'.
Comparasion between 'Read Z' and 'Synergy Z' can show synergy or antagonism. 
