import numpy as np

def apply_noise(rho, gamma):
    """
    Apply simple thermal decoherence channel.
    gamma controls noise strength.
    """

    noise_matrix = np.array([
        [1, 0],
        [0, 1 - gamma]
    ], dtype=complex)

    rho_noisy = noise_matrix @ rho @ noise_matrix.conj().T

    # Normalize density matrix
    rho_noisy = rho_noisy / np.trace(rho_noisy)

    return rho_noisy