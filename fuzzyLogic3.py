import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')             
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan') 
kecepatan = ctrl.Consequent(np.arange(0, 101, 1), 'kecepatan')   

suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['panas'] = fuzz.trimf(suhu.universe, [30, 40, 40])
kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 45])
kelembapan['normal'] = fuzz.trimf(kelembapan.universe, [35, 50, 75])
kelembapan['lembap'] = fuzz.trimf(kelembapan.universe, [65, 100, 100])
kecepatan['lambat'] = fuzz.trimf(kecepatan.universe, [0, 0, 40])
kecepatan['sedang'] = fuzz.trimf(kecepatan.universe, [30, 50, 70])
kecepatan['cepat'] = fuzz.trimf(kecepatan.universe, [60, 100, 100])

rule1 = ctrl.Rule(suhu['dingin'] & kelembapan['kering'], kecepatan['lambat'])
rule2 = ctrl.Rule(suhu['dingin'] & kelembapan['lembap'], kecepatan['lambat'])
rule3 = ctrl.Rule(suhu['normal'] & kelembapan['normal'], kecepatan['sedang'])
rule4 = ctrl.Rule(suhu['panas'] & kelembapan['kering'], kecepatan['sedang'])
rule5 = ctrl.Rule(suhu['panas'] & kelembapan['lembap'], kecepatan['cepat'])

kipas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
kipas_sim = ctrl.ControlSystemSimulation(kipas_ctrl)
suhu_input = 32.0
kelembapan_input = 80.0

kipas_sim.input['suhu'] = suhu_input
kipas_sim.input['kelembapan'] = kelembapan_input

kipas_sim.compute()

print("--- HASIL INFERENSI LOGIKA FUZZY ---")
print(f"Suhu Lingkungan : {suhu_input} °C")
print(f"Kelembapan      : {kelembapan_input} %")
print(f"Kecepatan Kipas : {kipas_sim.output['kecepatan']:.2f} %")

kecepatan.view(sim=kipas_sim)    
plt.show()