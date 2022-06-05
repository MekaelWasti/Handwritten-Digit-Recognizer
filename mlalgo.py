import gzip
from cv2 import imread
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from scipy.misc import *
# from algo2 import *

from skimage import color
from skimage import io


# ML Imports
from sklearn import datasets
from sklearn.cluster import KMeans


def algorithm():

    f = gzip.open("Digit Dataset/t10k-images-idx3-ubyte.gz",'r')

    image_size = 28
    num_images = 1

    f.read(16)
    buf = f.read(image_size * image_size * num_images)
    data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    print(data)
    data = data.reshape(num_images, image_size, image_size, 1)
    # print(data)


    image = np.asarray(data[num_images-1]).squeeze()
    plt.imshow(image)
    plt.gray()
    plt.show()

    print(data)


    # Make Plot Black and White
    plt.matshow(data[100])



    # Read Labels
    f = gzip.open('Digit Dataset/t10k-labels-idx1-ubyte.gz','r')
    f.read(8)
    for i in range(0,50):   
        buf = f.read(1)
        labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
        print(labels)





def kmeans(userInput):
    digits = datasets.load_digits()
    k = 10
    model = KMeans(n_clusters=k,random_state=42)
    model.fit(digits.data)

    print(f'My Image\'s Array{userInput.reshape(1,-1)}')
    print(f'My Array Shape{userInput.shape}')

    # d1,d2,d3 = userInput.shape
    # print("WOAH")
    # print(d1,d2,d3)
    # userInput = userInput.reshape((1,d1*d2))

    # userInput = userInput.flatten().reshape(64,-1)
    # print(f'ARAYYY{userInput}')
    # print(f'SHAPEEEE{userInput.shape}')

    # x_data = np.array(np.array(cv2.imread("1.png")))

    # pixels = x_data.flatten().reshape(64,)
    # print(pixels.shape)


    img = Image.open("1.png").convert('L')
    # img = color.rgb2gray(io.imread('1.png'))
    # img = io.imread('1.png', as_gray=True)

    # img = imread("1.png")
    userInput = np.asarray(img)
    print(np.asarray(img))
    print("YER?")
    print(userInput.shape)
    # img = img.flatten()
    # print("YERRR")
    # print(img.reshape(64,))
    # print(img.shape)
    # userInput = img

    # userInput = userInput.flatten()
    # print(userInput)
    # print(userInput.shape)


    prediction = 0
    # prediction = model.predict(userInput)
    prediction = model.predict(userInput.reshape(1,-1))


    print()
    for i in range(len(prediction)):
        if prediction[i] == 0:
            print(f"PREDICTION - REAL: 3", end='')
            prediction = 3
            wordedNumber = "THREE"
        elif prediction[i] == 1:
            print(f"PREDICTION - REAL: 0", end='')
            prediction = 0
            wordedNumber = "ZERO"
        elif prediction[i] == 2:
            print(f"PREDICTION - REAL: 8", end='')
            prediction = 8
            wordedNumber = "EIGHT"
        elif prediction[i] == 3:
            print(f"PREDICTION - REAL: 1", end='')
            prediction = 1
            wordedNumber = "ONE"
        elif prediction[i] == 4:
            print(f"PREDICTION - REAL: 9", end='')
            prediction = 9
            wordedNumber = "NINE"
        elif prediction[i] == 5:
            print(f"PREDICTION - REAL: 2", end='')
            prediction = 2
            wordedNumber = "TWO"
        elif prediction[i] == 6:
            print(f"PREDICTION - REAL: 4", end='')
            prediction = 4
            wordedNumber = "FOUR"
        elif prediction[i] == 7:
            print(f"PREDICTION - REAL: 7", end='')
            prediction = 7
            wordedNumber = "SEVEN"
        elif prediction[i] == 8:
            print(f"PREDICTION - REAL: 6", end='')
            prediction = 6
            wordedNumber = "SIX"
        elif prediction[i] == 9:
            print(f"PREDICTION - REAL: 5", end='')
            prediction = 5
            wordedNumber = "FIVE"

    print()

    return prediction,wordedNumber




# def kmeans(userInput):
#     digits = datasets.load_digits()
#     # print(digits.data)
#     plt.gray()
#     k = 10
#     model = KMeans(n_clusters=k,random_state=10)
#     model.fit(digits.data)
#     # prediction = model.predict(userInput)
#     # print(prediction)
    


def test():
    print("recognizing")
    # image = Image.open("1.png")
    image = Image.open("1.png")
    image = image.resize((8,8),Image.ANTIALIAS)
    # image = image.resize((28,28),Image.ANTIALIAS)
    # image = image.resize((84,84),Image.ANTIALIAS)
    image.save("1.png",quality=95)
    imageData = np.asarray(image)

    # with np.printoptions(threshold=np.inf):
        # print(imageData)
    # print("yer")
    # print(imageData)

    return kmeans(imageData)
