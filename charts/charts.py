import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['LULA', 'PINZA', 'BUENA']
    values = [23, 2, 44]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('grafico.png')
    plt.close()
