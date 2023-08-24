# Swarm Visualizer
This is a plotting visualizer packaged developed by UT Austin Swarm Lab. Please use these plotting package for all papers, plots in lab slides, etc. If you find errors or need a new utility, feel free to push new functions. 

## Usage
For example usage, see the code in the `tests` folder.

If you are a user:
```
pip install -e .
```

If you are a developer:
```
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip build
python -m pip install --editable ."[dev, test]"
```
Please make sure to write unit test for every method that you are developing.


Here's example import

```python
from swarm_visualizer.violinplot import plot_grouped_violinplot
from swarm_visualizer.boxplot import plot_grouped_boxplot
from swarm_visualizer.gridplot import plot_grid
```

