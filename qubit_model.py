import numpy as np

def create_qubit():
    """
    Create initial qubit state |ψ> = (|0> + |1>) / sqrt(2)
    """
    psi = np.array([[1/np.sqrt(2)],
                    [1/np.sqrt(2)]], dtype=complex)

    return psi