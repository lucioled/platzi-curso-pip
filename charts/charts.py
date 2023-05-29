import matplotlib.pyplot as plt

<<<<<<< HEAD
def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
=======

def generate_pie_chart():
    labels = ['LULA', 'PINZA', 'BUENA']
    values = [23, 2, 44]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('grafico.png')
    plt.close()
>>>>>>> 5c96ef8a03ff6c86659b813c4b712c355214085d
