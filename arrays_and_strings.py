import matplotlib.pyplot as plt
import cv2 
import numpy as np

def is_unique(string_data):
    new = []
    for x in string_data:
        if x in new:
            return False
        else:
            new.append(x)
    return True

def is_permutation(str_data1, str_data2):
    if len(str_data1) != len(str_data2):
        return False
    d_str1 = {x: 0 for x in str_data1}
    for x, y in zip(str_data1, str_data2):
        d_str1[x] = d_str1[x]+1
        d_str1[y] = d_str1[y]+1
    for values in d_str1.values():
        if values%2 != 0:
            return False
    return True

def URLify(string):
    string = string.strip().replace(" ", "%20")
    return string

def permutation_palindrome(string):
    string = string.strip().replace(" ", "")
    unq_str = list(set(string))
    d_str = {x : 0 for x in unq_str}
    for val in string:
        d_str[val] = d_str[val]+1
    for values in d_str.values():
        if values%2 != 0:
            return False
    return True

def func1(str1, str2):
    count = 0
    for id in zip(str1, str2):
        if x != y:
            count = count +1
    if count > 1:
        return False
    else:
        return True
        

def one_away(str_1, str_2):
    i = 0    
    if len(str_1) - len(str_2) > 1:
        return False
    
    if len(str_1) == len(str_2):
        return func1(str_1, str_2)
    
    if len(str_2) > len(str_1):
        str1 = str_2
        str2 = str_1
    else:
        str1 = str_1
        str2 = str_2
        
    
    for idx_1, val_1 in enumerate(str1):
        if i < len(str2) and str2[i] == val_1:
            i = i + 1   
    if i == len(str1)-1:
        return True
    else:
        return False    

def compressed(str1):
    i = 0
    string_final = ""
    for idx, val in enumerate(str1):
        i = i + 1
        if idx + 1 == len(str1) or val != str1[idx+1]:
            string_final = string_final + val + str(i)
            i = 0
    return string_final


image = cv2.imread("./images_rotate.jpeg")
#Extract just the first channel
image = image[:,:,0:1]
image = image.reshape((image.shape[0], image.shape[1]))

def rotate_90(image):
    p = np.arange(0, -len(image), -1)
    q = np.arange(len(image)-1, -1 , -1)
    new_image = np.zeros_like(image)
    for i in range(image.shape[0]):
        temp1 = p[i]
        temp2 = q[i]
        for j in range(image.shape[1]):
            new_image[i, j] = image[i+temp1, j+temp2]
            temp1 = temp1+1
            temp2 = temp2-1
    return new_image

fig, ax = plt.subplots(2)
ax[0].imshow(image)
ax[1].imshow(rotate_90(image))
fig.show()

def zero_matrix(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i, j] == 0:
                break
        if mat[i, j] == 0:
            break
            
    mat[i, :] = 0
    mat[:, j] = 0
    return mat

def string_rotation(word, rotated_word):
    if word in rotated_word+rotated_word:
        return True


