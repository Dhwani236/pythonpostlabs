# a: z transform of 3^nu[n]
import sympy as sp
# Define symbols
n, z= sp.symbols('n z')
# Define the signal x[n] = 3^n * u[n]
x_n = 3**n
# Compute the Z-transform
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# Print the result
print("Z-transform of x[n] = 3^n u[n]:")
sp.pprint(X_z, use_unicode=True)


#b : z transform of cos(omega n)u[n]
n, z, omega = sp.symbols('n z omega')
# Define the sinusoidal sequence x[n] = cos(omega * n) * u[n]
x_n = sp.cos(omega * n)
# Compute the Z-transform
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# Print the result
print("Z-transform of x[n] = cos(omega * n) u[n]:")
sp.pprint(X_z, use_unicode=True)
