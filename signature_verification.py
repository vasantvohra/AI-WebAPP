#!/usr/bin/env python
# coding: utf-8

# ## Standard libraries

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# ## Import keras

# In[2]:

import tensorflow as tf

from tensorflow.keras.models import load_model
from tensorflow.keras.models import model_from_json
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras import backend as K


# Loss function to find the distance score between two images

# In[3]:


def contrastive_loss(y_true, y_pred):
    '''Contrastive loss from Hadsell-et-al.'06
    http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf
    '''
    margin = 1
    return K.mean(y_true * K.square(y_pred) + (1 - y_true) * K.square(K.maximum(margin - y_pred, 0)))


# ## Load Siamese N/W architecture from saved model 

# In[4]:


json_file = open('siamese_BaseNetwork.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
base_network = model_from_json(loaded_model_json)
#print("checking")
#base_network.summary()


# ##  Root mean Square loss function

# In[5]:

# ## Load saved model architeture

# In[6]:
#def model_load():
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
#    model.summary()
#def weights_load():
rms = RMSprop(lr=1e-4, rho=0.9, epsilon=1e-08)
model.load_weights('./Weights/signet-Engsig260-003.h5')
model.compile(loss=contrastive_loss, optimizer=rms)

graph = tf.get_default_graph()

# In[22]:


def Show(img1,img2):
    '''Function to preview the signatures'''
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10, 10))
    ax1.imshow(np.squeeze(img1), cmap='gray')
    ax2.imshow(np.squeeze(img2), cmap='gray')
    ax1.axis('off')
    ax1.set_title("on record")
    ax2.axis('off')
    ax2.set_title("to be verified")
    plt.show()

# In[25]:
def Result(img1,img2):
    
    tr_acc, threshold=(0.8836851256190756, 0.14)#0.15
    global graph
    with graph.as_default():
        result=model.predict([img1, img2])
    diff = result[0][0]
    #print("Difference Score = ", diff)
    resultt=''
    if diff > threshold:
        resultt += "Its a Forged Signature"
    else:
        resultt += "Its a Genuine Signature"
    return threshold,diff,resultt


# In[21]:


img_h, img_w = 155, 220
def imageETL(img1,img2):
    '''Function to extract transform and load the signature acc. to model trained.'''
    img1 = cv2.resize(img1,(img_w,img_h))
    img2 = cv2.resize(img2,(img_w,img_h))
    img1 = np.array(img1, dtype = np.float64) #uint8
    img2 = np.array(img2, dtype = np.float64)
    img1 /= 255.0
    img2 /= 255.0
    img1 = img1[..., np.newaxis]
    img2 = img2[..., np.newaxis]
    img1 = img1[np.newaxis, ...]
    img2 = img2[np.newaxis, ...]
    L=[]
    L.append(img1)
    L.append(img2)
    return L

def main(genuine,candidate):
    print(genuine)
    print(candidate)
    img1 = cv2.imread(genuine,0)
    img2 = cv2.imread(candidate,0)
    ETL = imageETL(img1,img2)
    threshold,diff,result = Result(ETL[0], ETL[1])
    return threshold,diff,result
                 
##def Rdjango(genuine,candidate):
##    print(genuine)
##    print(candidate)
##    img1 = cv2.imread(genuine,0)
##    img2 = cv2.imread(candidate,0)
##    print(img1.shape,img2.shape)
##    diff,result = 0.045,"Its a Genuine Signature"
##    return diff,result
