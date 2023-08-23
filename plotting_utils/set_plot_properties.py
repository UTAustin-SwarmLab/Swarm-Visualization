import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pylab as pylab


def set_plot_properties(
    font_size: float = 20,
    legend_font_size: float = 14,
    xtick_label_size: float = 14,
    ytick_label_size: float = 14,
    markersize: float = 10,
) -> None:
    """
    Sets plot properties
    :param font_size: font size
    :param legend_font_size: legend font size
    :param xtick_label_size: xtick label size
    :param ytick_label_size: ytick label size
    :return: None
    """

    sns.set_color_codes()
    sns.set()

    plt.rc("text", usetex=True)
    font = {"family": "normal", "weight": "bold", "size": font_size}
    plt.rc("font", **font)
    plt.rcParams["text.latex.preamble"] = r"\boldmath"

    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["font.weight"] = "bold"

    params = {
        "legend.fontsize": legend_font_size,
        "axes.labelsize": font_size,
        "axes.titlesize": font_size,
        "xtick.labelsize": xtick_label_size,
        "ytick.labelsize": ytick_label_size,
        "lines.markersize": markersize,
        "figure.autolayout": True,
    }

    pylab.rcParams.update(params)

    sns.set_style(style="darkgrid")
