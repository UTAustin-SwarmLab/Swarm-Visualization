from statannotations.Annotator import Annotator



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
    
    annotator = Annotator(ax,box_pairs,data=df, x=x_var, y=y_var, hue = hue, order=order_list)
    annotator.configure(test=test_type, text_format=text_format, loc=loc, verbose=verbose, fontsize=fontsize)
    annotator.apply_and_annotate()
