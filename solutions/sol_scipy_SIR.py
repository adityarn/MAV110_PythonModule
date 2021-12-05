from scipy.integrate import odeint

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = Sus0, Inf0, Rec0
# Integrate the SIR equations over the time grid, t.
t = np.arange(150)
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T


plt.plot(np.arange(150), S, label="Susceptible")
plt.plot(np.arange(150), R, label="Recovered")
plt.plot(np.arange(150), I, label="Infected")
plt.legend()