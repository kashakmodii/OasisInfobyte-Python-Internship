import matplotlib.pyplot as plt

def plot_bmi_history(dates, bmis, name):
    plt.figure(figsize=(6, 4))
    plt.plot(dates, bmis, marker='o', linestyle='-')
    plt.title(f"BMI Trend for {name}")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()