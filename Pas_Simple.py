
pas=0.05
first_position=0.0

def x(i):
    if i>0:
        return first_position+(i-1)*pas
    else:
        return first_position+(i+1)*pas


def fonction(i):
    return x(i)**2-1.5*x(i)

def pas_fixe():
    i=1
    if fonction(2)<fonction(1) :
        while fonction(i+1)<fonction(i): 
            i+=1
        x1=x(i-1)
        x2=x(i)
    elif fonction(2)>fonction(1):
        while fonction(i+1)>fonction(i):
            i-=1
        x1=x(i-1)
        x2=x(i)
    
    elif fonction(2)>fonction(1):
        x1=x(-2)
        x2=x(2)
    
    elif fonction(2)==fonction(3):
        x1=x(1)
        x2=x(2)
    return i,x1,x2

def aff(fonction, pas_fixe):
    results=pas_fixe()
    i=results[0]
    x1=results[1]
    x2=results[2]   
    print(fonction(i),x1,x2)

aff(fonction, pas_fixe)
                 
             

    