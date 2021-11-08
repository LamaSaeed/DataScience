#problem 1 


# a : (1+5 , 3+2)
    # g1 : [1,3,4,5,7]
    # g2 : [1,3,4,5,7]
    # g3 : result
# b: (3*1 , 3*3)
    
# c: (3*5 , 3*2)
    
# d: ((3*1 , 3*3)+(3*5 , 3*2))

a, b, c= [1,3], [5,2], 3

def add_funct(g1, g2):
    g3=[]
    for i in range(len(g1)):
        g3.append(g1[i]+g2[i])
    return g3

def subt_funct(g1, g2):
    g3=[]
    for i in range(len(g1)):
        g3.append(g1[i]+g2[i])
    return g3

print(add_funct([3,9],[15,6]))


def add_multip_funct(g1, g2, m):
    for i in range(len(g1)):
        g1[i] *= m
        g2[i] *= m
    g3=[]
    for i in range(len(g1)):
        g3.append(g1[i]+g2[i])
    return g3

def subt(g1, g2, m):
    for i in range(len(g1)):
        g1[i] *= m
        g2[i] *= m
    g3=[]
    for i in range(len(g1)):
        g3.append(g1[i]+g2[i])
    return g3

def multip_funct(g, m):
    for i in range(len(g)):
        g[i] *= m
    return g
print(add_multip_funct(a,b,c))

print(multip_funct(a,c))



#problem 2


a = [1, 3]
b = [2, 6]
c = [-1, -3]
d = [1, -3]
e = [1, 2, 3]
f = [1, 2, 3, 4]

print(f"Norm {a} = {np.linalg.norm(a) } " )
print(f"Norm {b} = {np.linalg.norm(b) } " )
print(f"Norm {c} = {np.linalg.norm(c) } " )
print(f"Norm {d} = {np.linalg.norm(d) } " )
print(f"Norm {e} = {np.linalg.norm(e) } " )
print(f"Norm {f} = {np.linalg.norm(f) } " )