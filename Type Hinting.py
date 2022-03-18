from msilib import sequence
from typing import List

def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

# This will show up as an issue
# if you are using a linter
list_avg(123)
