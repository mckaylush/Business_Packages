# generate_charts.py
import os
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt

# ---- Data ----
X = np.array([[1200, 40],
              [800, 25],
              [950, 30],
              [1500, 60]])

# ---- Scaling ----
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

minmax = MinMaxScaler()
X_minmax = minmax.fit_transform(X)

# ---- Output folder ----
outdir = "assets/img"
os.makedirs(outdir, exist_ok=True)

# ---- Combined figure (3 panels) ----
fig, axes = plt.subplots(1, 3, figsize=(12, 4), constrained_layout=True)

axes[0].scatter(X[:, 0], X[:, 1])
axes[0].set_title("Raw")
axes[0].set_xlabel("Revenue")
axes[0].set_ylabel("Customers")

axes[1].scatter(X_standardized[:, 0], X_standardized[:, 1])
axes[1].set_title("StandardScaler (z-score)")
axes[1].set_xlabel("Revenue (z)")
axes[1].set_ylabel("Customers (z)")

axes[2].scatter(X_minmax[:, 0], X_minmax[:, 1])
axes[2].set_title("MinMaxScaler (0–1)")
axes[2].set_xlabel("Revenue (0–1)")
axes[2].set_ylabel("Customers (0–1)")

fig.suptitle("Scaling Comparison: Raw vs StandardScaler vs MinMaxScaler", fontsize=12)
combined_path = os.path.join(outdir, "scaling_comparison.png")
fig.savefig(combined_path, dpi=200)
plt.close(fig)

# ---- Separate images (one per plot) ----
def save_scatter(data, title, xlab, ylab, fname):
    plt.figure(figsize=(4, 3))
    plt.scatter(data[:, 0], data[:, 1])
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, fname), dpi=200)
    plt.close()

save_scatter(X, "Revenue vs Customers (Raw)", "Revenue", "Customers", "scatter_raw.png")
save_scatter(X_standardized, "Revenue vs Customers (Standardized)", "Revenue (z-score)", "Customers (z-score)", "scatter_standardized.png")
save_scatter(X_minmax, "Revenue vs Customers (MinMax 0–1)", "Revenue (0–1)", "Customers (0–1)", "scatter_minmax.png")

# Optional: also print arrays for your post
print("Standardized:\n", X_standardized)
print("\nMinMax Scaled:\n", X_minmax)
print("\nSaved images to:", outdir)
