import numpy as np

# Pauli Z operator
Z = np.array([
    [1, 0],
    [0, -1]
], dtype=complex)


def state_to_density(state):
    """
    Convert pure state vector |ψ> to density matrix ρ = |ψ><ψ|
    """
    return state @ state.conj().T


def measurement_probabilities(rho):
    """
    Return probabilities of measuring |0> and |1>
    """
    p0 = np.real(rho[0, 0])
    p1 = np.real(rho[1, 1])

    return float(p0), float(p1)


def expectation_value(rho, operator):
    """
    Compute expectation value <O> = Tr(ρO)
    """
    return float(np.real(np.trace(rho @ operator)))