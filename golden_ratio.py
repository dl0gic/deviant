#!/usr/bin/env python3

import math

# Calculate the Golden Mean Ratio (Phi)
phi = (1 + math.sqrt(5)) / 2

# Multiply numbers from 1 to 100 by Phi and print the results
for i in range(1, 101):
    result = i * phi
    print(f"{i} * {phi:.6f} = {result:.6f}")