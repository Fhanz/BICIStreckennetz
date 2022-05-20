from calendar import c
from pyexpat import model
from re import T
from gurobipy import Model,GRB,quicksum

import random

random.seed(10)

t = 360
n = 12
C = 5

#rangos
C_ = range(1, c + 1)
N_ = range(1, n + 1)
T_ = range(1, t + 1)


#Parametros 
#G = {(i): random.randint(15000, 40000) for i in N_} , como definir los parametros 
# definmos un sub indice de [i,j,k] que son los que se meveran dentro de los indices, estos estan en orden [C_,N_,T_].
# Para evitar errores de codigo defini todos los parametros como mayusculas  y los sub indices como son i,j,k en minusculas.




#### ESCRIBA SU MODELO AQUI ####
m = Model()

#Variables
x = m.addVars(N_,C_, vtype = GRB.BINARY,name="x" )
w = m.addVars(N_,C_,T_, vtype=GRB.BINARY, name="w")
z = m.addVars(T_,vtype=GRB.BINARY, name="z")


m.update()



#R1
#m.addConstrs(sum(x[i,j,h,k] for i in N_) <= 1 for j in J_ for h in D_ for k in K_)
m.addConstrs(sum(x[i,j] for i in C_) <= 1 - E[j]  for j in N_)

#R2
m.addConstrs(sum(z[ñ]*S for ñ in T_ )+ sum(x[i,j]*(L[j]*(D[i]+K[i]+2*G[i])) for i in C_ for j in N_) <= P )

#R3
m.addConstrs(x[i,j] <= H[i,j] for i in C_ for j in N_)

#R4
m.addConstrs(sum(w[k,i,j] for k in T_ ) <= x[i,j]*L[j]*U[i] for i in C_ for j in N_  )

#no esta tomando el signo de igualdad asi que lo voy a hacer en dos uno de >= y otro de <=
m.addConstrs(sum(w[k,i,j] for k in T_ ) >= x[i,j]*L[j]*U[i] for i in C_ for j in N_  )


#R5
m.addConstrs(sum (w[i,j,k]*J[i] for i in C_ for j in N_) <= O[ñ]+z[ñ] for k in T_ )

#R6
m.addConstrs( w[i,j,ñ] <= x[i,j] for i in C_ for j in N_ for ñ in T_)

# falta definir las naturaleza de las variables, pero en el de la tarea no esta definido  asi que nose si se hace 



#Función Objetivo
m.setObjective(sum(x[i,j]*l[j]*I[j]*a[j] for i in C_ for j in N_), GRB.MAXIMIZE)

#Imprimir Valor Objetivo
m.optimize()
print(m.Objval())
#################################








