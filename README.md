# Eccentric Buckling Analysis Using Transfer Matrix Method (TMM)

This repository contains a symbolic analysis of the critical buckling load for an eccentrically compressed steel member using the **Transfer Matrix Method (TMM)**. The computation is performed in Python with **SymPy** for symbolic mathematics.

## 📌 Overview

This project was developed as part of an undergraduate research thesis in structural engineering. The study focuses on modeling the buckling behavior of a multi-segment steel member with varying stiffness, including eccentricity at each segment.

The goal is to calculate the **critical buckling load (Pcr)** using a mathematical model, and compare it with **experimental results** to evaluate the validity of the theory.

## 📐 Methodology

- The steel column is divided into 5 segments with different flexural rigidities.
- Each segment is modeled with its own transfer matrix, incorporating eccentricity.
- Boundary conditions are applied at both ends.
- A symbolic formulation is used to compute the transformation from bending moment to axial load.

## 🔎 Key Features

- Symbolic computation using `sympy`
- Matrix-based modeling of eccentric buckling
- Experimental verification included
- Fully Python-based implementation

