"""
        ----------Objectif du Programme ""

 ce programme permet de résoudre des problèmes de maximisation ou minimisation et aussi 
 de déterminer la valeur de la fonction objectif (fonction économique Z ) 
 en utilisant la méthode simplex .
 et aussi en utilisant la methode Big M

                        
"""

import sys #on va intéragir avec le système,donc on importe le système
import numpy as np # numpy librairie destinée à manipuler des matrices ou des tableaux ainsi que des fonctions mathématiques opérant sur des tableaux..
                   # numpy va retourner un array (une variable spéciale pouvant contenir plusieurs valeurs à la fois donc un tableau ) --- np

#  on démarre une liste vide [], puis  on utilise la fonction append() ou extend() pour y ajouter des éléments:
# le programme utilise que des boucles for,while ...aucune fonction spécial à part append(),range()
noms_contraint = []      # nom des contraintes 
noms_des_contraintes = [] #
valeurs_des_colones = []
equation_de_z = []         
final_rows = []
solutions = []
x = 'X'                # x= X pour ne pas utiliser x,y ainsi que e ,donc nous aurons X1,X2 .......Xn
equation_de_z2 = []
variables_suprimer = []

print ( "pour executer la question_2 , cliquez sur numero 2")
k = input(str("choix s or m or Q2 ==> ecrivez s : Simplexe , Or m : Big_M ( warning changer les variable à la main avant d'executer M à la ligne 703) "))
def simplexee():                  
    global nombre_object_Z, nombre_des_contraintes
    print("""
               #######################################################################|
               |                     Coding By SASSI Youssef                          |
               |        sous la direction du  Monsieur Thiago ABREU  :                | 
               |                                                                      |   
               |             département informatique , EPISEN ITS.                   |
               |                                                                      |
               ########################################################################

 Avant de commencer,quel type de problème voulez-vous résoudre ?	
    1 :Max( <= ).
    2 :Min ( >= ).
 
    0 : Aide.

    """)

    try:        # try permet de gérer les erreurs au cas où l'utilisateur ne respecte pas les normes du programme
        type_probleme = int(input(" choisisez  un numereo ( 1 , 2 ou 0 )  >")) # l'utilisateur doit tapper un nombre entier positif
    except:                                                             # exception pour les erreurs puis afficher un message à l'utilisateur
        print("try again !! choisissez un numéro ")
        type_probleme = int(input(" choisisez  un numereo ( 1 , 2 ou 0 )  >")) # on lui donne une chance de choisir un numéro

    if type_probleme not in [2, 1, 0]:  # si l'utilisateur n'a pas choisit le numéro 0 ou 1 ou 2
        sys.exit("vous avez choisi un mauvais choix  try again ->" + str(type_probleme)) #le programme s'arrete avec ce message + le numéro choisi  
    if type_probleme == 0: # si l'utilisateur a choisi la valeur de 0, il verra un méssage d'aide
        print(r"""
        Help :
        Résolution les problèmes par la méthode simplex
        
       

                       
         ----------Résolution par le programme python-------

         1) combien des variable Z  ? 1 2 3 ....... n   vous avez le choix 
         2) combien de contraintes avez-vous ? 1 2 3 ....... n   vous avez le choix 
         3) définissez les noms de contrainte pour mieux organiser les données,exemple A , B C , Youssef  ...........
         4) cette étape, nous allons écrire l'équation de la Z fonction objéctive 
             Soit X1  numéro 1 
                  X2  numéro 2 
                  Xn  numéro N  
                  ce sont les variables de contraintes 

                Z = X1 + X2 + ... + Xn   

                contrainte 1 = X1 + X2    
                contrainte 2 = X1 + X2  
                contrainte 3 = X1 + X2   
                contrainte n = X1 + X2     
             
              
           

        5) Vous aurez votre tableau simplex avec les solutions admissibles .
        Merci  
                 
        """)
        sys.exit() # le programme s'arrete et on sort de la condition if type_problème = 0

    print('\n##########################################')
    nombre_object_Z = int(input("combien de variable dans Z ?: >")) # on va choisir les nombres de variable X1 X2 ...... 
    nombre_des_contraintes = int(input("combien de contraintes  ?: >"))  #on va choisir le nombre de Contrainte ( n )

    #j'ai utilisé boucle for lorsque l’on souhaite répéter un nombre donné de fois la même instruction ou le même bloc d’instructions,
    
    for i in range(1, nombre_object_Z + 1): 
        val = x + str(i)                         # on va nommer les contrainte pour faciliter à comprendre chaque contrainte pour les donner des variables ( organisation pour ne pas faire des erreur)
        noms_des_contraintes.append(val)        #la fonction append() a été défini en haut 

    for i in range(1, nombre_des_contraintes + 1): #        # on va nommer les contrainte pour faciliter à comprendre chaque contrainte pour les donner des variables ( organisation pour ne pas faire des erreur)

        valeur_cont = input("le nom du contrainte numéro %d : > par exemple (A , B ..) " % i)
        noms_contraint.append(valeur_cont)
    print("_______________________________________________________________")
   # Soit xj la numéro j, j= 1....n, . 
   # Alors Z = C1x1 + C2x2 + ... + Cnxn ( fonction objective )

    if type_probleme == 1:
        for i in noms_des_contraintes:
            try:
                val = float(input("la variable de  %s dans la fonction objectif( Z ): >" % i))  # ajouter les valeur de X1 ...Xn 
            except:               
                print("s'il vous plaît entrez un numéro")
                val = float(input("le coût unitaire associé à %s dans la fonction objectif( Z ): >" % i)) # ajouter les valeur de X1 ...Xn
            equation_de_z.append(0 - float(val))
        equation_de_z.append(0)

        while len(equation_de_z) <= (nombre_object_Z + nombre_des_contraintes):
            equation_de_z.append(0)
        print("________________________________________________________________")

       
        for prod in noms_contraint:
            for const in noms_des_contraintes:
                try:
                    val = float(input("quelle est la contrainte de %s dans %s ? >" % (const, prod))) # remplir chaque variable par un valeur pour chaque contrainte ( remlir en chaine avec un boucle ) avec l'utilisateur en clavier 
                except:                                                                                # avec meme nombre de variable de contrainte
                    print(" entré un numéro")
                    val = float(input("quelle est la contrainte de %s dans %s ? >" % (const, prod)))
                valeurs_des_colones.append(val)
            equate_prod = float(input('Equation donne combien ? %s : >' % prod)) #le système d'équation somme de ai1x1 + ai2x2 + ... + ainxn <= bi
            valeurs_des_colones.append(equate_prod)

        col_final = t_rows(valeurs_des_colones) # on lance  la méthode simplex et on insère des valeurs
        i = len(noms_des_contraintes) + 1
        while len(noms_des_contraintes) < len(col_final[0]) - 1:
            noms_des_contraintes.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        noms_des_contraintes.append('Solution')
        col_final.append(equation_de_z)
        cols_vals = np.array(col_final) # np a été défini en haut
        for a, _ in enumerate(equation_de_z):
            row = cols_vals[:, a]
            row = row.tolist()
            final_rows.append(row)
        print('\n##########################################')
        Max(col_final, final_rows)



    elif type_probleme == 2:
        for i in noms_des_contraintes:
            try:
                val = float(input("la valeur de %s dans l'équation de Z (fonctiction objectif): >" % i)) # ajouter les valeur de X1 ...Xn
            except:
                print("s'il vous plait entrez un numéro")
                val = float(input("la valeur de %s dans l'equation de Z (fonction objectif ): >" % i))
            equation_de_z.append(val)
        equation_de_z.append(0)

        while len(equation_de_z) <= (nombre_object_Z + nombre_des_contraintes):
            equation_de_z.append(0)
        print("________________________________________________________________")

        for prod in noms_contraint:
            for const in noms_des_contraintes:
                try:
                    val = float(input("quelle est la contrainte de %s dans --> %s ? >" % (const, prod))) # remplir chaque variable par un valeur pour chaque contrainte ( remlir en chaine avec un boucle ) avec l'utilisateur en clavier 
                except:                                                                                # avec meme nombre de variable de contrainte
                
                    print("s'il vous plaît Assurez-vous d'avoir entré un numero")
                    val = float(input("le cout unitaire associé à %s dans %s: >" % (const, prod)))
                valeurs_des_colones.append(val)
            equate_prod = float(input('Equation donne combien ? %s : >' % prod))
            valeurs_des_colones.append(equate_prod)


        # on démare le tableau de simplex  
       #on peut distinguer trois blocs. 
       #D’abord la fonction objective sur la première ligne.
       #Ensuite, un système d’équation linéaire (de type Ax = b) correspondant à l’ensemble des contraintes du
      #programme, finalement les contraintes de positivités des variables. Remarquons ensuite que les variables
      #sont indexées de 1 à n et qu’on a mis chacune sur une colonne néanmoins la première colonne est réservée
      #aux variables de la base (J + (X0 )). De plus la dernière colonne du tableau est réservée aux valeurs des
      #variables dans la base et la dernière ligne du tableau aux coefficients de la fonction objectives(δj ). Ainsi,
      #on peut garder uniquement le coefficient et la colonne sans mentionner la variable sur chaque ligne. On
      #obtient ainsi le tableau du simplexe correspondant .


        col_final = r_rows(valeurs_des_colones)
        i = len(noms_des_contraintes) + 1
        while len(noms_des_contraintes) < nombre_des_contraintes + nombre_object_Z:
            noms_des_contraintes.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        solutions[:] = []
        add_from = len(noms_des_contraintes)+1
        while len(noms_des_contraintes) < len(col_final[0][:-1]):
            variables_suprimer.append('X' + str(add_from))
            noms_des_contraintes.append('X' + str(add_from))
            add_from += 1
        variables_suprimer.append(' Z')
        variables_suprimer.append('Z1')
        noms_des_contraintes.append('Solution')
        for ems in variables_suprimer:
            solutions.append(ems)
        while len(equation_de_z) < len(col_final[0]):
            equation_de_z.append(0)
        col_final.append(equation_de_z)
        col_final.append(equation_de_z2)
        cols_vals = np.array(col_final)
        for a, _ in enumerate(equation_de_z):
            row = cols_vals[:, a]
            row = row.tolist()
            final_rows.append(row)
        print('\n##########################################')
        Min(col_final, final_rows)

    else:
        sys.exit("vous avez fait un mauvais choix :p try an other one->" + str(type_probleme))

# partie MAX
def Max(col_final, final_rows): 
    row_app = []
    final_new_row = []
    last_colone = col_final[-1]
    min_derniere_colone = min(last_colone)
    min_manager = 1
    print(" TABLEAU 1")
    print('  ', noms_des_contraintes)
    for i, cols in enumerate(col_final):
        print(solutions[i], cols)
    count = 2
    while min_derniere_colone < 0 and min_manager == 1:
        print("*********************************************************")
        last_colone = col_final[-1]
        last_row = final_rows[-1]
        min_derniere_colone = min(last_colone)
        index_of_min = last_colone.index(min_derniere_colone)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        for i, _ in enumerate(last_row[:-1]):
            try:
                val = float(last_row[i] / pivot_row[i])
                val = 10000000000 if val <= 0 else val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        element_du_pivot = pivot_row[index_min_div_val]
        colones_du_pivot = col_final[index_min_div_val]
        index_colones_du_pivot = col_final.index(colones_du_pivot)
        row_app[:] = []
        index_pivot_elem = colones_du_pivot.index(element_du_pivot)
        for col in col_final:
            if col is not colones_du_pivot and col is not col_final[-1]:
                form = col[index_pivot_elem] / element_du_pivot
                for i, elem in enumerate(col):
                    value = (elem - float(form * colones_du_pivot[i]))
                    row_app.append(round(value, 2))
            elif col is colones_du_pivot:
                for elems in colones_du_pivot:
                    value = float(elems / element_du_pivot)
                    row_app.append(round(value, 2))
            else:
                form = abs(col[index_pivot_elem]) / element_du_pivot
                for i, elem in enumerate(col):
                    value = elem + float(form * colones_du_pivot[i])
                    row_app.append(round(value, 2))
        col_final[:] = []
        final_new_row[:] = []
        final_new_row = [row_app[x:x + len(equation_de_z)] for x in range(0, len(row_app), len(equation_de_z))]
        for list_el in final_new_row:
            col_final.append(list_el)
        cols_vals = np.array(col_final)
        final_rows[:] = []
        for a, _ in enumerate(equation_de_z):
            row = cols_vals[:, a]
            row = row.tolist()
            final_rows.append(row)
        min_manager = 1 if min(row_div_val) != 10000000000 else 0
        print('éléments du pivot: %s' % element_du_pivot)
        print('colone du pivot: ', pivot_row)
        print(' ', colones_du_pivot)
        print("\n")
        solutions[index_colones_du_pivot] = noms_des_contraintes[index_pivot_row]

        print(" TABLEAU %d " % count)
        print('  ', noms_des_contraintes)
        for i, cols in enumerate(col_final):
            print(solutions[i], cols)
        last_colone = col_final[-1]
        min_derniere_colone = min(last_colone)
        count += 1

# partie Minimization
def Min(col_final, final_rows):
    row_app = []
    final_new_row = []
    last_colone = col_final[-1]
    min_derniere_colone = min(last_colone)
    min_manager = 1
    print(" TABLEAU 1")
    print('  ', noms_des_contraintes)
    i = 0
    for cols in col_final:
        print(solutions[i], cols)
        i += 1
    count = 2
    while min_derniere_colone < 0 and min_manager == 1:
        print("*********************************************************")
        last_colone = col_final[-1]
        last_row = final_rows[-1]
        min_derniere_colone = min(last_colone[:-1])
        index_of_min = last_colone.index(min_derniere_colone)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        element_du_pivot = pivot_row[index_min_div_val]
        colones_du_pivot = col_final[index_min_div_val]
        index_colones_du_pivot = col_final.index(colones_du_pivot)
        row_app[:] = []
        index_pivot_elem = colones_du_pivot.index(element_du_pivot)
        for col in col_final:
            if col is not colones_du_pivot and col is not col_final[-1]:
                form = col[index_pivot_elem] / element_du_pivot
                i = 0
                for elem in col:
                    value = (elem - float(form * colones_du_pivot[i]))
                    row_app.append(round(value, 2))
                    i += 1
            elif col is colones_du_pivot:
                for elems in colones_du_pivot:
                    value = float(elems / element_du_pivot)
                    row_app.append(round(value, 2))
            else:
                form = abs(col[index_pivot_elem]) / element_du_pivot
                i = 0
                for elem in col:
                    value = elem + float(form * colones_du_pivot[i])
                    row_app.append(round(value, 2))
                    i += 1
        equals = len(col_final[0])
        col_final[:] = []
        final_new_row[:] = []
        final_new_row = [row_app[x:x + equals] for x in range(0, len(row_app), equals)]
        for list_el in final_new_row:
            col_final.append(list_el)
        cols_vals = np.array(col_final)
        a = 0
        final_rows[:] = []
        try:
            for _ in equation_de_z:
                row = cols_vals[:, a]
                row = row.tolist()
                final_rows.append(row)
                a += 1
        except:
            pass
        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('éléments du pivot: %s' % element_du_pivot)
        print('colone du pivot: ', pivot_row)
        print('', colones_du_pivot)
        print("\n")
        removable = solutions[index_colones_du_pivot]
        solutions[index_colones_du_pivot] = noms_des_contraintes[index_pivot_row]
        if removable in variables_suprimer:
            idex_remove = noms_des_contraintes.index(removable)
            for colms in col_final:
                colms.remove(colms[idex_remove])
            noms_des_contraintes.remove(removable)
        print("TABLEAU %d" % count)
        print('  ', noms_des_contraintes)
        i = 0
        for cols in col_final:
            print(solutions[i], cols)
            i += 1
        last_colone = col_final[-1]
        min_derniere_colone = min(last_colone)
        count += 1
        cols_vals = np.array(col_final)
        a = 0
        final_rows[:] = []
        try:
            for _ in equation_de_z:
                row = cols_vals[:, a]
                row = row.tolist()
                final_rows.append(row)
                a += 1
        except:
            pass


def r_rows(column_values):
    col_final = [column_values[x:x + nombre_object_Z + 1] for x in range(0, len(column_values), nombre_object_Z + 1)]
    for b, _ in enumerate(col_final[0]):
        z_sum = 0
        for row in col_final:
            z_sum = row[b] + z_sum
        equation_de_z2.append(0 - z_sum)
    for cols in col_final:
        while len(cols) < (nombre_object_Z + (2*nombre_des_contraintes)-1):
            cols.insert(-1, 0)


    i= nombre_object_Z
    for sub_col in col_final:
        sub_col.insert(i, -1)
        equation_de_z2.insert(-1, 1)
        i += 1

    for sub_col in col_final:
        sub_col.insert(i, 1)
        i += 1
    while len(equation_de_z2) < len(col_final[0]):
        equation_de_z2.insert(-1, 0)

    return col_final


def t_rows(column_values):
    col_final = [column_values[x:x + nombre_object_Z + 1] for x in range(0, len(column_values), nombre_object_Z + 1)] 
    for cols in col_final:
        while len(cols) < (nombre_object_Z + nombre_des_contraintes):
            cols.insert(-1, 0)

    i = nombre_object_Z
    for sub_col in col_final:
        sub_col.insert(i, 1)
        i += 1
    return col_final

'''

la Partie Big M 
Nb : il y a encore de probleme pour les grandes valeurs 

'''
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
        print('voici la resultat avec la methode du Big _ M ')
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


def min_M(table):
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
def Question_2(gen_matrix, constrain, obj, max_M, min_M):
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
    print(min_M(m))
def afff(gen_matrix, constrain, obj, max_M, min_M):
   # m = gen_matrix(2,2)
    #constrain(m,'2,-1,sup_egale,10')
    #constrain(m,'1,1,inf_egale,20')
    #obj(m,'2,10,0')
    #print(max_M(m))     
    
    m = gen_matrix(2,4)
    constrain(m,'1,3,sup_egale,250')
    constrain(m,'3,4,sup_egale,270')
    constrain(m,'2,5,sup_egale,300')
    
    obj(m,'200,350')
    print(min_M(m))

def choix():
    if k == "s":
        simplexee()

    if k == "m":
        afff(gen_matrix, constrain, obj, max_M, min_M)

    if k =="Q2":
        Question_2(gen_matrix, constrain, obj, max_M, min_M)


if __name__ == "__main__":
    choix()




