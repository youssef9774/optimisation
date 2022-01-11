
import matplotlib.pyplot as plt
import numpy as np
#dicotomy

def dichotomy(fonction,extreme_1,extreme_2,e):
    
    amp, x1 = dico_(extreme_1, extreme_2)

    while amp > e:
        amp = abs(extreme_2 - extreme_1)
        
        if fonction(x1) == 0:
            return x1
        elif fonction(extreme_1) * fonction(x1)  > 0:
            extreme_1 = x1
        else:
            extreme_2 = x1
        x1 = (extreme_1 + extreme_2) / 2     
    return x1

def dico_(extreme_1, extreme_2):
    amp, x1 = ki(extreme_1, extreme_2)
    return amp,x1

def ki(extreme_1, extreme_2):
    amp = 1
    x1 = (extreme_1 + extreme_2)  / 2
    return amp,x1
        
print( dichotomy(lambda var1: var1*var1 - 1, 0, 1, 0.001) )

