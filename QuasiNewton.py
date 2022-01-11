#QuasiNewton

def fonction(j):
    return j**3-j-1


def fonction_dis(func,j,dx):
    return (func(j+dx)-func(j-dx))/(2*dx)

def fonction_dis1(func,j,dx):
    return (func(j+dx)-2*func(j)+func(j-dx))/((dx)**2)

def variablee():
    premier_pos=1
    dx=0.01
    eps=0.001
    return premier_pos,dx,eps

premier_pos, dx, eps = variablee()


def j(i,premier_pos,dx,func):
    if i==1:
        return premier_pos
    else:
        return j(i-1,premier_pos,dx,func)-((dx*(func(j(i-1,premier_pos,dx,func)+dx)-func(j(i-1,premier_pos,dx,func)-dx)))/(2*(func(j(i-1,premier_pos,dx,func)+dx)-2*func(j(i-1,premier_pos,dx,func))+func(j(i-1,premier_pos,dx,func)-dx))))

def resultat(func,dx,premier_pos,eps):
    i=1
    while abs(fonction_dis(func,j(i,premier_pos,dx,func),dx))>eps:
        i+=1
    return j(i,premier_pos,dx,func)

print (resultat(fonction,dx,premier_pos,eps))