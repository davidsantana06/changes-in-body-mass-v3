from app.classes.person import Person
from app.shared_constants import ROUND_LIM
from matplotlib import pyplot as plt
from typing import List
import seaborn as sns


START_INTERV, END_INTERV = 88, 103
COLOR = {
    'dark': '#212529',
    'green': '#7BC74D',
    'tertiary': '#909294',
    'red': '#FF5A5F',
    'yellow': '#FFC952',
    'white': '#FFFFFF'
}
FD_TITLE = {'family': 'sans-serif', 'weight': 'light', 'size': 12}
FD_AXIS = {'family': 'sans-serif', 'weight': 'ultralight', 'style': 'italic', 'size': 10}
FD_WEIGHT = {'family': 'sans-serif', 'weight': 'semibold', 'size': 8}

def show_chart(decrypted_mw: List[Person]):
    '''
    ### Função (Extra)
    Gera um gráfico de barras com a relação entre o peso atual das pessoas do mini-mundo.
    '''

    # Definir a cor das barras e a média de pesagens
    axis = {'x': [], 'y': []}
    colors = []
    weight_sum = 0

    for person in decrypted_mw:
        id = person.get_id()
        weight = person.get_current_weight()
        weight_sum += weight

        axis['x'].append(weight)
        axis['y'].append(str(id))

        color = COLOR['green'] if weight <= START_INTERV else COLOR['yellow'] if weight <= END_INTERV else COLOR['red']
        colors.append(color)

    weight_avg = round(weight_sum / len(decrypted_mw), ROUND_LIM)


    # Compor a figura com todos os dados extraídos
    plt.figure('Changes in Body Mass V3')
    sns.set_style('dark')
    ax = sns.barplot(x=axis['x'], y=axis['y'], palette=colors)
    ax.axvline(x=weight_avg, color=COLOR['tertiary'], linestyle=':', alpha=0.7, zorder=0)

    plt.title('RELAÇÃO DE PESO ATUAL', fontdict=FD_TITLE, pad=10)
    plt.xlabel('Peso (Kg)', fontdict=FD_AXIS, labelpad=15)
    plt.ylabel('Pessoa (ID)', fontdict=FD_AXIS, labelpad=15)
    plt.subplots_adjust(left=0.155, bottom=0.18, right=0.855, top=0.838)


    # Adicionar o valor do peso à cada barra na figura
    for idx, weight in enumerate(axis['x']):
        ax.text(
            10, (idx + 0.04), str(weight),
            color=COLOR['white'],
            ha='center',
            va='center',
            fontdict=FD_WEIGHT
        )


    # Exibir o gráfico
    plt.show()
