import matplotlib.pyplot as plt
import numpy as np

# Sample data
names = ['S. binderi', 'P. pavonica', 'P. tetrastromatica', 'H. clathratus', 'D. dichotoma']
Molecular_Weight = [0.44, 0.24, 0.52, 0.16, 0.31]
Intrinsic_Viscosity = [93, 51, 111, 35, 66]

# Assign numerical values to names
name_values = np.arange(len(names))

# Create the 2D graph
fig, ax = plt.subplots()

# Plot the data
colors = ['red', 'yellow', 'green', 'blue', 'purple']
ax.plot(Molecular_Weight, Intrinsic_Viscosity, marker='o', markersize=8, linestyle='-', color='lightgray', linewidth=4, alpha=0.5)
for i in range(len(names)):
    ax.plot(Molecular_Weight[i], Intrinsic_Viscosity[i], marker='o', markersize=8, linestyle='', color=colors[i])

# Set axis labels
ax.set_xlabel('Molecular Weight (Mw) X $10^5$', fontsize=12, fontname='Georgia')
ax.set_ylabel('Intrinsic Viscosity ([η])', fontsize=12, fontname='Georgia')

# Set plot style and layout
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.tick_params(width=1.5)
fig.set_facecolor('white')

# Add legend with names and markers
legend_handles = [plt.Line2D([], [], marker='o', linestyle='', color=color, markersize=8) for color in colors]
legend_labels = ax.legend(legend_handles, [f'$\it{{{name}}}$' for name in names], loc='lower right', fontsize=8, frameon=False)
for text in legend_labels.get_texts():
    text.set_fontsize(12)
    text.set_fontname('Georgia')

# Show the plot
plt.tight_layout()
plt.show()
