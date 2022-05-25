import pandas
import timeit

start = timeit.default_timer()


loop = True
ciclovias = []
calles = []
dias = 0

p_generales = pandas.read_excel(io="parametros.xlsx", sheet_name="Parametros generales")
p_ciclovias = pandas.read_excel(
    io="parametros.xlsx", sheet_name="Parametros de ciclovias"
)
p_calles = pandas.read_excel(io="parametros.xlsx", sheet_name="Parametros de calles")
p_tiempo = pandas.read_excel(io="parametros.xlsx", sheet_name="Parametros de tiempo")
p_cic_calle = pandas.read_excel(
    io="parametros.xlsx", sheet_name="Parametros de ciclovias y calle"
)

p_generales = p_generales.fillna(0)
p_ciclovias = p_ciclovias.fillna(0)
p_calles = p_calles.fillna(0)
p_tiempo = p_tiempo.fillna(0)
p_cic_calle = p_cic_calle.fillna(0)


# indices


def c_():
    ciclovias = int(p_ciclovias["c"].max())
    return ciclovias


def n_():
    calles = int(p_calles["n"].max())
    return calles


def t_():
    dias = int(p_tiempo["t"].max())
    return dias

#print(c_())
#print(n_())
#print(t_())

# parametros generales

def p_():
    presupuesto = p_generales["P"][1]
    return presupuesto

def s_():
    sueldo = p_generales["S"][1]
    return sueldo

#print(f"P: {p_()}")
#print(f"S: {s_()}")

# parametros relativos a las ciclovias:
def K_c():
    lista = []
    for c in range(c_()):
        lista.append(p_ciclovias["Kc [$/m]"][c])
    return lista

def G_c():
    lista = []
    for c in range(c_()):
        lista.append(p_ciclovias["Gc [$]"][c])
    return lista

def D_c():
    lista = []
    for c in range(c_()):
        lista.append(p_ciclovias["Dc [$/m]"][c])
    return lista

def U_c():
    lista = []
    for c in range(c_()):
        lista.append(p_ciclovias["Uc [dias/m]"][c])
    return lista

def J_c():
    lista = []
    for c in range(c_()):
        lista.append(p_ciclovias["Jc [personas]"][c])
    return lista


#print(p_calles["In"][3])

#print(f"K_c: {K_c()}")
#print(f"G_c: {G_c()}")
#print(f"D_c: {D_c()}")
#print(f"U_c: {U_c()}")
#print(f"J_c: {J_c()}")


# parametros relativos a las calles:

def E_n():
    lista = []
    for n in range(n_()):
        lista.append(p_calles["En"][n])
    return lista

def I_n():
    lista = []
    for n in range(n_()):
        lista.append(p_calles["In"][n])
    return lista

def L_n():
    lista = []
    for n in range(n_()):
        lista.append(p_calles["Ln"][n])
    return lista

def A_n():
    lista = []
    for n in range(n_()):
        lista.append(p_calles["An"][n])
    return lista

# print(f"E_n: {E_n()}")
# print(f"I_n: {I_n()}")
# print(f"L_n: {L_n()}")
# print(f"A_n: {A_n()}")


# parametros relativos al tiempo

def O_t():
    lista = []
    for t in range(t_()):
        lista.append(int(p_tiempo["Ot"][t]))
    return lista

#print(f"O_t: {O_t()}")

# Parámetros relativos a las ciclovias y las calles

def H_nc():
    lista = []
    for n in range(n_()):
        listita = []
        for c in range(c_()):
            listita.append(int(p_cic_calle[f"{c + 1}"][n]))
        lista.append(listita)
    return lista

#print(f"H_nc: {H_nc()}")

stop = timeit.default_timer()
print(f'Tiempo de carga de datos: {round(stop - start, 2)} s')  
