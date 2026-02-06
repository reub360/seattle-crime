# Scripts Directory

This directory contains utility scripts for data acquisition and project setup.

## Available Scripts

### download_data.py

Downloads Seattle crime data from the Seattle Open Data Portal using the Socrata API.

**Usage:**
```bash
# Download 50,000 records (default)
python scripts/download_data.py

# Download custom number of records
python scripts/download_data.py --limit 100000

# Specify custom output path
python scripts/download_data.py --output data/raw/custom_name.csv
```

**Options:**
- `--limit`: Maximum number of records to download (default: 50000)
- `--output`: Output file path (default: data/raw/spd_crime_data.csv)

**Note:** For downloading the complete dataset (millions of records), it's recommended to use the manual download option from the Seattle Open Data Portal website.

## Future Scripts

Planned scripts for future implementation:

- `download_census_data.py` - Download census data for Seattle neighborhoods
- `download_weather_data.py` - Download historical weather data
- `download_transit_data.py` - Download King County Metro transit data
- `setup_environment.py` - Automated environment setup
- `validate_data.py` - Comprehensive data validation

## Contributing

When adding new scripts:
1. Include clear docstrings
2. Add command-line argument parsing
3. Provide helpful error messages
4. Update this README
5. Add usage examples

---

**Last Updated**: 2026-02-06
