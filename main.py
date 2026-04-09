from qubit_model import create_qubit
from noise_channel import apply_noise
from measurement import state_to_density, expectation_value, Z
from adaptive_control import compute_correction_angle, apply_adaptive_correction
from planck_physics import compute_gamma
from visualization import plot_results
from ai_predictor import predict_k


def main():

    # USER INPUT
    temp = float(input("Enter temperature (Kelvin): "))
    freq = float(input("Enter qubit frequency (Hz): "))

    # Choose AI or manual feedback strength
    use_ai = input("Use AI to predict k? (y/n): ").lower()

    if use_ai == "y":
        k = predict_k(temp, freq)
        print(f"AI-predicted k: {k:.3f}")
    else:
        k = float(input("Enter feedback strength (k): "))

    # Step 1: Create qubit state
    psi = create_qubit()

    # Step 2: Convert to density matrix
    rho = state_to_density(psi)

    # Step 3: Compute thermal noise
    gamma = compute_gamma(freq, temp)

    # Step 4: Apply noise channel
    rho_noisy = apply_noise(rho, gamma)

    # Step 5: Measure expectation
    exp_before = expectation_value(rho_noisy, Z)

    # Step 6: Compute correction angle
    angle = compute_correction_angle(exp_before, k)

    # Step 7: Apply correction
    rho_corrected = apply_adaptive_correction(rho_noisy, angle)

    # Step 8: Measure after correction
    exp_after = expectation_value(rho_corrected, Z)

    # Print results
    print("\nResults:")
    print("Expectation before correction:", round(exp_before, 12))
    print("Expectation after correction:", round(exp_after, 12))

    improvement = exp_after - exp_before
    print("Improvement:", round(improvement, 12))

    # Step 9: Visualization
    plot_results(exp_before, exp_after)


if __name__ == "__main__":
    main()