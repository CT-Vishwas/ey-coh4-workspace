import argparse
import sys

from .config import load_config
from .pipeline import run_etl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the scalable ETL pipeline and reporting automation.")
    parser.add_argument("--config", dest="config_path", help="Optional path to load configuration from.")
    parser.add_argument("--run", action="store_true", help="Execute the ETL pipeline.")
    parser.add_argument("--report-only", action="store_true", help="Generate report from the current destination data.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config(args.config_path)

    if args.run:
        result = run_etl(config)
        print("ETL completed:", result)
        return 0
    if args.report_only:
        print("Report-only mode is not yet implemented.")
        return 0

    print("No action specified. Use --run to execute ETL.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
