"""
Use this script for running any common code to initialize a Jupyter Notebook

To include this script in any notebook simply run the following:

    %run nb_init.py
"""

# sys path workaround for importing sibling packages like "common" in our case
import sys

sys.path.insert(0, "..")
