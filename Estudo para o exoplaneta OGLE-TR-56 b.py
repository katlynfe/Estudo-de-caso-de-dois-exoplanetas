#!/usr/bin/env python
# coding: utf-8

# In[1]:


''' Estudo para o exoplaneta OGLE-TR-56 b'''

''' Definição de alguns parâmetros'''
import numpy as np
import math

excentricidade = 0.67 
periodo_dias = 1.21191096
periodo_segundos = periodo_dias*86400
periodo_anos = periodo_dias/365.25
K_m_s = 313.0
K_km_s = K_m_s/1000
K_km_h = K_m_s*3.6
M_estrela_Msol = 1.228
M_estrela_kg = M_estrela_Msol*(1.989*10**30)
R_estrela_Rsol = 1.363
R_estrela_m = R_estrela_Rsol*695500000
Teff_estrela = 6050
Teff_sol = 5772
albedo_terra = 0.367
profundidade_transito_porcento = 1.080
profundidade_transito = profundidade_transito_porcento/100
inclinaçao = 1.21191096
G = (6.67408*10**(-11))


'''Definição de medidas'''

M_planeta_M_jupiter = ((4.919*(10**-3))*(K_m_s)*((1-(excentricidade**2))**(1/2))*((periodo_dias)**(1/3))*((M_estrela_Msol)**(2/3)))
print('Massa do planeta em relação à massa de Júpiter = ',M_planeta_M_jupiter)

M_planeta_M_terra = M_planeta_M_jupiter * ((1.898*10**27)/(5.972*10**24))#massa de Júpiter sobre a massa da Terra
print('Massa do planeta em função da Terra = ',M_planeta_M_terra)

M_planeta_kg = M_planeta_M_terra *(1.989*10**30)

semi_eixo_maior_m = ((((periodo_segundos**2)*G*(M_estrela_kg + (M_planeta_M_terra)))/(4*math.pi**2))**(1/3))
semi_eixo_maior_ua = semi_eixo_maior_m/(1.49*10**11)# para transformar em UA
print('Semi-eixo maior do planeta via Lei de Kepler = ',semi_eixo_maior_ua)

semi_eixo_maior_baricentro_m = (((periodo_segundos*(1-excentricidade**2)**(1/2))*K_m_s)/(2*math.pi))
semi_eixo_maior_baricentro_ua = semi_eixo_maior_baricentro_m/(1.49*10**11)
print('Semi-eixo maior do baricentro do sistema = ',semi_eixo_maior_baricentro_ua)

R_planeta_R_jupiter = ((profundidade_transito)**(1/2))*(9.94951)*(R_estrela_Rsol)#razao do raio do Sol sobre o raio de Júpiter
print('Raio do planeta em função de Júpiter = ',R_planeta_R_jupiter)

R_planeta_R_terra = R_planeta_R_jupiter * (69911/6371)#raio de Júpiter sobre o raio da Terra
print('Raio do planeta em função da Terra = ',R_planeta_R_terra)


Probabilidade_transito = ((R_estrela_m)/(semi_eixo_maior_m*(1-excentricidade**2)))*100
print('Probabilidade de trânsito porcento = ',Probabilidade_transito)

T_transito = ((periodo_dias*24)/math.pi)*math.asin((R_estrela_m/semi_eixo_maior_m)*((((1-(R_planeta_R_terra/R_estrela_m))**2)-(((semi_eixo_maior_m/R_estrela_m)*0.214735)**2))/(1-(0.214735**2)))**(1/2))
print('Tempo de trânsito do planeta = ',T_transito)

Grau_insolaçao = ((R_estrela_Rsol**2)*((Teff_estrela/Teff_sol)**4)*(1/semi_eixo_maior_ua**2))
print('Grau de insolação do planeta = ',Grau_insolaçao)

T_equilibrio = Teff_estrela*((1-0.367)**(1/4))*((R_estrela_m/(2*semi_eixo_maior_m))**(1/2))#0.367 é o albedo da Terra
print('Temperatura de equilíbrio do planeta = ',T_equilibrio)

Hab_zone_int = 0.75*(((R_estrela_Rsol**2)*((Teff_estrela/Teff_sol)**4))**2)
print('Zona habitável interna da estrela = ',Hab_zone_int)
Hab_zone_c = 1.00*(((R_estrela_Rsol**2)*((Teff_estrela/Teff_sol)**4))**2)
print('Zona habitável central da estrela = ',Hab_zone_c)
Hab_zone_ext = 1.77*(((R_estrela_Rsol**2)*((Teff_estrela/Teff_sol)**4))**2)
print('Zona habitável externa da estrela = ',Hab_zone_ext)


# In[ ]:




