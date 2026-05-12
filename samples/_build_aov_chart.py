"""
Mock AOV decomposition waterfall.
Recreates the visual structure of an internal year-over-year AOV decomposition
(MECE product-type buckets + Shapley split) using synthetic numbers, so it can
live on a public portfolio without exposing proprietary figures.

Run from repo root:
    python samples/_build_aov_chart.py
Outputs:
    samples/aov-decomposition.png
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Synthetic data: prior-year AOV, the YoY drivers, this-year AOV.
ly_total = 640
drivers = [
    ("Product\nprice/unit", 58),
    ("Underbedding\n$/order", 19),
    ("Service plan\n$/order", 9),
    ("Accessories\n$/order", 6),
    ("Units\nper order", 3),
]
ty_total = ly_total + sum(v for _, v in drivers)  # 735
swing = ty_total - ly_total  # 95

labels = ["LY Total"] + [d[0] for d in drivers] + ["TY Total"]
n = len(labels)

Y_MIN = 500  # zoomed baseline so the variance is legible

NAVY = "#1e3c72"
GREEN = "#2e8b57"
GREY = "#9aa5b1"

fig, ax = plt.subplots(figsize=(13, 7), dpi=140)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

x = range(n)
running = ly_total

# LY anchor (drawn from the zoomed baseline)
ax.bar(0, ly_total - Y_MIN, width=0.62, bottom=Y_MIN, color=NAVY, zorder=3)
ax.text(0, Y_MIN + (ly_total - Y_MIN) / 2, f"${ly_total}", ha="center", va="center",
        color="white", fontsize=15, fontweight="bold")

# Driver bars (floating)
for i, (name, val) in enumerate(drivers, start=1):
    bottom = running
    ax.bar(i, val, width=0.62, bottom=bottom, color=GREEN, zorder=3)
    ax.text(i, bottom + val + 4, f"+${val}", ha="center", va="bottom",
            color=GREEN, fontsize=13, fontweight="bold")
    # connector to next
    ax.plot([i - 0.31, i + 0.31 + (1 - 0.62)], [bottom + val, bottom + val],
            color=GREY, linestyle="--", linewidth=1, zorder=2)
    # connector from previous top
    ax.plot([i - 1 + 0.31, i - 0.31], [bottom, bottom],
            color=GREY, linestyle="--", linewidth=1, zorder=2)
    running += val

# TY anchor
ax.bar(n - 1, ty_total - Y_MIN, width=0.62, bottom=Y_MIN, color=NAVY, zorder=3)
ax.text(n - 1, Y_MIN + (ty_total - Y_MIN) / 2, f"${ty_total}", ha="center", va="center",
        color="white", fontsize=15, fontweight="bold")
# connector into TY total
ax.plot([n - 2 + 0.31, n - 1 - 0.31], [running, running],
        color=GREY, linestyle="--", linewidth=1, zorder=2)

# % of swing labels below axis
ax.set_xticks(list(x))
xt_labels = []
for i, lab in enumerate(labels):
    if 1 <= i <= len(drivers):
        pct = drivers[i - 1][1] / swing * 100
        xt_labels.append(f"{lab}\n({pct:.0f}% of swing)")
    else:
        xt_labels.append(lab)
ax.set_xticklabels(xt_labels, fontsize=10)

ax.set_ylim(Y_MIN, ty_total + 35)
ax.set_ylabel("Average Order Value ($)", fontsize=11, fontweight="500")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${int(v)}"))
ax.grid(True, axis="y", alpha=0.3, linestyle="--", zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)

ax.set_title(
    f"AOV Decomposition — YoY (illustrative)\n"
    f"${ly_total} → ${ty_total}   (+${swing} YoY, fully attributed to product-type drivers)",
    fontsize=14, fontweight="700", color="#111827", pad=14, loc="left")

# subtle methodology note
fig.text(0.5, -0.02,
         "MECE product-type buckets, additive (no overlap); core-product bucket decomposed via Shapley values "
         "(penetration × price-per-unit × units/order).  Synthetic figures.",
         ha="center", fontsize=8.5, color="#9aa5b1", style="italic")

plt.tight_layout()
plt.savefig("samples/aov-decomposition.png", dpi=140, bbox_inches="tight",
            facecolor="white")
print("Wrote samples/aov-decomposition.png")
