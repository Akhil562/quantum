import matplotlib.pyplot as plt

def plot_results(exp_before, exp_after):

    labels = ["Before Correction", "After Correction"]
    values = [exp_before, exp_after]

    plt.figure(figsize=(6,4))
    plt.bar(labels, values)

    plt.title("Qubit Expectation Value Stabilization")
    plt.ylabel("<Z> Expectation Value")

    # Show values with 12 decimal places
    for i, v in enumerate(values):
        plt.text(i, v, f"{v:.12f}", ha='center', va='bottom')

    # Auto zoom scale
    center = (exp_before + exp_after) / 2
    margin = abs(exp_before - exp_after) * 5

    if margin == 0:
        margin = 1e-6

    plt.ylim(center - margin, center + margin)

    plt.grid(axis='y', linestyle='--', alpha=0.6)

    plt.show()