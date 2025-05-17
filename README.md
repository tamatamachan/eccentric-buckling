# eccentric-buckling
Buckling analysis of eccentric compression members using the Transfer Matrix Method, implemented in Python.
# Eccentric Compression Buckling Analysis with Transfer Matrix Method

This repository contains a Python-based implementation of buckling analysis for eccentrically compressed steel members using the **Transfer Matrix Method (TMM)**.

## Overview

This code was developed as part of my undergraduate thesis at Okayama University of Science, focusing on the buckling behavior of eccentric steel pipe members in a spatial truss system.  
The entire mathematical model—including eccentricity, initial conditions, and stiffness distribution—was implemented from scratch in Python.

## Features

- 5-element transfer matrix model
- Boundary condition matrix formulation
- Critical buckling load (Pcr) calculation
- Editable parameters (E, I, L, e, M, etc.)

## Example Output

```python
Pcr = 125.34 kN

## Sample code
# main.py
# Eccentric buckling analysis using Transfer Matrix Method (TMM)

# ライブラリのインポート
import numpy as np
import sympy as sp

# 材料ヤング率 [N/mm^2]
E1, E2, E3, E4, E5 = 210000, 205000, 125000, 205000, 205000

# 断面2次モーメント [mm^4]
I1, I2, I3, I5 = 12150, 48267, 361177, 271151
I4 = (I5 - I3) / 2

# 部材長さ [mm]
l1, l2, l3, l4, l5 = 20, 140, 50, 120, 690
total_length = l1 + l2 + l3 + l4 + l5

# 偏心量 [mm]
k = 7.7

# 結果出力
print("== パラメータ ==")
print(f"E1-E5: {E1}, {E2}, {E3}, {E4}, {E5} [N/mm^2]")
print(f"I1-I5: {I1}, {I2}, {I3}, {I4}, {I5} [mm^4]")
print(f"L1-L5: {l1}, {l2}, {l3}, {l4}, {l5} [mm]")
print(f"Total Length: {total_length} mm")
print(f"Eccentricity: {k} mm")



