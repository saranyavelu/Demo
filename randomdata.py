import random
import numpy

def Rand(start, end, size):
    val = []
    for j in range(100):
        val.append(numpy.random.randint(start, end, size)) 
   
    return val



