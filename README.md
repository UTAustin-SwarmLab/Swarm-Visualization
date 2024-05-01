# Swarm Visualization
This is a plotting visualizer packaged developed by UT Austin Swarm Lab. Please use these plotting package for all papers, plots in lab slides, etc. If you find errors or need a new utility, feel free to create pull request for new features.

## Usage
For example usage, see the code in the `tests` folder. If you want to see example plots, run `pytest` in your terminal. All example plots will be available in `tests/example_plots`


If you are a user:
```
Option 1:
pip install git+https://github.com/UTAustin-SwarmLab/Swarm-Visualization

Option 2:
pip install -e .
```

## Development
If you are a developer:
```
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip build
python -m pip install --editable ."[dev, test]"
```
Please make sure to write unit tests for every method that you are developing.

Here's an example code to import functions from the package:

```python
from swarm_visualizer import plot_grouped_violinplot
from swarm_visualizer import plot_grouped_boxplot
from swarm_visualizer import plot_grid
```

