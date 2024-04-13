import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Parâmetros fornecidos
L = 450  # cm
w_max = 1.75 * 10**3  # N/cm
E = 50 * 10**6  # N/cm^2
I = 30 * 10**3  # cm^4

# Passo a: Definição da função H(x)
def H(x):
    return (w_max * x**2) / (24 * E * I) * (L**3 - 2 * L * x**2 + x**3)

# Passo b: Plotando H(x) para encontrar x0
def plot_H():
    # Gerando valores de x
    x_values = np.linspace(0, L, 1000)
    # Calculando H(x) para os valores de x
    H_values = H(x_values)
    # Plotando H(x)
    plt.plot(x_values, H_values, label='H(x)')
    plt.title('Gráfico de H(x)')
    plt.xlabel('x (cm)')
    plt.ylabel('H(x)')
    plt.grid(True)
    plt.legend()
    plt.show()
    # Encontrando o valor aproximado de x onde H(x) é máximo
    x0 = x_values[np.argmax(H_values)]
    print("Valor aproximado de x onde H(x) é máximo:", x0)
    return x0, H_values

# Passo c: Encontrando o máximo de H(x) diretamente
result = minimize_scalar(lambda x: -H(x), bounds=(0, L), method='bounded')
x_max = result.x
max_deflection = -result.fun

print("Valor de x onde a deflexão é máxima:", x_max)
print("Valor máximo da deflexão:", max_deflection)

# Plotando o ponto onde a deflexão é máxima
x0, H_values = plot_H()
plt.scatter(x_max, H(x_max), color='red', label='Deflexão Máxima')
plt.legend()
plt.show()

# Plotando H(x) novamente com destaque no ponto x0
plt.plot(np.linspace(0, L, 1000), H_values, label='H(x)')
plt.scatter(x0, H(x0), color='green', label='Ponto de Deflexão Máxima')
plt.title('Gráfico de H(x) com Destaque no Ponto de Deflexão Máxima')
plt.xlabel('x (cm)')
plt.ylabel('H(x)')
plt.grid(True)
plt.legend()
plt.show()
