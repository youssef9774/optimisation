import numpy as np 
def gen_matrix(var,cons):    
    return np.zeros((cons+1, var+cons+2))

def next_round_r(table):    
    m = min(table[:-1,-1])
    return m < 0

def next_round(table):    
    l_right = len(table[:,0])
    m = min(table[l_right-1,:-1])
    return m < 0

def position_negative_row(table):
    l_left = len(table[0,:])
    m = min(table[:-1,l_left-1])
    return np.where(table[:-1,l_left-1] == m)[0][0] if m<=0 else None

def find_neg(table):
    l_right = len(table[:,0])
    m = min(table[l_right-1,:-1])
    return np.where(table[l_right-1,:-1] == m)[0][0] if m<=0 else None

def loc_piv_r(table):
    total = []        
    r = position_negative_row(table)
    row = table[r,:-1]
    m = min(row)
    c = np.where(row == m)[0][0]
    col = table[:-1,c]
    for i, b in zip(col,table[:-1,-1]):
        if i**2>0 and b/i>0:
            total.append(b/i)
        else:                
            total.append(10000)
    index = total.index(min(total))        
    return [index,c]

def loc_piv(table):
    if next_round(table):
        total = []
        n = find_neg(table)
        for i,b in zip(table[:-1,n],table[:-1,-1]):
            if b/i >0 and i**2>0:
                total.append(b/i)
            else:
                total.append(10000)
        index = total.index(min(total))
        return [index,n]

def pivot(row,col,table):
    l_right = len(table[:,0])
    l_left = len(table[0,:])
    t = np.zeros((l_right,l_left))
    pr = table[row,:]
    if table[row,col]**2>0:
        e = 1/table[row,col]
        r = pr*e
        for i in range(len(table[:,col])):
            k = table[i,:]
            c = table[i,col]
            if list(k) == list(pr):
                continue
            else:
                t[i,:] = list(k-r*c)
        t[row,:] = list(r)
        return t
    else:
        print('pivot interdie.')


def convert(eq):
    eq = eq.split(',')
    if 'G' in eq:
        g = eq.index('G')
        del eq[g]
        eq = [float(i)*-1 for i in eq]
        return eq
    if 'L' in eq:
        l = eq.index('L')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq

def convert_min(table):
    table[-1,:-2] = [-1*i for i in table[-1,:-2]]
    table[-1,-1] = -1*table[-1,-1]    
    return table

def gen_var(table):
    l_left = len(table[0,:])
    l_right = len(table[:,0])
    var = l_left - l_right -1
    return ['x'+str(i+1) for i in range(var)]


def add_cons(table):
    l_right = len(table[:,0])
    empty = []
    for i in range(l_right):
        total = sum(j**2 for j in table[i,:])
        if total == 0: 
            empty.append(total)
    return len(empty)>1

def constrain(table,eq):
    if add_cons(table) == True:
        l_left = len(table[0,:])
        l_right = len(table[:,0])
        var = l_left - l_right -1      
        j = 0
        while j < l_right:            
            row_check = table[j,:]
            total = 0
            for i in row_check:
                total += float(i**2)
            if total == 0:                
                row = row_check
                break
            j +=1
        eq = convert(eq)
        i = 0
        while i<len(eq)-1:
            row[i] = eq[i]
            i +=1        
        row[-1] = eq[-1]
        row[var+j] = 1    
    else:
        print('max constraint.')
def add_obj(table):
    l_right = len(table[:,0])
    empty = []
    for i in range(l_right):
        total = sum(j**2 for j in table[i,:])
        if total == 0:
            empty.append(total)
    return len(empty)==1

def obj(table,eq):
    if add_obj(table)==True:
        eq = [float(i) for i in eq.split(',')]
        l_right = len(table[:,0])
        row = table[l_right-1,:]
        i = 0        
        while i<len(eq)-1:
            row[i] = eq[i]*-1
            i +=1
        row[-2] = 1
        row[-1] = eq[-1]
    else:
        print('..')


def maxz(table):
    while next_round_r(table)==True:
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)
    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)        
    l_left = len(table[0,:])
    l_right = len(table[:,0])
    var = l_left - l_right -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]            
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0
    val['max'] = table[-1,-1]
    return val


def minz(table):
    table = convert_min(table)
    while next_round_r(table)==True:
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)    
    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)       
    l_left = len(table[0,:])
    l_right = len(table[:,0])
    var = l_left - l_right -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]             
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0 
            val['min'] = table[-1,-1]*-1
    return val

def afff(gen_matrix, constrain, obj, maxz, minz):
    m = gen_matrix(2,2)
    constrain(m,'2,-1,G,10')
    constrain(m,'1,1,L,20')
    obj(m,'2,10,0')
    print(maxz(m))     
    m = gen_matrix(2,4)
    constrain(m,'2,5,G,30')
    constrain(m,'-3,5,G,5')
    constrain(m,'8,3,L,85')
    constrain(m,'-9,7,L,42')
    obj(m,'2,7,0')
    print(minz(m))

if __name__ == "__main__":
    afff(gen_matrix, constrain, obj, maxz, minz)