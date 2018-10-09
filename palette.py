from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2


#CLI Parser

#ap =argparse.ArgumentParser()
#ap.add_argument('-i', '--image', required= True, help = 'Path to image')
#ap.add_argument('-c', '--clusters', required=True, type=int, help= 'Number of clusters')
#args = vars(ap.parse_args())

path = '../palette/images/her2.jpg'
n_clusters = int(input('Select number of clusters:  '))

#load images
img = cv2.imread(path)
#img = cv2.imread(args['image'])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.axis('off')
plt.imshow(img)

# reshape the image to be a list of pixels
img = img.reshape((img.shape[0] * img.shape[1], 3))


#cluster K means
#clt = KMeans(n_clusters = args['clusters'])

clt = KMeans(n_clusters = n_clusters)

clt.fit(img)


# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)


#display image

plt.figure()
plt.axis('off')
plt.imshow(bar)
plt.show()
plt.savefig('../palette/images/palette.png', format='png')
