import numpy as np

def compute_correction_angle(exp_val, k):
    """
    Compute rotation angle for adaptive feedback.

    exp_val : measured expectation value <Z>
    k       : feedback strength

    Negative feedback stabilizes the qubit by rotating
    it opposite to the measured deviation.
    """
    angle = -k * exp_val
    return float(angle)


def apply_adaptive_correction(rho, angle):
    """
    Apply a rotation around the Y-axis to stabilize the qubit.

    rho   : density matrix
    angle : rotation angle computed from feedback
    """

    # Y-axis rotation matrix
    R = np.array([
        [np.cos(angle/2), -np.sin(angle/2)],
        [np.sin(angle/2),  np.cos(angle/2)]
    ], dtype=complex)

    # Apply correction
    rho_corrected = R @ rho @ R.conj().T

    # Normalize density matrix
    rho_corrected /= np.trace(rho_corrected)

    return rho_corrected