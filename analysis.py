import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Quarterly MRR growth data (%)
    data = {
        "Quarter": ["Q1", "Q2", "Q3", "Q4"],
        "MRR_Growth": [8.22, 5.11, 12.48, 7.10],
    }
    df = pd.DataFrame(data)

    # Calculate average
    avg_growth = df["MRR_Growth"].mean()

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df["Quarter"], df["MRR_Growth"])

    # Reference lines
    industry_target = 15.0
    ax.axhline(industry_target, linestyle="--", linewidth=1.5, label=f"Industry Target ({industry_target}%)")
    ax.axhline(avg_growth, linestyle=":", linewidth=1.5, label=f"Average ({avg_growth:.2f}%)")

    # Labels & title
    ax.set_title("Quarterly MRR Growth vs. Target", pad=12)
    ax.set_xlabel("Quarter")
    ax.set_ylabel("MRR Growth (%)")
    ax.set_ylim(0, max(industry_target, df["MRR_Growth"].max()) * 1.15)
    ax.grid(axis="y", alpha=0.3)
    ax.legend()

    # Annotate bars with values
    for i, v in enumerate(df["MRR_Growth"]):
        ax.text(i, v + max(0.3, v * 0.02), f"{v:.2f}%", ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig("performance_chart.png", dpi=300)

    # Print the average for convenience when running the script
    print(f"Average MRR Growth: {avg_growth:.2f}%")

if __name__ == "__main__":
    main()
