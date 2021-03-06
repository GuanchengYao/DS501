#-------------------------------------------------------------------------
# Note: please don't use any additional package except the following packages
import numpy as np
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import PIL
from sklearn.datasets import fetch_olivetti_faces
# Hint: you can reuse the functions that you have implemented in problem 1. For example, p1.PCA() 
import problem1 as p1 
#-------------------------------------------------------------------------
'''
    Problem 3: eigen faces 
    In this problem, you will use PCA to compute eigen faces in a face image dataset.
    We will use olivetti face image dataset (http://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html).
    It include 400 face images, and 40 human subjects. For each human subject, we have 10 face images.
    Each face image is a 64 by 64 black-and-white image.
    You need to install the following package:
        * sklearn
        * scipy
        * pillow
    You could use `pip install sklearn`                        
                  `pip install pillow`
                  `pip install scipy` to install the packages.
    You could test the correctness of your code by typing `nosetests -v test3.py` in the terminal.
    Hint: you can reuse the functions that you have implemented in problem 2. For example, p2.PCA() 

    Notations:
            ---------- input data ------------------------
            n: the number of face images, an integer scalar. (n = 400)
            p: the number of pixels in each image, an integer scalar. (p= 4096)
            c: the number of classes (persons), an integer scalar. (c = 40)
            h: the height of a face image, an integer scalar. (h = 64)
            w: the width of a face image, an integer scalar. (w = 64)
            X: the feature matrix, a float numpy matrix of shape n by p. (400 by 4096)
            y: labels associated to each face image, a numpy integer matrix of shape (n by 1). (400 by 1)
               The i-th element can be  0,1,..., or 39 corresponding to the Subject ID of the i-th image. 
            mu: the average vector of matrix X, a numpy float matrix of shape 1 by p. (1 by 4096)
                Each element mu[0,i] represents the average value in the i-th column of matrix X.
            mu_image: the average face image, a numpy float matrix of shape h by w (64 by 64). 
                      Each element mu[i,j] represents the average value in the ij-th pixel in all face images. 
            k: the number of dimensions to reduce to, an integer scalar.
            P_images:  the eigen faces, a python list of length k. 
                Each element in the list is an eigen face image, which is a numpy float matrix of shape 64 by 64. 
            Xp: the feature matrix with reduced dimensions, a numpy float matrix of shape n by k. (400 by k) 
'''

#--------------------------
def reshape_to_image(x):
    '''
        Reshape a feature vector into a face image 
        Input:
            x:  a feature vector , a float numpy matrix of shape (1, 4096). 
        Output:
            image: the face image, a float numpy matrix of shape (64,64). 
    (5 points)
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    image = np.reshape(x,(64,64))

    #########################################
    return image

#--------------------------
def compute_mu_image(X):
    '''
        Compute the average face image in the dataset . 
        Input:
            X:  the feature matrix, a float numpy matrix of shape (400, 4096). Here 400 is the number of images, 4096 is the number of features.
        Output:
            mu_image:  the average face image, a float numpy matrix of shape (64,64). Hint: you could reshape a vector of length 4096 into a matrix of shape 64 X 64
        Hint: you need first compute the average vector of matrix X. The shape of the average vector is (1 by 4096), then you can reshape the vector into a matrix of shape 64 by 64.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    a, mu_image = p1.centering_X(X)
    mu_image = reshape_to_image(mu_image)

    #########################################
    return mu_image


#--------------------------
def compute_eigen_faces(X, k=20):
    '''
        Compute top k eigen faces of the olivetti face image dataset using PCA.
        Input:
            X:  the feature matrix, a float numpy matrix of shape (400, 4096). Here 400 is the number of images, 4096 is the number of features.
            k:  the number of eigen face to keep. 
        Output:
            P_images:  the eigen faces, a python list of length k. 
                Each element in the list is an eigen face image, which is a numpy float matrix of shape 64 by 64. 
            Xp: the feature matrix with reduced dimensions, a numpy float matrix of shape n by k. (400 by k) 
        Note: this function may take 1-5 minutes to run, and 1-2GB of memory while running.
    '''
    
    #########################################
    ## INSERT YOUR CODE HERE
    Xp, P = p1.PCA(X, k)
    P_images = []
    for i in range(k):
        P_images.append(np.reshape(P[:,i],(64,64)))

    #########################################
    return P_images, Xp



#--------------------------
def load_dataset():
    '''
        Load (or download if not exist) the olivetti face image dataset (http://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html).
        Output:
            X: the feature matrix, a float numpy matrix of shape n by p. (400 by 4096)
            y: labels associated to each face image, a numpy integer matrix of shape (n by 1). (400 by 1)
               The i-th element can be  0,1,..., or 39 corresponding to the Subject ID of the i-th image. 
            images: numpy array of shape (400, 64, 64). Each face image is a (64, 64) matrix, and we have 400 images in the dataset.
        Hint: you could use fetch_olivetti_faces() function in sklearn package to download the dataset
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    # download (or load local copy of) the olivetti face image dataset
    faces = fetch_olivetti_faces()
    X = np.mat(faces['data'])

    # the images
    images = faces['images']

    # the label to predict is the id of the person
    y = np.mat(np.reshape(faces['target'],(400,1)))
    
    #########################################
    return X, y, images 


