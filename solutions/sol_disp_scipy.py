def disp(k, T=10, g=9.81, h=10):
    omega = 2*np.pi / T
    return omega**2  - g*k*np.tanh(k*h)

optimize.newton(disp, 0.07)