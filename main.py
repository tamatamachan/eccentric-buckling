import sympy as sp

# Material properties
E1 = E2 = E3 = E4 = E5 = 205000  # Young's modulus [N/mm^2]
I1 = 12150                      # Second moment of area [mm^4]
I2 = 48267
I3 = 36117
I5 = 271151
I4 = (I5 - I3) / 2

# Segment lengths [mm]
L1, L2, L3, L4, L5 = 20, 140, 50, 120, 690
eccentricity = 7.7             # Eccentricity [mm]
P = sp.Symbol('P')             # Load symbol
My = 412 * 2700                # Yield bending moment [N·mm]

# Boundary matrix (left end)
R = sp.Matrix([
    [0, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Field transfer matrix function
def F(L, E, I):
    return sp.Matrix([
        [1, -L, L**2/(2*E*I), L**3/(6*E*I), P*eccentricity*L**2/(2*E*L)],
        [0,  1, -L/(E*I), -L**2/(2*E*I), -P*eccentricity*L/(E*I)],
        [0,  0, 1, L, P*eccentricity],
        [0,  0, 0, 1, 0],
        [0,  0, 0, 0, 1]
    ])

# Transfer matrices for each segment
F1 = F(L1, E1, I1)
F2 = F(L2, E2, I2)
F3 = F(L3, E3, I3)
F4 = F(L4, E4, I4)
F5 = F(L5, E5, I5)

# Full transfer from left to right
Vr = F5 * F4 * F3 * F2 * F1 * R

# Boundary matrix (right end)
RR = sp.Matrix([
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
])

# Extract key terms from boundary condition equation
VrxRR = RR * Vr
Answer_M1 = VrxRR[0, 0]
Answer_1 = VrxRR[0, 2]

# Conversion coefficient from moment to load
Coefficient = (Answer_M1 / Answer_1) * P

# Solve for critical buckling load
Pcr_expression = Coefficient * My
Pcr_value = sp.N(Pcr_expression)
Pcr_kN = Pcr_value / 1000

# Output
print("=== Eccentric Buckling Result ===")
print("Conversion Coefficient:", sp.N(Coefficient))
print("Pcr [N]:", round(Pcr_value))
print("Pcr [kN]:", round(Pcr_kN, 2))
