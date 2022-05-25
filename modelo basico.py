# from calendar import c
from gurobipy import Model, GRB, quicksum
import random



random.seed(10)

t = 10
n = 8
c = 3

# rangos
C_ = range(c)

N_ = range(n)

T_ = range(t)


# Parametros

# Presupuesto de la municipalidad
P = 88300

# Plazo maximo para terminar la construccion de las obras
T = t

# Sueldo fijo diario para trabajador externo
S = 1300
# Costo de produccion de un metro de la ciclovia tipo c
K = [2000, 3000, 5000]  # Ciclovia tipo [0] cuesta 2000$ por unidad de largo

# Costo de produccion de senalizacion de ciclovia tipo c
G = [20, 30, 50]  # Senalizacion de ciclovia tipo [0] cuesta 20$

# Costo de mantencion por metro de ciclovia tipo c
D = [2000, 3000, 5000]  # Ciclovia tipo [0] cuesta 2000$ por unidad de largo
# Tiempo de construccion de la ciclovia tipo c
U = [1, 2, 3]

# Personal requerido para construir ciclovia tipo c
J = [2, 3, 4]

# Largo de la calle n
L = [1, 2, 3, 4, 5, 3, 4, 6]

# Cantidad de personas que utilizan la calle n
A = [50, 80, 12, 100, 60, 1000, 70, 500]

# Indice de accidentes que sufren bicicletas en la calle n
I = [0.8, 0.5, 0.9, 1.0, 0.6, 0.2, 0.6, 1]

# Existencia de ciclovia en la calle n
E = [0, 0, 0, 0, 1, 0, 0, 0]
 
# Personal disponible para trabajar en el dia t
O = [7, 7, 7, 7, 7, 5, 5, 7, 7, 7]

# Si en la calle n se puede construir
H = [[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1], [1, 1, 1], [0, 1, 1], [0, 1, 1], [0, 1, 1]]


# definmos un sub indice de [i,j,k] que son los que se meveran dentro de los indices, estos estan en orden [C_,N_,T_].
# Para evitar errores de codigo defini todos los parametros como mayusculas  y los sub indices como son i,j,k en minusculas.


m = Model("BICIStreckennetz")


# Variables
x = m.addVars(N_, C_, vtype=GRB.BINARY, name="x")
w = m.addVars(N_, C_, T_, vtype=GRB.BINARY, name="w")
z = m.addVars(T_, vtype=GRB.INTEGER, name="z")


m.update()


# R1
# m.addConstrs(sum(x[i,j,h,k] for i in N_) <= 1 for j in J_ for h in D_ for k in K_)
m.addConstrs(
    (quicksum(x[n, c] for c in C_) <= 1 - E[n] for n in N_),
    name="Una ciclovia por calle",
)

# R2
m.addConstr(
    (
        quicksum(z[t] * S for t in T_)
        + quicksum(x[n, c] * (L[n] * (D[c] + K[c]) + 2 * G[c]) for n in N_ for c in C_)
        <= P
    ),
    name="No superar el presupuesto",
)

# R3
m.addConstrs(
    (x[n, c] <= H[n][c] for n in N_ for c in C_), name="compatibilidad ciclovia-calle"
)

# R4
m.addConstrs(
    (quicksum(w[n, c, t] for t in T_) == x[n, c] * U[c] * L[n] for c in C_ for n in N_),
    name="Cumplir plazo",
)

# R5
m.addConstrs(
    (quicksum(w[n, c, t] * J[c] for n in N_ for c in C_) <= O[t] + z[t] for t in T_),
    name="Respetar personal maximo",
)

# R6
m.addConstrs(
    (w[n, c, t] <= x[n, c] for n in N_ for c in C_ for t in T_),
    name="Activacion/desactivacion variable W",
)


# Funcion Objetivo
m.setObjective(
    quicksum(x[n, c] * L[n] * I[n] * A[n] for n in N_ for c in C_), GRB.MAXIMIZE
)

# Imprimir Valor Objetivo
m.optimize()
print(f"\nEl valor objetivo es: {m.Objval}\n")
#################################

print("Ciclovias planeadas:\n")
for n_i in range(n):
    for c_i in range(c):
        if x[n_i, c_i].x != 0:
            print(f"En la calle {n_i + 1} se construira una ciclovia tipo {c_i + 1}")

print(f"Trabajores externos contratados en proyecto: {quicksum(z[t].x for t in T_ )}")


for t_i in range(t):
    trabajo_en_curso = quicksum(w[n, c, t_i] for n in N_ for c in C_)
    if float(str(trabajo_en_curso)[-5] + "." + str(trabajo_en_curso)[-3]) > 0:
        print(f"\n\nDia {t_i + 1}:\n")
        if z[t_i].x != 0:
            print(f"--Se contrataron {z[t_i].x} trabajadores extra--")
        for n_i in range(n):
            for c_i in range(c):
                if w[n_i, c_i, t_i].x != 0:
                    print(f"Se esta construyendo una ciclovia en la calle {n_i + 1}")


