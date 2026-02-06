#!/usr/bin/env python
"""
Download Seattle crime data from Seattle Open Data Portal.

This script downloads the SPD Crime Data using the Socrata API.
For larger datasets, consider downloading manually from the portal.

Usage:
    python scripts/download_data.py [--limit LIMIT] [--output OUTPUT]
"""

import argparse
import pandas as pd
from pathlib import Path
import sys
from datetime import datetime


def download_spd_crime_data(
    limit: int = 50000,
    output_path: str = "data/raw/spd_crime_data.csv"
) -> None:
    """
    Download SPD Crime Data from Seattle Open Data Portal.

    Parameters
    ----------
    limit : int, default 50000
        Maximum number of records to download
    output_path : str
        Path to save the downloaded data
    """
    print("=" * 60)
    print("Seattle Crime Data Downloader")
    print("=" * 60)
    print(f"\nData Source: Seattle Open Data Portal")
    print(f"Dataset: SPD Crime Data: 2008-Present")
    print(f"API: Socrata SODA API")
    print(f"\nDownload Settings:")
    print(f"  - Record Limit: {limit:,}")
    print(f"  - Output Path: {output_path}")
    print("\n" + "-" * 60)

    # Create output directory if it doesn't exist
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Construct API URL
    base_url = "https://data.seattle.gov/resource/tazs-3rd5.csv"
    url = f"{base_url}?$limit={limit}"

    print(f"\nDownloading data from: {base_url}")
    print(f"This may take a few minutes...\n")

    try:
        # Download data
        df = pd.read_csv(url)

        print(f"✅ Download successful!")
        print(f"\nDataset Summary:")
        print(f"  - Records downloaded: {len(df):,}")
        print(f"  - Columns: {len(df.columns)}")
        print(f"  - Memory size: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

        # Save to file
        print(f"\nSaving to: {output_path}")
        df.to_csv(output_path, index=False)
        print(f"✅ Data saved successfully!")

        # Display column names
        print(f"\nColumns in dataset:")
        for i, col in enumerate(df.columns, 1):
            print(f"  {i:2d}. {col}")

        # Display date range if available
        date_cols = [col for col in df.columns if 'date' in col.lower()]
        if date_cols:
            date_col = date_cols[0]
            df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
            print(f"\nDate Range:")
            print(f"  - Start: {df[date_col].min()}")
            print(f"  - End: {df[date_col].max()}")

        print("\n" + "=" * 60)
        print("Download Complete!")
        print("=" * 60)
        print(f"\nNext Steps:")
        print(f"  1. Review the data: data/README.md")
        print(f"  2. Start analysis: notebooks/exploratory/01_initial_data_exploration.ipynb")
        print(f"  3. Follow setup guide: SETUP.md")

    except Exception as e:
        print(f"❌ Error downloading data: {e}")
        print(f"\nTroubleshooting:")
        print(f"  1. Check your internet connection")
        print(f"  2. Verify the API endpoint is accessible")
        print(f"  3. Try reducing the limit (current: {limit})")
        print(f"  4. Download manually: https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5")
        sys.exit(1)


def main():
    """Parse arguments and run the download."""
    parser = argparse.ArgumentParser(
        description="Download Seattle crime data from Open Data Portal"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50000,
        help="Maximum number of records to download (default: 50000)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/raw/spd_crime_data.csv",
        help="Output file path (default: data/raw/spd_crime_data.csv)"
    )

    args = parser.parse_args()

    download_spd_crime_data(
        limit=args.limit,
        output_path=args.output
    )


if __name__ == "__main__":
    main()
