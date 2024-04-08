import numpy as np
import matplotlib.pyplot as plt

# Parâmetros fornecidos
L = 450  # cm
w_max = 1.75 * 10**3  # N/cm
E = 50 * 10**6  # N/cm^2
I = 30 * 10**3  # cm^4

# Passo a: Definição da função H(x)
def H(x):
    return 15 * x**4 - 30 * L**2 * x**2 - 7 * L**4

# Passo b: Plotando H(x) para encontrar x0
def plot_H():
    # Gerando valores de x
    x_values = np.linspace(0, L, 1000)
    # Calculando H(x) para os valores de x
    H_values = H(x_values)
    # Plotando H(x)
    plt.plot(x_values, H_values)
    plt.title('Gráfico de H(x)')
    plt.xlabel('x (cm)')
    plt.ylabel('H(x)')
    plt.grid(True)
    plt.show()
    # Encontrando o valor aproximado de x onde H(x) é máximo
    x0 = x_values[np.argmax(H_values)]
    print("Valor aproximado de x onde H(x) é máximo:", x0)
    return x0

# Passo c: Implementação do método de Newton
def newton_method(f, f_prime, x0, tolerance=1e-9, max_iterations=1000):
    x = x0
    iteration = 0
    while abs(f(x)) > tolerance and iteration < max_iterations:
        x = x - f(x) / f_prime(x)
        iteration += 1
    if iteration == max_iterations:
        print("O método de Newton não convergiu após", max_iterations, "iterações.")
        return None
    else:
        return x

# Definindo a derivada de H(x)
def H_prime(x):
    return 60 * x**3 - 60 * L**2 * x

# Executando os passos a, b e c
x0 = plot_H()
x_max = newton_method(H, H_prime, x0)
print("Valor de x onde a deflexão é máxima:", x_max)
