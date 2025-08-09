import matplotlib.pyplot as plt

# Data
age_groups = ['0-20 Years', '21-40 Years', '41-60 Years', '61+ Years']
population = [531, 473, 303, 161]  # in millions

# Figure size
plt.figure(figsize=(10, 6))

# Bar plot
plt.bar(age_groups, population, color=['yellow', 'blue', 'orange', 'gray'])

# Title and labels
plt.title("India's Population Distribution by Age Group (2022)", fontsize=14)
plt.xlabel("Age Group", fontsize=11)
plt.ylabel("Population (Millions)", fontsize=12)

# Annotating bars
for i, value in enumerate(population):
    plt.text(i, value + 5, f"{value}M", ha='center', fontsize=10)

# Grid lines
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout and show
plt.tight_layout()
plt.show()