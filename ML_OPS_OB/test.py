#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:14:02 2024

@author: estebanjimenez
"""

import pickle
import pandas as pd



# Cargar modelo

# Cargar modelo
with open("/Users/estebanjimenez/Library/CloudStorage/OneDrive-Personal/Tec_Monterrey/Maestria_Aya/MLOPS/ML_OPS_OB/ML_OPS_OB/pages/best_model_reduced.pkl", "rb") as f:
    model = pickle.load(f)

# Imprimir modelo cargado
print("Modelo cargado:", model)