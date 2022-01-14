import numpy as np 



# non va verifier si 1+ pivots sont nécessaires en raison d'un élément négatif dans la colonne la plus à droite,
#  à l'exclusion de la valeur inférieure
def gen_matrix(var,cons):    
    return np.zeros((cons+1, var+cons+2))

# nous vérifierons si 1+ pivots sont nécessaires en raison d'un élément négatif dans la ligne inférieure, 
# à l'exclusion de la valeur finale.
def next_round_r(table):    
    m = min(table[:-1,-1])
    return m < 0
#on a créé des fonctions qui renvoient des booléens, que des pivots supplémentaires soient nécessaires ou non, nous devons déterminer où se trouvent ces éléments. 
# on va  commencer par trouver les éléments négatifs dans la colonne la plus à droite.
def next_round(table):    
    l_right = len(table[:,0])
    m = min(table[l_right-1,:-1])
    return m < 0
# nous devons localiser les éléments négatifs dans la rangée inférieure
def position_negative_row(table):
    l_left = len(table[0,:])
    m = min(table[:-1,l_left-1])
    return np.where(table[:-1,l_left-1] == m)[0][0] if m<=0 else None

def find_neg(table):
    l_right = len(table[:,0])
    m = min(table[l_right-1,:-1])
    return np.where(table[l_right-1,:-1] == m)[0][0] if m<=0 else None
# nous avons identifié les indices de colonne et de ligne, respectivement ,
# pour les éléments négatifs de la dernière colonne et de la dernière ligne.
#  Mais nous devons aller plus loin et trouver l'élément pivot correspondant à ces valeurs
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
#on a besoin qu'elle fasse un pivot 
# autour d'un élément afin de supprimer l'entrée négative dans la dernière colonne ou ligne et de retourner le tableau mis à jour.

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
# on a besoin d'un moyen pour l'utilisateur d'entrer une chaîne de caractères, qui sera convertie en variables flottantes. 
# Notre fonction recevra des entrées telles que ('100,300,inf_egale,400') ; 
# cela signifie 100(x1) + 300(x2) ≤ 400. Alternativement, 'sup_egale' pourrait être utilisé pour signifier une inégalité ≥.

def convert(eq):
    eq = eq.split(',')
    if 'sup_egale' in eq:
        g = eq.index('sup_egale')
        del eq[g]
        eq = [float(i)*-1 for i in eq]
        return eq
    if 'inf_egale' in eq:
        l = eq.index('inf_egale')
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

# la toute première étape consiste à indiquer à python combien de variables et de contraintes 
# il y a et à générer une matrice de taille adéquate. 
# Il s'ensuit que nous avons besoin d'un moyen de vérifier si des contraintes 1+ peuvent être ajoutées à la matrice, 
# ce qui signifie qu'il y a au moins deux rangées de tous les éléments 0. Si cette condition n'est pas satisfaite, 
# notre programme ne permettra pas à l'utilisateur d'ajouter des contraintes supplémentaires


def add_cons(table):
    l_right = len(table[:,0])
    empty = []
    for i in range(l_right):
        total = sum(j**2 for j in table[i,:])
        if total == 0: 
            empty.append(total)
    return len(empty)>1
# nous devons en fait ajouter les contraintes au problème. Nous pouvons définir uniquement la fonction comme suit.
#  La fonction prendra le tableau comme argument ainsi que l'équation, 
# qui sera convertie en utilisant la fonction précédente et sera insérée dans le tableau, de manière appropriée.

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



#nous avons besoin d'une fonction qui puisse vérifier si la fonction objectif peut être ajoutée. 
# Il existe de nombreuses façons d'aborder ce problème, mais mon approche a été d'ajouter la fonction objectif en dernier, 
# après que toutes les contraintes aient été saisies, car il s'agit de la dernière ligne du tableau

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
        print()
        print('la resultat de Big M')
        print()
        print()

# Il est enfin temps d'assembler tous les éléments et de créer les fonctions de maximisation et de minimisation 
# Ces fonctions seront très similaires, elles utiliseront toutes deux des boucles while pour déterminer
#  si un pivot 1+ est nécessaire, localiser l'élément pivot, pivoter autour de celui-ci et continuer le processus 
# jusqu'à ce que tous les éléments négatifs aient été retirés de la dernière colonne et de la dernière ligne. 
# Ensuite, des variables seront générées pour x1 à xn et des valeurs leur seront attribuées en fonction de leur position dans le tableau.
#  De plus, la valeur appropriée sera attribuée à max. Enfin, la fonction renvoie le max et les variables sous forme de dictionnaire

def max_M(table):
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


def minz_M(table):
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

def afff(gen_matrix, constrain, obj, max_M, minz_M):
   # m = gen_matrix(2,2)
    #constrain(m,'2,-1,sup_egale,10')
    #constrain(m,'1,1,inf_egale,20')
    #obj(m,'2,10,0')
    #print(max_M(m))     
    
    m = gen_matrix(2,4)
    constrain(m,'4,3,sup_egale,250')
    constrain(m,'3,4,sup_egale,270')
    constrain(m,'2,5,sup_egale,300')
    
    obj(m,'200,350')
    print(minz_M(m))

if __name__ == "__main__":
    afff(gen_matrix, constrain, obj, max_M, minz_M)