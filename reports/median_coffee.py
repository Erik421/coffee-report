from collections import defaultdict
from statistics import median
from typing import List, Dict

from .base import BaseReport


class MedianCoffeeReport(BaseReport):
    name = "median-coffee"

    def build(self, rows: List[Dict]) -> List[List]:
        grouped = defaultdict(list)

        for row in rows:
            student = row["student"]
            coffee_spent = float(row["coffee_spent"])
            grouped[student].append(coffee_spent)

        result = []

        for student, values in grouped.items():
            med = median(values)
            result.append([student, med])

        result.sort(key=lambda x: x[1], reverse=True)

        return result

    def headers(self) -> List[str]:
        return ["student", "median_coffee"]