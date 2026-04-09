import numpy as np
import pandas as pd

from qubit_model import create_qubit
from measurement import state_to_density, expectation_value, Z
from noise_channel import apply_noise
from adaptive_control import compute_correction_angle, apply_adaptive_correction
from planck_physics import thermal_occupation

# Define ranges for training
temps = [0.015, 0.1, 1, 4, 300]   # cryogenic → room temp
freqs = [5e9, 20e9, 4e14]         # microwave → optical
k_values = np.arange(0.1, 5.1, 0.1)

data = []

for T in temps:
    for f in freqs:

        # Thermal occupation
        n = thermal_occupation(f, T)
        gamma = 0.05 * n

        for k in k_values:

            # Step 1: initial qubit
            psi = create_qubit()
            rho = state_to_density(psi)

            # Step 2: apply noise
            noisy_rho = apply_noise(rho, gamma)

            # Step 3: expectation before correction
            exp_before = expectation_value(noisy_rho, Z)

            # Step 4: compute correction angle
            angle = compute_correction_angle(exp_before, k)

            # Step 5: apply correction
            corrected_rho = apply_adaptive_correction(noisy_rho, angle)

            # Step 6: expectation after correction
            exp_after = expectation_value(corrected_rho, Z)

            improvement = exp_after - exp_before

            data.append([T, f, k, improvement])

df = pd.DataFrame(data, columns=["temp","freq","k","improvement"])

df.to_csv("training_data.csv", index=False)

print("Training data generated and saved to training_data.csv")