from PIL import Image
import numpy as np 
def grayscale(path):
	img=Image.open(path)
	arr=np.array(img)
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			sum=0
			for k in range(len(arr[i][j])):
				sum+=arr[i][j][k]
			sum=sum//4
			for k in range(len(arr[i][j])):
				arr[i][j][k]=sum
	return Image.fromarray(arr)
