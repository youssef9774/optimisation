
#Pas_accelere
def x(i,first_position,x1):
    if i>0:
        return x1+(i-1)*first_position
    else:
        return x1+(i+1)*first_position


def f(i,first_position,x1):
    return x(i,first_position,x1)**2-1.5*x(i,first_position,x1)

def pas_acc():
    x1=0.0
    first_position=0.05
    i=1
    if f(2,first_position,x1)<f(1,first_position,x1):
        while f(i+1,first_position,x1)<f(i,first_position,x1): 
            i+=1
            first_position *= 2
        x1=x(i-1,first_position,x1)
        x2=x(i,first_position,x1)
    if f(2,first_position,x1)>f(1,first_position,x1):
        while f(i+1,first_position,x1)>f(i,first_position,x1):
            i-=1
            first_position *= 2
        x1=x(i-1,first_position,x1)
        x2=x(i,first_position,x1)
    elif f(2,first_position,x1)==f(3,first_position,x1):
        x1=x(1,first_position,x1)
        x2=x(2,first_position,x1)
    elif f(2,first_position,x1)>f(1,first_position,x1):
        x1=x(-2,first_position,x1)
        x2=x(2,first_position,x1)
    return i,x1,x2,first_position

def new_func(pas_acc):
    results=pas_acc()
    i=results[0]
    x1=results[1]
    x2=results[2]   
    first_position=results[3]
    return x1,x2

x1, x2 = new_func(pas_acc)
print(" resultat in ",x1,"$",x2)
