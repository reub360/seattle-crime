# Seattle Crime Analysis - Setup Guide

This guide will help you set up your development environment and get started with the project.

## Prerequisites

- Python 3.9 or higher
- Git
- 4GB+ RAM recommended for data processing
- Internet connection for downloading datasets

## Step 1: Clone and Navigate

```bash
git clone <repository-url>
cd seattle-crime
```

## Step 2: Create Virtual Environment

### On Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install:
- Data processing libraries (pandas, numpy)
- Geospatial libraries (geopandas, folium, shapely, contextily)
- Visualization libraries (matplotlib, seaborn, plotly)
- Statistical libraries (scipy, statsmodels)
- Development tools (jupyter, pytest, black, flake8)

**Note**: Installing geopandas may take a few minutes as it has system dependencies.

### Optional: Verify Installation

```bash
python -c "import pandas, geopandas, folium; print('All core libraries installed successfully!')"
```

## Step 4: Set Up Jupyter

```bash
# Install Jupyter kernel for this environment
python -m ipykernel install --user --name=seattle-crime --display-name="Seattle Crime Analysis"

# Launch Jupyter Lab
jupyter lab
```

## Step 5: Download Initial Dataset

### Option A: Manual Download
1. Visit [Seattle Open Data Portal](https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5)
2. Click "Export" → "CSV"
3. Save to `data/raw/spd_crime_data.csv`

### Option B: Using Python Script
```bash
python scripts/download_data.py
```

### Option C: Using Socrata API
```python
import pandas as pd

# Download recent data (limited to 50,000 rows for testing)
url = "https://data.seattle.gov/resource/tazs-3rd5.csv?$limit=50000"
df = pd.read_csv(url)
df.to_csv('data/raw/spd_crime_data.csv', index=False)
print(f"Downloaded {len(df)} records")
```

## Step 6: Start Exploring

Open the exploratory notebook:
```bash
jupyter lab notebooks/exploratory/01_initial_data_exploration.ipynb
```

## Project Structure

```
seattle-crime/
├── data/
│   ├── raw/              # Place downloaded datasets here
│   └── processed/        # Cleaned data will be saved here
├── notebooks/
│   ├── exploratory/      # Start here: EDA notebooks
│   └── analysis/         # Advanced analysis notebooks
├── src/                  # Python modules
│   ├── analysis/
│   ├── visualization/
│   ├── geospatial/
│   └── utils/
├── outputs/              # Generated visualizations
└── tests/                # Unit tests
```

## Quick Start Workflow

1. **Activate environment**: `source venv/bin/activate`
2. **Download data**: Use one of the methods above
3. **Open Jupyter**: `jupyter lab`
4. **Run exploration**: Open `notebooks/exploratory/01_initial_data_exploration.ipynb`
5. **Start analyzing**: Follow the notebook cells

## Environment Variables (Optional)

For API access, create a `.env` file in the project root:

```bash
# .env
CENSUS_API_KEY=your_census_api_key_here
NOAA_API_KEY=your_noaa_api_key_here
```

Get API keys:
- Census API: https://api.census.gov/data/key_signup.html
- NOAA API: https://www.ncdc.noaa.gov/cdo-web/token

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test
pytest tests/test_utils.py
```

## Code Formatting and Linting

```bash
# Format code with Black
black src/ tests/

# Lint with flake8
flake8 src/ tests/

# Type check with mypy
mypy src/
```

## Common Issues

### Issue: geopandas installation fails
**Solution**: Install system dependencies first
```bash
# Ubuntu/Debian
sudo apt-get install gdal-bin libgdal-dev

# Mac
brew install gdal

# Then retry: pip install geopandas
```

### Issue: Jupyter kernel not found
**Solution**: Reinstall kernel
```bash
python -m ipykernel install --user --name=seattle-crime --display-name="Seattle Crime Analysis"
```

### Issue: Memory error with large datasets
**Solution**: Use chunking or dask
```python
# Read in chunks
chunks = pd.read_csv('data/raw/large_file.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)
```

## Next Steps

After setup:
1. ✅ Review `data/README.md` for data source documentation
2. ✅ Run `01_initial_data_exploration.ipynb` to understand the data
3. ✅ Check `CLAUDE.md` for development guidelines
4. ✅ Read `README.md` for project objectives

## Getting Help

- **Documentation**: See `docs/` folder
- **AI Assistant Guidelines**: See `CLAUDE.md`
- **Data Documentation**: See `data/README.md`
- **Issues**: Check GitHub issues or create a new one

## Deactivating Environment

When done working:
```bash
deactivate
```

---

**Last Updated**: 2026-02-06
**Maintained By**: Project Team
