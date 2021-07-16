import argparse
import importlib

# Probably gonna cause issues if blanket importing everything. Rethink this.
from typing import *
import collections
import functools

# parser = argparse.ArgumentParser()
# parser.add_argument("--problem_num", "-p", type=str)

path = "0212_Word_Search_II"
solution = importlib.import_module(f"{path}", package=None)
print(solution)
print(solution.__dir__())
print(solution.__dict__)
print(solution.Solution)
