import numpy as np

# Physical constants
h = 6.626e-34   # Planck constant (J·s)
kB = 1.381e-23  # Boltzmann constant (J/K)

def thermal_occupation(freq, temp):
    """
    Bose-Einstein distribution: average thermal occupation number.
    """

    # Prevent division by zero
    if temp <= 0:
        return 0

    x = (h * freq) / (kB * temp)

    # Avoid overflow in exp
    if x > 700:
        return 0

    return 1 / (np.exp(x) - 1)


def compute_gamma(freq, temp):
    """
    Noise strength proportional to thermal occupation.
    """
    n = thermal_occupation(freq, temp)

    gamma = 0.05 * n

    # Prevent gamma > 1
    gamma = min(gamma, 0.9)

    return gamma