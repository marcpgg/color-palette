# Color-Clustering

Python script to find most dominant colors in any image, using k-means clustering.

Examples:

![Florida](/images/florida.jpeg)
![Palette Florida](/images/Figure_florida.png)

!['Her'](/images/her2.jpg)
!['Palette Her'](/images/Figure_her2.png)




The script basically clusters the pixel intensities of an RGB image. Given an image with _MxN_ pixels, each consisting of three components: Red, Green, and Blue respectively. Pixels that belong to a given cluster will be more similar in color than pixels belonging to a separate cluster.



## Requirements
* Python 3
* OpenCV
* matplotlib
* sklearn
