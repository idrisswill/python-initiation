import matplotlib.pyplot as plt

COLORS = {'m': '#00798c', 'b': '#E2DCD8', 's': '#9c3848',
          'af': '#edae49', 'ab': '#33658a', 'h': '#d1495b',
          'h2': '#f64740', 't': '#16DB93'}

def plot_expected( prob, digits, digs):
    if digs in [1, 2, 3]:
        y_max = (prob.max() + (10 ** -(digs) / 3)) * 100
        figsize = 2 * (digs ** 2 + 5), 1.5 * (digs ** 2 + 5)
    fig, ax = plt.subplots(figsize=figsize)
    plt.title('Expected Benford Distributions', size='xx-large')
    plt.xlabel('digits', size='x-large')
    plt.ylabel('Distribution (%)', size='x-large')
    ax.set_facecolor(COLORS['b'])
    ax.set_ylim(0, y_max)
    ax.bar(digits, prob * 100, color=COLORS['t'], align='center')
    ax.set_xticks(digits)
    ax.set_xticklabels(digits)

    plt.show(block=False)