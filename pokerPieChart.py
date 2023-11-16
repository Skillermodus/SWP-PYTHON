import matplotlib.pyplot as plt

def createPieChart(warsch):
    ax = plt.subplot()
    ax.pie(list(warsch.values()), labels=list(warsch.keys()), autopct="%1.5f%%", radius=1.5)
    plt.show()