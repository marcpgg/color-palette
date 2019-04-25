# Color-Clustering

Notebook to find most dominant colors in any image, using k-means clustering.
If notebook does not render on github, use this [NBviewer link](https://nbviewer.jupyter.org/github/marcpgg/color-palette/blob/master/colorPalette.ipynb).

Examples:

![Florida](/images/florida.jpeg)
![Palette Florida](/images/Figure_florida.png)

!['Her'](/images/her2.jpg)
!['Palette Her'](/images/Figure_her2.png)



Applying Kmeans clustering to each pixel intensities of an RGB image.  
Pixels that belong to a given cluster will be closer to their 0-255 RGB value, thus will be similar in color.



## Requirements
* Python 3
* OpenCV
* Matplotlib
* scikit-learn
