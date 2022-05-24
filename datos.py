import pandas
loop = True
ciclovias = []
calles = []
dias = 0

p_generales = pandas.read_excel(io = "parametros.xlsx", sheet_name = "Parametros generales")
p_ciclovias = pandas.read_excel(io = "parametros.xlsx", sheet_name = "Parametros de ciclovias")
p_calles    = pandas.read_excel(io = "parametros.xlsx", sheet_name = "Parametros de calles")
p_tiempo    = pandas.read_excel(io = "parametros.xlsx", sheet_name = "Parametros de tiempo")
p_cic_calle = pandas.read_excel(io = "parametros.xlsx", sheet_name = "Parametros de ciclovias y calle")

# indices

def c_():
    ciclovias = p_ciclovias["c"].max()
    return ciclovias

print(c_())

# while loop:
#     nueva_ciclovia = input("\nIngrese tipo de ciclovía:\n")
#     if nueva_ciclovia != "x" and nueva_ciclovia != "X":
#         ciclovias.append(nueva_ciclovia)
#     else:
#         loop = False

# loop = True
# index  = 1
# while loop:
#     nueva_calle = input(f"\nApodo de calle {index}:\n")
#     if nueva_calle != "x" and nueva_calle != "X":
#         calles.append(nueva_calle)
#         index += 1
#     else:
#         loop = False

# dias = int(input("\nDuracion del proyecto en dias:\n"))

# # parametros generales

# P = int(input("\nPresupuesto de la municipalidad:\n"))
# T = dias
# S = int(input("\nSueldo de trabajador externo:\n"))


# # parametros relativos a las ciclovias:

# K_c = []
# for i in range(len(ciclovias)):
#     k_nuevo = int(input(f"\nCosto de produccion de ciclovia tipo {i + 1} ({ciclovias[i]}):\n"))
#     K_c.append(k_nuevo)

# G_c = []
# for i in range(len(ciclovias)):
#     g_nuevo = int(input(f"\nCosto de produccion de señalizacion de ciclovia tipo {i + 1} ({ciclovias[i]}):\n"))
#     G_c.append(g_nuevo)

# D_c = []
# for i in range(len(ciclovias)):
#     d_nuevo = int(input(f"\nCosto de mantencion de ciclovia tipo {i + 1} ({ciclovias[i]}):\n"))
#     D_c.append(d_nuevo)

# U_c = []
# for i in range(len(ciclovias)):
#     u_nuevo = int(input(f"\nTiempo de produccion por metro de ciclovia tipo {i + 1} ({ciclovias[i]}):\n"))
#     U_c.append(u_nuevo)

# J_c = []
# for i in range(len(ciclovias)):
#     j_nuevo = int(input(f"\nCantidad de personal requerido para construir un metro de ciclovía {i + 1} ({ciclovias[i]}):\n"))
#     J_c.append(j_nuevo)


# # parametros relativos a las calles:

# L_n = []
# for i in range(len(calles)):
#     l_nuevo = int(input(f"\nLargo de la calle {i + 1} ({calles[i]}):\n"))
#     L_n.append(l_nuevo)

# A_n = []
# for i in range(len(calles)):
#     a_nuevo = int(input(f"\nCantidad de personas que ocupan la calle {i + 1} ({calles[i]}):\n"))
#     A_n.append(a_nuevo)

# I_n = []
# for i in range(len(calles)):
#     i_nuevo = float(input(f"\nIndice de accidentes sufridos por bicicletas en la calle {i + 1} ({calles[i]}):\n"))
#     I_n.append(i_nuevo)

# E_n = []
# for i in range(len(calles)):
#     loop = True
#     while loop:
#         e_nuevo = input(f"\n¿Existe ciclovía en la calle {i + 1} ({calles[i]})? (s/n):\n")
#         if e_nuevo.lower() in "si":
#             E_n.append(1)
#             loop = False
#         elif e_nuevo.lower() in "no":
#             E_n.append(0)
#             loop = False
#         else:
#             print("La respuesta ingresada no es válida, por favor vuelva a intentar\n")

# # parametros relativos al tiempo

# O_t = []
# for i in range(dias):
#     o_nuevo = int(input(f"\nPersonal máximo disponible en el dia {i + 1}:\n"))
#     O_t.append(o_nuevo)

# # Parámetros relativos a las ciclovias y las calles

# loop = True

# H_nc = []
# for n in range(len(calles)):
#     while loop:
#         for c in range(len(calles)):
#             loop = True
#             h_nuevo = input(f"\n¿Se puede construir la ciclovía tipo {c + 1} ({ciclovias[c]}) en la calle {n + 1} ({calles[n]})? (s/n):\n")
#             if h_nuevo.lower() in "si":
#                 H_nc.append(1)
#                 loop = False
#             elif h_nuevo.lower() in "no":
#                 H_nc.append(0)
#                 loop = False
#             else:
#                 print("La respuesta ingresada no es válida, por favor vuelva a intentar\n")

# # prints varios
# print(f"largo lista ciclovias: {len(ciclovias)}")
# print(f"largo lista calles: {len(calles)}")
# print(f"rango lista ciclovias: {range(len(ciclovias))}")
# print(f"rango lista calles: {range(len(calles))}")

# for i in range(len(ciclovias)):
#     print(f"ciclovia numero {i}")

# for i in range(len(calles)):
#     print(f"calle numero {i}")

