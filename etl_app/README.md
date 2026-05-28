# ETL Application

A scalable Python ETL application scaffold with automated reporting generation.

## Structure

- `etl_app/config.py` - Configuration and environment loader.
- `etl_app/extract.py` - Data extraction utilities from CSV/JSON.
- `etl_app/transform.py` - Business rule and cleaning logic.
- `etl_app/load.py` - Data loading operations.
- `etl_app/reporting.py` - Report generation utilities.
- `etl_app/pipeline.py` - Orchestrates the ETL flow.
- `etl_app/cli.py` - Command-line entrypoint.
- `etl_app/utils.py` - Helper functions.
- `etl_app/tests/` - Basic unit test scaffold.

## Run

```bash
python -m etl_app.cli --run
```

## Notes

- Uses standard library only.
- Designed for easy extension into databases, APIs, and schedule-based automation.
