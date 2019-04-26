# Color-Clustering

Finding most dominant colors in an image
 
Applying Kmeans clustering to each pixel color intensities of an RGB image.  
Pixels that belong to a given cluster will be closer to the cluster's 0-255 RGB values, thus will be similar in color. Pixels belonging to each cluster are quantified and plotted in a horizontal stacked histogram.


If notebook does not render on github, use this [NBviewer link](https://nbviewer.jupyter.org/github/marcpgg/color-palette/blob/master/colorPalette.ipynb).


#### Example:


![Palette Florida](/images/example-palette.png)



## Requirements
* Python 3
* OpenCV
* Matplotlib
* scikit-learn
