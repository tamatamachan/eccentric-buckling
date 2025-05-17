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
