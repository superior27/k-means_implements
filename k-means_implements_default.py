#-*- coding:utf-8-*-
from numpy import loadtxt
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import random

list_points = np.array([[1.9,7.3],[3.4,7.5],[2.5,6.8],[1.5,6.5],[3.5,6.4],
    [2.2,5.8],[3.4,5.2],[3.6,4],[5,3.2],[4.5,2.4],
    [6,2.6],[1.9,3],[1,2.7],[1.9,2.4],[0.8,2],
    [1.6,1.8],[1,1]])

def initializationCentroid():
    my_centroid_x = random.uniform(0,9)
    my_centroid_y = random.uniform(0,10)
    my_centroid = [my_centroid_x,my_centroid_y] 
    return my_centroid

def createQuantityCentroid(quantity_centroid):
    list_centroid = []
    i=0
    while(i<quantity_centroid):
        list_centroid.append(initializationCentroid())
        i+=1
    my_list_centroid = np.array(list_centroid)
    return my_list_centroid

def calculateDistance(list_centroid):
    my_list_point = []
    my_point = []
    for element_point in list_points:
        for element_centroid in list_centroid:      
            result_x = (element_point[0]-element_centroid[0])**2
            result_y = (element_point[1]-element_centroid[1])**2
            result = (result_x+result_y)**0.5
            element_point = np.append(element_point,result)
        my_list_point.append(element_point)
    new_list_point = np.array(my_list_point)
    return new_list_point

def classificationPoints(list_points):
    my_list_point = []
    for element_point in list_points:
        menor = min(element_point[2::])
        number = np.where(element_point==menor)
        element_point = np.append(element_point,(number[0][0]-2))
        my_list_point.append(element_point)
    new_list_point = np.array(my_list_point)
    del my_list_point
    return new_list_point

def recalculateCentroid(list_centroid,list_points):
    i = 0
    cont_element = 0
    new_list_centroid = list_centroid
    while(i < len(list_centroid)):
        media_centroid_x = 0
        media_centroid_y = 0
        cont_element = 0
        for element_point in list_points:
            if element_point[-1] == i:
                media_centroid_x+=element_point[0]
                media_centroid_y+=element_point[1]
                cont_element+=1
        if cont_element:
            media_centroid_x = media_centroid_x/cont_element
            media_centroid_y = media_centroid_y/cont_element
            new_list_centroid[i][0] = media_centroid_x
            new_list_centroid[i][1] = media_centroid_y        
        i+=1
    del list_centroid
    return new_list_centroid

def myLoop():
    cont = 0
    number = int(raw_input("Informe o número de Centróides que deseja:"))
    flag = 1
    my_list_centroid = createQuantityCentroid(number)
    my_list_points = calculateDistance(my_list_centroid)
    my_list_points = classificationPoints(my_list_points)    
    old_list_centroid = my_list_centroid.copy()
    print my_list_centroid
    print old_list_centroid
    while flag or cont == 30:
        my_list_centroid = recalculateCentroid(my_list_centroid,my_list_points)
        my_list_points = calculateDistance(my_list_centroid)
        my_list_points = classificationPoints(my_list_points)
        print my_list_centroid
        print old_list_centroid
        if np.array_equal(my_list_centroid, old_list_centroid):
            flag = 0
        else:
            old_list_centroid = my_list_centroid.copy()
        cont+=1
    print "Número de interações: "+str(cont)
        

myLoop()