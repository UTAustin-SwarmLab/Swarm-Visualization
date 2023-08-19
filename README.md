# plotting_utils
Please use these plotting utilities for all papers, plots in lab slides, etc. If you find errors or need a new utility, feel free to push new functions. 

## Usage
For example usage, see the code in the `examples` folder.

The plotting utilities are in the `plotting_utils` folder, which is a Python package. To use the plotting utilities, you must add the `plotting_utils` folder to your `PYTHONPATH`. For example, if you are using a bash shell, you can add the following line to your `.bashrc` file:
```bash
export PYTHONPATH=$PYTHONPATH:/path/to/plotting_utils
```
where `/path/to/plotting_utils` is the path to the `plotting_utils` folder on your machine.
Then you can use the plotting utilities in your Python code as follows:
```python
from plotting_utils import *
```
