# from calendar import c
from gurobipy import Model, GRB, quicksum
from datos import K_c, G_c, D_c, U_c, J_c, L_n, A_n, I_n, E_n, O_t, H_nc, p_, t_, s_, n_, c_
import timeit

start = timeit.default_timer()


t = int(t_())
n = int(n_())
c = int(c_())

# rangos
#C_ = range(c)
C_ = range(int(c_()))

#N_ = range(n)
N_ =range(int(n_()))

#T_ = range(t)
T_= range(int(t_()))


# Parametros

# Presupuesto de la municipalidad
# P = 88300
P=p_()

# Plazo maximo para terminar la construccion de las obras
#T = t
T=t_()

# Sueldo fijo diario para trabajador externo
#S = 130000000
S = s_()

# Costo de produccion de un metro de la ciclovia tipo c
#K = [2000, 3000, 5000]  # Ciclovia tipo [0] cuesta 0.002$ por km
K = K_c()

# Costo de produccion de senalizacion de ciclovia tipo c
#G = [20, 30, 50]  # Senalizacion de ciclovia tipo [0] cuesta 20$
G = G_c()

# Costo de mantencion por metro de ciclovia tipo c
#D = [2000, 3000, 5000]  # Ciclovia tipo [0] cuesta 0.002$ por km
D = D_c()

# Tiempo de construccion de la ciclovia tipo c
#U = [1, 2, 3]
U = U_c()

# Personal requerido para construir ciclovia tipo c
#J = [2, 3, 4]
J = J_c()

# Largo de la calle n en metros
#L = [1, 2, 3, 4, 5, 3]
L = L_n()

# Cantidad de personas que utilizan la calle n
#A = [50, 80, 12, 100, 60, 1000]
A = A_n()

# Indice de accidentes que sufren bicicletas en la calle n
#I = [0.8, 0.5, 0.9, 1.0, 0.6, 0.2]
I = I_n()

# Existencia de ciclovia en la calle n
#E = [0, 0, 0, 0, 0, 0]
E = E_n()
 
# Personal disponible para trabajar en el dia t
# O = []
# for i in range(t):
#     O.append(7)
O = O_t()


# Si en la calle n se puede construir
#H = [[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1], [1, 1, 1], [0, 1, 1]]
H = H_nc()


# definmos un sub indice de [i,j,k] que son los que se meveran dentro de los indices, estos estan en orden [C_,N_,T_].
# Para evitar errores de codigo defini todos los parametros como mayusculas  y los sub indices como son i,j,k en minusculas.


m = Model("BICIStreckennetz")
m.setParam("TimeLimit", 1800)


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
    (quicksum(w[n, c, t] for t in T_) == x[n, c] * round(U[c] * L[n]) for c in C_ for n in N_),
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

m.addConstrs((z[t] <= O[t] for t in T_), name = "grupos equitativos de trabajadores")


# Funcion Objetivo
m.setObjective(
    quicksum(x[n, c] * L[n] * I[n] * A[n] for n in N_ for c in C_), GRB.MAXIMIZE
)

# Imprimir Valor Objetivo
m.optimize()

# print("\n"+"-"*9+" Restricciones Activas "+"-"*9)
# for constr in m.getConstrs():
#     if constr.getAttr("slack") == 0:
#         print(f"La restriccion {constr} est?? activa")


print(f"\nEl valor objetivo es: {m.Objval}\n")
#################################
calles = 0
log = ""
largo = 0
log += ("Ciclovias planeadas:\n\n")
for n_i in range(n):
    for c_i in range(c):
        if x[n_i, c_i].x != 0:
            log += (f"En la calle {n_i + 1} se construira una ciclovia tipo {c_i + 1}\n")
            calles += 1
            largo += L[n_i]

log += (f"\nSe construyen {calles} ciclovias en total.\n")
log += (f"Se construyen {round(largo/1000, 3)} km de ciclovias en total.\n")
log += (f"Trabajores externos contratados en proyecto: {quicksum(z[t].x for t in T_ )}")

print(log)

dinero_restante = P
dias_sin_trabajar = 0
spam = False

option = input("Quieres mostrar el itnerario diario? (s/n):\n")
if option.lower() in "si":
    spam = True

for t_i in range(t):
    dia = (f"\n\n\nDia {t_i + 1}:\n")
    if spam:
        print(dia)
    log += dia
    flojeando = True
    dinero_gastado = 0
    if z[t_i].x != 0:
        trabajadores = (f"Se contrataron {z[t_i].x} trabajadores extra\n")
        if spam:
            print(trabajadores)
        log += trabajadores
        dinero_restante -= z[t_i].x*S
        dinero_gastado +=z[t_i].x*S
    for n_i in range(n):
        for c_i in range(c):
            if w[n_i, c_i, t_i].x != 0:
                construccion = (f"Se esta construyendo una ciclovia en la calle {n_i + 1}\n")
                if spam:
                    print(construccion)
                log += construccion
                dinero_gastado += ((L[n_i] * (D[c_i] + K[c_i]) + 2 * G[c_i])/(L[n_i]*U[c_i]))
                dinero_restante -= ((L[n_i] * (D[c_i] + K[c_i]) + 2 * G[c_i])/(L[n_i]*U[c_i]))
                flojeando = False
    if flojeando:
        dias_sin_trabajar += 1
    presupuesto = (f"Presupuesto utilizado: {round(dinero_gastado)}\n")
    if spam:
        print(presupuesto)
    log += presupuesto
    if t_i == 179:
        dinero_restante = round(dinero_restante)
        print(f"Dinero restante: {dinero_restante}\n\n")
    log += (f"Dinero restante: {dinero_restante}\n\n")

log += (f"\nHubo {dias_sin_trabajar} dias en los que no se construyeron ciclovias")
print(f"\nHubo {dias_sin_trabajar} dias en los que no se construyeron ciclovias")
log += (f"--Itinerario diario--\n{log}")

file = open("resultados.txt", "w")
file.write(log)
file.close()

stop = timeit.default_timer()
print(f'Tiempo de ejecucion del modelo:  {round(stop - start, 2)} s')  

