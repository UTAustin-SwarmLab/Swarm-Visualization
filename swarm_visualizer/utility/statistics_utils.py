from statannotations.Annotator import Annotator


def add_wilcoxon_value(
    ax,
    df=None,
    x_var=None,
    y_var=None,
    hue=None,
    order_list=None,
    box_pairs=None,
    test_type="Wilcoxon",
    text_format="full",
    loc=None,
    fontsize=20,
    verbose=0,
    pvalue_format_string="{:.4f}",
    show_test_name=False,
    **kwargs
) -> None:
    annotator = Annotator(
        ax, box_pairs, data=df, x=x_var, y=y_var, hue=hue, order=order_list
    )
    annotator.configure(
        test=test_type,
        text_format=text_format,
        loc=loc,
        verbose=verbose,
        fontsize=fontsize,
        pvalue_format_string=pvalue_format_string,
        show_test_name=show_test_name,
      **kwargs
    )
    annotator.apply_and_annotate()
