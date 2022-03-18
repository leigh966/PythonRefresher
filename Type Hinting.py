from msilib import sequence
from typing import List

# Takes a parameter sequence that is a list and returns a float
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

# This will show up as an issue
# if you are using a linter
list_avg(123)
