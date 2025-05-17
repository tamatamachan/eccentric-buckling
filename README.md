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

#main.py
import sympy as sp

# 材料特性
E1 = E2 = E3 = E4 = E5 = 205000
I1 = 12150
I2 = 48267
I3 = 36117
I5 = 271151
I4 = (I5 - I3) / 2

# 区間長さ・偏心量
L1, L2, L3, L4, L5 = 20, 140, 50, 120, 690
k = 7.7
P = sp.Symbol('P')
My = 412 * 2700

# 左端境界条件行列
R = sp.Matrix([
    [0, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# フィールドマトリクス関数
def F(L, E, I):
    return sp.Matrix([
        [1, -L, L**2/(2*E*I), L**3/(6*E*I), P*k*L**2/(2*E*L)],
        [0, 1, -L/(E*I), -L**2/(2*E*I), -P*k*L/(E*I)],
        [0, 0, 1, L, P*k],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ])

# 各区間
F1 = F(L1, E1, I1)
F2 = F(L2, E2, I2)
F3 = F(L3, E3, I3)
F4 = F(L4, E4, I4)
F5 = F(L5, E5, I5)

# 全体の伝達
Vr = F5 * F4 * F3 * F2 * F1 * R

# 右端の境界条件行列
RR = sp.Matrix([
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
])

# 条件式の生成
VrxRR = RR * Vr
Answer_M1 = VrxRR[0, 0]
Answer_1 = VrxRR[0, 2]

# 圧縮強度への変換係数
Coefficient = (Answer_M1 / Answer_1) * P

# 最終座屈荷重の計算
SOLVE = Coefficient * My
SOLVE_N = sp.N(SOLVE)
SOLVE_kN = SOLVE_N / 1000

# 結果出力
print("=== 計算結果 ===")
print("係数:", sp.N(Coefficient))
print("Pcr [N]:", round(SOLVE_N))
print("Pcr [kN]:", round(SOLVE_kN, 2))
