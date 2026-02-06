# Data Documentation

This directory contains raw and processed datasets for the Seattle crime analysis project.

## Directory Structure

```
data/
├── raw/            # Original, immutable datasets (not version controlled)
├── processed/      # Cleaned and transformed datasets (not version controlled)
└── README.md       # This file
```

## Data Sources

### Core Dataset

#### 1. Seattle Police Department Crime Data
- **Source**: [Seattle Open Data Portal](https://data.seattle.gov)
- **Dataset**: SPD Crime Data: 2008-Present
- **Direct Link**: https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5
- **Update Frequency**: Daily
- **Format**: CSV, JSON
- **Fields**:
  - Report Number
  - Offense ID
  - Offense Start DateTime
  - Offense End DateTime
  - Report DateTime
  - Group A B (Crime classification)
  - Crime Against Category
  - Offense Parent Group
  - Offense
  - Offense Code
  - Precinct
  - Sector
  - Beat
  - MCPP (Micro Community Policing Plan area)
  - Longitude
  - Latitude
- **Storage**: `data/raw/spd_crime_data.csv`

### Supplemental Datasets

#### 2. Geospatial Boundaries
- **Source**: [Seattle Open Data Portal](https://data.seattle.gov)
- **Datasets**:
  - Seattle Neighborhoods: https://data.seattle.gov/dataset/Neighborhoods/2mbt-aqqx
  - Seattle Police Precincts: https://data.seattle.gov/dataset/Police-Precincts/kzun-tx4j
  - Parks and Recreation: https://data.seattle.gov/Parks-and-Recreation/Parks/3vrk-67bw
- **Format**: GeoJSON, Shapefile
- **Storage**: `data/raw/geospatial/`

#### 3. Seattle 911 Call Data (Computer Aided Dispatch)
- **Source**: [Seattle Open Data Portal](https://data.seattle.gov)
- **Dataset**: Seattle Real Time Fire 911 Calls
- **Direct Link**: https://data.seattle.gov/Public-Safety/Seattle-Real-Time-Fire-911-Calls/kzjm-xkqj
- **Format**: CSV, JSON
- **Storage**: `data/raw/seattle_911_calls.csv`

### Contextual Datasets

#### 4. U.S. Census Data
- **Source**: [U.S. Census Bureau](https://data.census.gov)
- **API**: Census API
- **Data Tables**:
  - ACS 5-Year Estimates (American Community Survey)
  - Demographic and Housing Estimates
  - Income and Poverty
  - Employment Status
- **Geographic Level**: Census Tract, Block Group
- **Storage**: `data/raw/census/`

#### 5. Weather Data
- **Source**: [NOAA National Centers for Environmental Information](https://www.ncei.noaa.gov)
- **Station**: Seattle-Tacoma International Airport (GHCND:USW00024233)
- **Variables**: Temperature, Precipitation, Conditions
- **Format**: CSV
- **Storage**: `data/raw/weather/`

#### 6. Public Transit Locations
- **Source**: [King County Metro](https://kingcounty.gov/en/dept/metro)
- **Datasets**:
  - Metro Bus Stops
  - Light Rail Stations
  - Transit Routes
- **Format**: GeoJSON, Shapefile
- **Storage**: `data/raw/transit/`

## Download Instructions

### Seattle Police Department Crime Data
```bash
# Manual download from Seattle Open Data Portal
# Or use Socrata API:
curl "https://data.seattle.gov/resource/tazs-3rd5.csv?$limit=50000" -o data/raw/spd_crime_data.csv
```

### Geospatial Boundaries
```bash
# Download via Seattle Open Data Portal
# Neighborhoods, Police Precincts, Parks available in multiple formats
```

### Census Data
```python
# Use Census API with Python
import requests
# API key required: https://api.census.gov/data/key_signup.html
```

### Weather Data
```bash
# Download from NOAA Climate Data Online
# https://www.ncdc.noaa.gov/cdo-web/
```

## Data Processing Pipeline

1. **Raw Data** → `data/raw/` (never modified)
2. **Cleaning & Validation** → Processing scripts in `src/`
3. **Processed Data** → `data/processed/`

## Data Quality Notes

### Known Issues
- **Location Redaction**: Crime locations are generalized to the block level (100 block) for privacy
- **Missing Values**: Some records may have incomplete location or temporal data
- **Reporting Delays**: Crime data is typically reported with a 1-2 day delay
- **Reclassifications**: Crime classifications may be updated retroactively

### Data Coverage
- **Temporal Range**: 2008 - Present
- **Geographic Coverage**: Seattle city limits
- **Update Frequency**: Daily updates for recent data

## Privacy and Ethics

- All data used in this project is publicly available
- Location data is already anonymized by the source (generalized to block level)
- Do not attempt to de-anonymize or re-identify individuals
- Aggregate data appropriately in all visualizations and reports
- Follow all data use agreements and terms of service

## File Naming Conventions

### Raw Data
- `spd_crime_data_YYYYMMDD.csv` - SPD crime data snapshot
- `seattle_neighborhoods.geojson` - Neighborhood boundaries
- `census_acs5_YYYY.csv` - Census ACS 5-year estimates
- `weather_seattle_YYYY.csv` - Annual weather data

### Processed Data
- `crime_cleaned_YYYYMMDD.csv` - Cleaned crime data
- `crime_with_demographics.csv` - Crime data joined with census
- `crime_spatial_analysis.geojson` - Geospatially processed data

## Data Update Log

| Date | Dataset | Version/Period | Notes |
|------|---------|----------------|-------|
| TBD  | SPD Crime Data | TBD | Initial download |
| TBD  | Census ACS | TBD | Initial download |
| TBD  | Weather | TBD | Initial download |

---

**Last Updated**: 2026-02-06
**Maintained By**: Project Team
