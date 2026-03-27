import csv
from typing import List, Dict


def read_files(paths: List[str]) -> List[Dict]:
    rows: List[Dict] = []

    for path in paths:
        with open(path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)

    return rows