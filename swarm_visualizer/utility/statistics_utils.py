from statannot import add_stat_annotation


def add_wilcoxon_value(
    df=None,
    x_var=None,
    y_var=None,
    hue=None,
    order_list=None,
    ax=None,
    box_pairs=None,
    test_type=None,
    text_format=None,
    loc=None,
    fontsize=20,
    verbose=0,
) -> None:
    add_stat_annotation(
        ax,
        data=df,
        x=x_var,
        y=y_var,
        hue=hue,
        order=order_list,
        box_pairs=box_pairs,
        test=test_type,
        text_format=text_format,
        loc=loc,
        verbose=verbose,
        fontsize=fontsize,
    )
