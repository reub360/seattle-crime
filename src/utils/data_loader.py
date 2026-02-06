"""
Data loading utilities for Seattle crime data.

This module provides functions to load, validate, and prepare
crime data from various sources.
"""

import pandas as pd
import geopandas as gpd
from pathlib import Path
from typing import Optional, Union, Dict, Any
import warnings


def load_crime_data(
    file_path: Union[str, Path],
    parse_dates: bool = True,
    validate: bool = True,
) -> pd.DataFrame:
    """
    Load Seattle crime data from CSV file.

    Parameters
    ----------
    file_path : str or Path
        Path to the crime data CSV file
    parse_dates : bool, default True
        Whether to parse date columns automatically
    validate : bool, default True
        Whether to run basic validation checks

    Returns
    -------
    pd.DataFrame
        Loaded crime data

    Examples
    --------
    >>> df = load_crime_data('data/raw/spd_crime_data.csv')
    >>> print(f"Loaded {len(df)} records")
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    # Load data
    df = pd.read_csv(file_path)

    # Parse dates if requested
    if parse_dates:
        date_columns = [col for col in df.columns
                       if 'date' in col.lower() or 'time' in col.lower()]
        for col in date_columns:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except Exception as e:
                warnings.warn(f"Could not parse dates in column {col}: {e}")

    # Validate if requested
    if validate:
        _validate_crime_data(df)

    return df


def load_geospatial_data(
    file_path: Union[str, Path],
    crs: str = "EPSG:4326"
) -> gpd.GeoDataFrame:
    """
    Load geospatial data (neighborhoods, precincts, etc.).

    Parameters
    ----------
    file_path : str or Path
        Path to the geospatial file (GeoJSON, Shapefile, etc.)
    crs : str, default "EPSG:4326"
        Coordinate reference system

    Returns
    -------
    gpd.GeoDataFrame
        Loaded geospatial data
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Geospatial file not found: {file_path}")

    gdf = gpd.read_file(file_path)

    # Ensure consistent CRS
    if gdf.crs is None:
        gdf.set_crs(crs, inplace=True)
    elif gdf.crs != crs:
        gdf = gdf.to_crs(crs)

    return gdf


def _validate_crime_data(df: pd.DataFrame) -> None:
    """
    Run basic validation checks on crime data.

    Parameters
    ----------
    df : pd.DataFrame
        Crime data to validate
    """
    # Check for required columns (adjust based on actual data)
    expected_columns = ['latitude', 'longitude']  # Minimum expected

    # Check for coordinates
    coord_cols = [col for col in df.columns
                  if 'lat' in col.lower() or 'lon' in col.lower()]

    if len(coord_cols) < 2:
        warnings.warn("Missing coordinate columns. Spatial analysis may not be possible.")

    # Check for date columns
    date_cols = [col for col in df.columns
                 if 'date' in col.lower() or 'time' in col.lower()]

    if len(date_cols) == 0:
        warnings.warn("No date/time columns found. Temporal analysis may not be possible.")

    # Check for extreme missing values
    missing_pct = (df.isnull().sum() / len(df) * 100)
    critical_missing = missing_pct[missing_pct > 50]

    if len(critical_missing) > 0:
        warnings.warn(f"Columns with >50% missing data: {list(critical_missing.index)}")


def get_data_info(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Get summary information about the crime dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Crime data

    Returns
    -------
    dict
        Dictionary with dataset information
    """
    info = {
        'total_records': len(df),
        'total_columns': len(df.columns),
        'memory_mb': df.memory_usage(deep=True).sum() / 1024**2,
        'duplicates': df.duplicated().sum(),
        'missing_values': df.isnull().sum().sum(),
        'columns_with_missing': (df.isnull().sum() > 0).sum(),
    }

    # Add date range if date columns exist
    date_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]
    if date_cols:
        date_col = date_cols[0]
        info['date_range_start'] = df[date_col].min()
        info['date_range_end'] = df[date_col].max()

    return info


def validate_coordinates(
    df: pd.DataFrame,
    lat_col: str = 'latitude',
    lon_col: str = 'longitude',
    lat_range: tuple = (47.4, 47.8),
    lon_range: tuple = (-122.5, -122.2)
) -> pd.DataFrame:
    """
    Validate and filter coordinates to Seattle bounds.

    Parameters
    ----------
    df : pd.DataFrame
        Crime data with coordinates
    lat_col : str
        Name of latitude column
    lon_col : str
        Name of longitude column
    lat_range : tuple
        Valid latitude range (min, max)
    lon_range : tuple
        Valid longitude range (min, max)

    Returns
    -------
    pd.DataFrame
        Data with validated coordinates
    """
    if lat_col not in df.columns or lon_col not in df.columns:
        raise ValueError(f"Columns {lat_col} and/or {lon_col} not found in data")

    # Count invalid coordinates
    invalid_lat = ~df[lat_col].between(lat_range[0], lat_range[1])
    invalid_lon = ~df[lon_col].between(lon_range[0], lon_range[1])
    invalid_count = (invalid_lat | invalid_lon).sum()

    if invalid_count > 0:
        warnings.warn(
            f"Found {invalid_count} records with coordinates outside Seattle bounds. "
            f"These will be set to NaN."
        )
        df.loc[invalid_lat | invalid_lon, [lat_col, lon_col]] = None

    return df
