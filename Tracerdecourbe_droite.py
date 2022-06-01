import matplotlib.pyplot as plt
def f(x):
    y=-7*x +3
    return y


X = [] #X contient la liste des abscisses
i=-5
j=5
for x in range (i,j+1):
    X.append(x)
Y = [] #Y contient la liste des ordonnées
for x in X:
    y=f(x)
    Y.append(y)
print(Y)

fig = plt.figure()                                                                                                                      
                                                                                                                                                
ax = plt.axes() 
ax.grid(True)      
ax.set_ylabel("ord")                                                                                                                      
ax.set_xlabel("abs") 
ax.set_title("Courbe d'équation -7x + 3")                                                                                                                     
                                                                                                                                                
ax.plot(X, Y) 
plt.show() 