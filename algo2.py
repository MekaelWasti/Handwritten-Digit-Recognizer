import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans


digits = datasets.load_digits()



# print(digits.data)
print(f'Shape of data sample {digits.data[0].shape}')
# plt.gray()
# plt.matshow(digits.images[100])
# plt.show()


# print(digits.data[100])
print(f'Data Sample: {digits.data[100]}\n')


# print(digits.target[100])

k = 10
model = KMeans(n_clusters=k,random_state=42)
model.fit(digits.data)


# fig = plt.figure(figsize=(8,3))
# fig.suptitle("Visualize",fontsize=14,fontweight='bold')

# for i in range(10):

#   ax = fig.add_subplot(2,5,1+i)

#   ax.imshow(model.cluster_centers_[i].reshape((8,8)),cmap=plt.cm.binary)

# plt.show()

new_samples = np.array([
[0.00,0.00,0.13,0.23,0.42,0.42,0.02,0.00,0.00,0.50,2.19,2.19,2.19,2.19,0.62,0.00,0.00,0.00,0.40,0.27,0.15,2.13,0.54,0.00,0.00,0.00,0.00,0.00,0.40,2.19,0.15,0.00,0.00,0.00,0.00,0.00,0.70,2.01,0.00,0.00,0.00,0.00,0.00,0.00,1.01,1.73,0.00,0.00,0.00,0.00,0.00,0.00,1.32,1.47,0.00,0.00,0.00,0.00,0.00,0.00,0.90,0.62,0.00,0.00],
[0.00,0.00,0.00,0.27,0.31,0.00,0.00,0.00,0.00,0.27,1.51,2.17,1.67,0.00,0.00,0.00,0.00,1.87,1.98,1.50,1.86,0.00,0.00,0.00,0.00,1.12,0.24,0.69,2.13,0.00,0.00,0.00,0.00,0.00,0.00,0.36,2.19,0.24,0.00,0.00,0.00,0.00,0.00,0.16,2.19,0.60,0.00,0.00,0.00,0.00,0.00,0.00,2.19,0.66,0.00,0.00,0.00,0.00,0.00,0.00,2.15,0.47,0.00,0.00],
[0.00,0.00,0.00,0.27,0.09,0.00,0.00,0.00,0.00,0.00,1.04,2.14,1.74,0.09,0.00,0.00,0.00,0.47,2.19,1.17,2.19,0.36,0.00,0.00,0.00,0.11,1.82,2.08,1.89,0.02,0.00,0.00,0.00,0.00,1.52,2.17,2.09,0.46,0.00,0.00,0.00,0.18,2.19,0.99,2.17,0.60,0.00,0.00,0.00,0.00,1.95,2.19,1.19,0.00,0.00,0.00,0.00,0.00,0.53,0.62,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.22,1.30,1.62,0.97,0.00,0.00,0.00,0.00,1.45,1.80,1.21,2.19,0.23,0.00,0.00,0.00,1.34,1.52,0.42,2.19,0.42,0.00,0.00,0.00,0.55,2.17,2.13,2.19,0.22,0.00,0.00,0.00,0.00,0.47,0.76,2.19,0.22,0.00,0.00,0.00,0.00,0.00,0.22,2.19,0.22,0.00,0.00,0.00,0.00,0.00,0.14,2.02,0.14,0.00,0.00]
])

# print(f'Length of test sample {len(new_samples)}')
print(f'Shape of test sample {new_samples.shape}')


test = 3

# prediction = model.predict(new_samples)
# predic = digits.data[100].reshape(-1,1)
predic = digits.data[test]
expected = digits.target[test]
print(f'Shape of my sample {predic.shape}')
print(f'My Image\'s Array{predic}')

predic = np.array([ 0.,  0.,  0.,  2., 13.,  0.,  0.,  0.,  0.,  0.,  0.,  8., 15.,  0.,  0.,  0.,  0.,  0.,
  5.00, 16.00,  5.00,  2.00,  0.00,  0.00,  0.00,  0.00, 15.00, 12.00,  1.00, 16.00,  4.00,  0.00,  0.00,  4.00, 16.00,  2.00,
  9.00, 16.00,  8.00,  0.00,  0.00,  0.00, 10.00, 14.00, 16.00, 16.00,  4.00,  0.00,  0.00,  0.00,  0.00,  0.00, 13.00,  8.00,
  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, 13.00,  6.00,  0.00,  0.00])




predic = digits.data[test]


predic = digits.data[test]
print(f'MY DRAWN IMAGE {predic}')
print(f'MY DRAWN Shape {predic.shape}')
print(f'Other Shape {predic.shape}')

# prediction = model.predict(new_samples)
prediction = model.predict(predic.reshape(-1,1))
# prediction = model.predict(predic.reshape(-1,1))
print(f'My Image\'s Array{predic.reshape(-1,1)}')
# prediction = model.predict(digits.data[100].reshape(-1,1))
print(f'Prediction Result (CLUSTERS): {prediction}')
# print(f'Expected Result: {expected}')


# print(f'My Sample length{len(predic)}')
# print(f'My Sample shape{predic.shape}')
# print(digits.data[100].shape)
print()
for i in range(len(prediction)):
  if prediction[i] == 0:
    print(f"PREDICTION - REAL: 3", end='')
  elif prediction[i] == 1:
    print(f"PREDICTION - REAL: 0", end='')
  elif prediction[i] == 2:
    print(f"PREDICTION - REAL: 8", end='')
  elif prediction[i] == 3:
    print(f"PREDICTION - REAL: 1", end='')
  elif prediction[i] == 4:
    print(f"PREDICTION - REAL: 9", end='')
  elif prediction[i] == 5:
    print(f"PREDICTION - REAL: 2", end='')
  elif prediction[i] == 6:
    print(f"PREDICTION - REAL: 4", end='')
  elif prediction[i] == 7:
    print(f"PREDICTION - REAL: 7", end='')
  elif prediction[i] == 8:
    print(f"PREDICTION - REAL: 6", end='')
  elif prediction[i] == 9:
    print(f"PREDICTION - REAL: 5", end='')

print()

print(f'Expected Result: {expected}')
