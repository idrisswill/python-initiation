import matplotlib.pyplot as plt
import numpy as np
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


def get_plot_args(digs):
    """Selects the correct arguments for the plotting functions, depending on the
    the test (digs) chosen.
    """
    if digs in [1, 2, 3]:
        text_x = False
        n, m = 10 ** (digs - 1), 10 ** (digs)
        x = np.arange(n, m)
        figsize = (2 * (digs ** 2 + 5), 1.5 * (digs ** 2 + 5))
    elif digs == 22:
        text_x = False
        x = np.arange(10)
        figsize = (14, 10)
    else:
        text_x = True
        x = np.arange(100)
        figsize = (15, 7)
    return x, figsize, text_x


def plot_digs( x, y_Exp, y_Found, N, figsize, conf_Z, text_x=False,
              save_plot=None, save_plot_kwargs=None):
    """Plots the digits tests results

    Args:
        x: sequence to be used in the x axis
        y_Exp: sequence of the expected proportions to be used in the y axis
            (line)
        y_Found: sequence of the found proportions to be used in the y axis
            (bars)
        N: lenght of sequence, to be used when plotting the confidence levels
        figsize: tuple to state the size of the plot figure
        conf_Z: Confidence level
        save_pic: file path to save figure
        text_x: Forces to show all x ticks labels. Defaluts to True.
        save_plot: string with the path/name of the file in which the generated
            plot will be saved. Uses matplotlib.pyplot.savefig(). File format
            is infered by the file name extension.
        save_plot_kwargs: dict with any of the kwargs accepted by
            matplotlib.pyplot.savefig()
            https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html

    """
    if len(x) > 10:
        rotation = 90
    else:
        rotation = 0
    fig, ax = plt.subplots(figsize=figsize)
    plt.title('Expected vs. Found Distributions', size='xx-large')
    plt.xlabel('Digits', size='x-large')
    plt.ylabel('Distribution (%)', size='x-large')
    if conf_Z is not None:
        sig = conf_Z * np.sqrt(y_Exp * (1 - y_Exp) / N)
        upper = y_Exp + sig + (1 / (2 * N))
        lower_zeros = np.array([0] * len(upper))
        lower = np.maximum(y_Exp - sig - (1 / (2 * N)), lower_zeros)
        u = (y_Found < lower) | (y_Found > upper)
        c = np.array([COLORS['m']] * len(u))
        c[u] = COLORS['af']
        lower *= 100.
        upper *= 100.
        ax.plot(x, upper, color=COLORS['s'], zorder=5)
        ax.plot(x, lower, color=COLORS['s'], zorder=5)
        ax.fill_between(x, upper, lower, color=COLORS['s'],
                        alpha=.3, label='Conf')
    else:
        c = COLORS['m']
    ax.bar(x, y_Found * 100., color=c, label='Found', zorder=3, align='center')
    ax.plot(x, y_Exp * 100., color=COLORS['s'], linewidth=2.5,
            label='Benford', zorder=4)
    ax.set_xticks(x)
    ax.set_xticklabels(x, rotation=rotation)
    ax.set_facecolor(COLORS['b'])
    # if text_x:
    #     ind = np.array(df.index).astype(str)
    #     ind[:10] = np.array(['00', '01', '02', '03', '04', '05',
    #                       '06', '07', '08', '09'])
    #     plt.xticks(x, ind, rotation='vertical')
    ax.legend()
    ax.set_ylim(0, max([y_Exp.max() * 100, y_Found.max() * 100]) + 10 / len(x))
    ax.set_xlim(x[0] - 1, x[-1] + 1)

    if save_plot:
        if not save_plot_kwargs:
            save_plot_kwargs = {}
        plt.savefig(save_plot, **save_plot_kwargs)

    plt.show(block=False)