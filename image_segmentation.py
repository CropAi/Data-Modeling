import numpy as np 
import pandas as pd
import cv2 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class ImageSegmentation():
	def __init__(self, img_path):
		self.img = plt.imread(img_path)

	def fit(self):

		img_ = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
		x = img_.reshape((-1, 3))

		km = KMeans(n_clusters=20)
		km.fit(x)
		center = km.cluster_centers_
		labels = km.labels_

		colors = []
		for color in center:
			colors.append(color)

		new_img = np.zeros(x.shape)
		for i in range(x.shape[0]):
			new_img[i] = colors[labels[i]]
		new_img = new_img.reshape(img_.shape)
		new_img /= 255

		return new_img

