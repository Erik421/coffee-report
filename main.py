import argparse
import sys
from tabulate import tabulate

from reader import read_files
from reports import REPORTS


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+")
    parser.add_argument("--report")
    return parser.parse_args()


def main():
    args = parse_args()

    report = REPORTS.get(args.report)
    if not report:
        print(f"Unknown report: {args.report}")
        print(f"Available reports: {', '.join(REPORTS.keys())}")
        sys.exit(1)

    rows = read_files(args.files)
    table_data = report.build(rows)

    print(tabulate(
        table_data,
        headers=report.headers(),
        tablefmt="grid"
    ))


if __name__ == "__main__":
    main()