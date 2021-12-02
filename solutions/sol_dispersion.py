T = 10.
omega = 2*np.pi / T
g = 9.81
h = 10

k_0 = 2*np.pi/100
k_n = k_0

for i in range(10):
    k_n = omega**2 / (g * np.tanh(k_n*h))
    print(i, k_n)