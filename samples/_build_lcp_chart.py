"""
Mock page-speed impact chart generator.
Recreates the visual structure of an internal Mobile TTFB impact slide using
the same data shape, so the visualization can live on a public portfolio
without exposing company branding or proprietary assets.

Run from repo root:
    python samples/_build_lcp_chart.py
Outputs:
    samples/page-speed-impact.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Mobile TTFB bucket data
buckets = list(range(1, 11))
ttfb_ms = [298, 731, 1254, 1724, 2219, 2721, 3225, 3728, 4231, 7300]
conv_rate = [0.75, 0.60, 0.63, 0.62, 0.61, 0.61, 0.61, 0.59, 0.56, 0.47]
aov = [565, 558, 552, 555, 560, 565, 565, 533, 520, 573]
# Session volume in millions (relative bar heights)
sessions = [2.6, 2.2, 1.5, 1.2, 0.9, 0.55, 0.45, 0.4, 0.35, 0.3]

# Aggregate session counts per zone (Good <800ms, Moderate 800-1800ms, Poor >1800ms)
good_label = '4.8M sessions (49.7%)'
moderate_label = '4.0M sessions (41.0%)'
poor_label = '896K sessions (9.2%)'

fig, ax1 = plt.subplots(figsize=(14, 6.5), dpi=140)
fig.patch.set_facecolor('white')
ax1.set_facecolor('white')

# Background zones for performance thresholds
ax1.axvspan(0.5, 2.5, facecolor='#86efac', alpha=0.30, zorder=0)   # Good <800ms (covers buckets 1-2)
ax1.axvspan(2.5, 5.5, facecolor='#fde68a', alpha=0.40, zorder=0)   # Moderate 800-1800ms (~ buckets 3-5)
ax1.axvspan(5.5, 10.5, facecolor='#fca5a5', alpha=0.30, zorder=0)  # Poor >1800ms (buckets 6-10)

# Session volume bars (gray, behind lines)
bars = ax1.bar(buckets, sessions, width=0.7, color='#9ca3af',
               alpha=0.55, label='Session Volume', zorder=1)

# Conversion rate line (green, primary axis)
line_conv = ax1.plot(buckets, conv_rate, color='#16a34a', linewidth=2.4,
                     marker='o', markersize=8, markerfacecolor='#16a34a',
                     markeredgecolor='white', markeredgewidth=1.5,
                     label='Conversion Rate (%)', zorder=4)

ax1.set_xlabel('TTFB Bucket', fontsize=11, fontweight='500', color='#1f2937')
ax1.set_ylabel('Conversion Rate (%)', fontsize=11, color='#16a34a',
               fontweight='500')
ax1.tick_params(axis='y', labelcolor='#16a34a')
ax1.set_ylim(0.4, 0.85)
ax1.set_xlim(0.5, 10.5)
ax1.set_xticks(buckets)
ax1.set_xticklabels([f'{b}\n({ms}ms)' for b, ms in zip(buckets, ttfb_ms)],
                    fontsize=9)
ax1.grid(True, axis='y', alpha=0.3, linestyle='--', zorder=0)
ax1.set_axisbelow(True)

# AOV on secondary axis (blue, dashed)
ax2 = ax1.twinx()
line_aov = ax2.plot(buckets, aov, color='#3b82f6', linewidth=1.8,
                    linestyle='--', marker='o', markersize=7,
                    markerfacecolor='#3b82f6', markeredgecolor='white',
                    markeredgewidth=1.2, label='AOV ($)', zorder=3)
ax2.set_ylabel('AOV ($)', fontsize=11, color='#3b82f6', fontweight='500')
ax2.tick_params(axis='y', labelcolor='#3b82f6')
ax2.set_ylim(500, 590)

# Vertical threshold marker (red dashed) between buckets 7 and 8
ax1.axvline(x=7.5, color='#dc2626', linestyle='--', linewidth=1.5,
            alpha=0.7, zorder=2)

# Session count annotations at the top of each zone
top_y = 0.825
ax1.text(1.5, top_y, good_label,
         ha='center', fontsize=10, fontweight='700', color='#15803d')
ax1.text(4.0, top_y, moderate_label,
         ha='center', fontsize=10, fontweight='700', color='#b45309')
ax1.text(8.0, top_y, poor_label,
         ha='center', fontsize=10, fontweight='700', color='#b91c1c')

# Title
ax1.set_title('Mobile Performance: Conversion Rate & AOV by Landing Page TTFB',
              fontsize=14, fontweight='700', color='#111827', pad=16)

# Legend (combined)
good_patch = mpatches.Patch(color='#86efac', alpha=0.5, label='Good (<800ms)')
mod_patch = mpatches.Patch(color='#fde68a', alpha=0.6,
                           label='Moderate (800-1800ms)')
poor_patch = mpatches.Patch(color='#fca5a5', alpha=0.6, label='Poor (>1800ms)')
legend_handles = [good_patch, mod_patch, poor_patch,
                  line_conv[0], bars, line_aov[0]]
ax1.legend(handles=legend_handles, loc='lower left', fontsize=9,
           framealpha=0.95, edgecolor='#d1d5db')

# Clean up spines
for spine in ['top']:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig('samples/page-speed-impact.png', dpi=140, bbox_inches='tight',
            facecolor='white')
print('Wrote samples/page-speed-impact.png')
