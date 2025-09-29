# make_bar_chart.py
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Data (edit as needed) ---
data = pd.DataFrame({
    "Customer": ["A", "B", "C", "D"],
    "Revenue": [1200, 800, 950, 1500]
})

# --- Output folder ---
outdir = "assets/img"
os.makedirs(outdir, exist_ok=True)
outfile = os.path.join(outdir, "revenue_by_customer.png")

# --- Plot ---
sns.set_theme()  # simple, clean default styling
fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(x="Customer", y="Revenue", data=data, ax=ax)

ax.set_title("Revenue by Customer")
ax.set_xlabel("Customer")
ax.set_ylabel("Revenue")

# Optional: add value labels on bars (requires matplotlib ≥3.4)
try:
    ax.bar_label(ax.containers[0], fmt="%.0f", padding=3)
except Exception:
    # Fallback if bar_label isn't available
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width()/2, p.get_height(),
                f"{p.get_height():.0f}", ha="center", va="bottom")

fig.tight_layout()
fig.savefig(outfile, dpi=200, bbox_inches="tight")
plt.close(fig)

print(f"Saved chart to {outfile}")
