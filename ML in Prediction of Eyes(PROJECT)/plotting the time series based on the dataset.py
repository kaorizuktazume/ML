# load the dataset
import pyplot as plt
data = read_csv('brain activity.txt', header=None)
# retrieve data as numpy array
values = data.values
# create a subplot for each time series
plt.figure()
for i in range(values.shape[1]):
	plt.subplot(values.shape[1], 1, i+1)
	plt.plot(values[:, i])
plt.show()
