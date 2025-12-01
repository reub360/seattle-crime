# CLAUDE.md - AI Assistant Guide for seattle-crime

## Project Overview

**seattle-crime** is a comprehensive data analysis project utilizing publicly available crime incident data from the Seattle Police Department. The goal is to identify trends, patterns, and potential correlations in criminal activity across different neighborhoods and time periods within Seattle, WA. The analysis aims to transform raw data into actionable insights, providing a data-driven perspective on public safety dynamics in the city.

### Analysis Objectives

1. **Data Cleaning and Preprocessing**: Clean, validate, and structure the raw Seattle crime data for analytical use
2. **Exploratory Data Analysis (EDA)**: Uncover initial patterns, anomalies, and relationships within the dataset using statistical methods and data visualization
3. **Trend Identification**: Analyze temporal trends (e.g., time of day, day of week, seasonal variations) and spatial patterns (e.g., crime hotspots) in different types of criminal activity
4. **Geospatial Analysis/Crime Mapping**: Visualize the geographical distribution of crimes to identify specific high-risk areas in Seattle
5. **Contextual Correlation**: Integrate external socio-economic and environmental datasets to test hypotheses about the drivers of crime (e.g., income inequality, proximity to transit hubs, weather)
6. **Reporting**: Present key findings and insights in a clear, accessible format (e.g., reports, interactive dashboards) that can inform discussions around public safety resource allocation

### Key Deliverables

- **Interactive Dashboards**: Visualizations (e.g., built with Tableau or Python libraries like Plotly) showcasing crime frequency, types, and locations
- **Analysis Notebooks**: Jupyter notebooks detailing the entire analytical workflow, from data ingestion and cleaning to statistical modeling and visualization
- **Static Visualizations**: High-quality maps and charts in the outputs/ folder
- **Technical Report (PDF)**: Detailed document summarizing methodologies, assumptions, results, and limitations of the analysis
- **Cleaned Datasets**: Processed and anonymized datasets ready for further analysis (stored in data/processed directory)

## Repository Structure

### Current State
```
seattle-crime/
├── .git/                 # Git repository metadata
├── README.md            # Project overview
└── CLAUDE.md           # This file - AI assistant guide
```

### Recommended Structure
As the project develops, the following structure should be implemented:

```
seattle-crime/
├── data/                # Raw and processed data files
│   ├── raw/            # Original, immutable data
│   ├── processed/      # Cleaned and transformed data
│   └── README.md       # Data sources and descriptions
├── notebooks/          # Jupyter notebooks for exploration
│   ├── exploratory/    # Exploratory data analysis
│   └── analysis/       # Detailed analysis notebooks
├── src/                # Source code
│   ├── analysis/       # Data analysis scripts
│   ├── visualization/  # Visualization modules
│   ├── geospatial/     # Geospatial analysis and mapping
│   ├── utils/          # Utility functions
│   └── __init__.py
├── tests/              # Test files
│   └── test_*.py
├── docs/               # Documentation
│   └── reports/        # Technical reports (PDF)
├── outputs/            # Generated outputs
│   ├── figures/        # Static visualizations and charts
│   ├── maps/           # Crime maps and geospatial visualizations
│   └── dashboards/     # Interactive dashboard exports
├── .gitignore          # Git ignore patterns
├── requirements.txt    # Python dependencies
├── setup.py or pyproject.toml  # Package configuration
├── README.md           # Project overview
└── CLAUDE.md          # This file - AI assistant guide
```

## Development Workflows

### Git Workflow

**Branch Strategy:**
- Main branch: `main` (or `master`) - production-ready code
- Feature branches: `feature/descriptive-name`
- Claude branches: `claude/claude-md-*` (auto-generated)
- Bug fixes: `fix/issue-description`

**Commit Conventions:**
- Use clear, descriptive commit messages
- Format: `<type>: <description>`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Examples:
  - `feat: add crime data parser for Seattle Open Data`
  - `fix: correct date parsing in crime records`
  - `docs: update README with data sources`
  - `refactor: optimize data loading performance`

**Workflow Steps:**
1. Create or checkout feature branch
2. Make changes iteratively
3. Run tests and linters
4. Commit with descriptive message
5. Push to remote branch
6. Create pull request when ready

### Code Quality Standards

**Python Style:**
- Follow PEP 8 style guide
- Use type hints for function signatures
- Maximum line length: 88 characters (Black formatter default)
- Use meaningful variable and function names

**Documentation:**
- Add docstrings to all functions and classes
- Use Google or NumPy docstring format
- Include examples in docstrings for complex functions
- Keep inline comments minimal and meaningful

**Testing:**
- Write unit tests for all data processing functions
- Use pytest as the testing framework
- Aim for >80% code coverage
- Test edge cases and error conditions

## Technology Stack

### Recommended Tools

**Data Processing:**
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `dask` - Parallel computing for large datasets (optional)

**Visualization:**
- `matplotlib` - Basic plotting
- `seaborn` - Statistical visualizations
- `plotly` - Interactive visualizations and dashboards
- `tableau` - Professional dashboard creation (optional)

**Geospatial Analysis:**
- `geopandas` - Geographic data processing
- `folium` - Interactive maps
- `shapely` - Geometric operations
- `contextily` - Basemap tiles for maps

**Statistical Analysis:**
- `scipy` - Scientific computing and statistical tests
- `statsmodels` - Statistical modeling

**Development Tools:**
- `pytest` - Testing framework
- `black` - Code formatter
- `flake8` - Linter
- `mypy` - Type checker
- `jupyter` - Interactive notebooks

## Key Conventions for AI Assistants

### Data Handling

1. **Data Immutability:**
   - Never modify files in `data/raw/`
   - Always create new files in `data/processed/`
   - Document all transformations

2. **Data Privacy:**
   - Be mindful of personally identifiable information (PII)
   - Anonymize data when necessary
   - Follow data usage guidelines from source

3. **Data Validation:**
   - Always validate data after loading
   - Check for missing values, outliers, and inconsistencies
   - Document data quality issues

### Code Development

1. **Before Making Changes:**
   - Read existing code thoroughly
   - Understand the current implementation
   - Check for related tests

2. **When Adding Features:**
   - Start with data exploration in notebooks
   - Move production code to `src/` directory
   - Write tests for new functionality
   - Update documentation

3. **When Fixing Bugs:**
   - Write a test that reproduces the bug
   - Fix the issue
   - Verify the test passes
   - Document the fix in commit message

4. **Error Handling:**
   - Use try-except blocks for external data sources
   - Provide informative error messages
   - Log errors appropriately
   - Validate user inputs

### Analysis Best Practices

1. **Reproducibility:**
   - Set random seeds for reproducible results
   - Document software versions
   - Include environment setup instructions

2. **Version Control:**
   - Commit notebooks with cleared outputs
   - Use `.gitignore` for large data files
   - Document data sources with download instructions

3. **Performance:**
   - Profile code for large datasets
   - Use vectorized operations (pandas/numpy)
   - Consider chunking for memory-intensive operations

### Documentation Requirements

1. **README Updates:**
   - Keep installation instructions current
   - Document all data sources
   - Include usage examples
   - List all dependencies

2. **Code Comments:**
   - Explain complex algorithms
   - Document assumptions
   - Note data quality issues
   - Reference external resources

3. **Analysis Documentation:**
   - Document methodology
   - Explain statistical choices
   - Include limitations and caveats
   - Provide interpretation guidelines

## Common Tasks

### Setting Up Development Environment

```bash
# Clone repository
git clone <repository-url>
cd seattle-crime

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (when requirements.txt exists)
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt  # If exists
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_analysis.py
```

### Data Analysis Workflow

```python
# 1. Load data
import pandas as pd
df = pd.read_csv('data/raw/seattle_crime.csv')

# 2. Explore data
df.info()
df.describe()
df.head()

# 3. Clean data
df_clean = df.dropna()
# Document cleaning steps

# 4. Analyze
# Perform analysis

# 5. Visualize
# Create visualizations

# 6. Save results
df_clean.to_csv('data/processed/seattle_crime_clean.csv', index=False)
```

### Geospatial Analysis Guidelines

1. **Coordinate Systems:**
   - Use WGS84 (EPSG:4326) for latitude/longitude data
   - Use appropriate projected CRS for distance calculations (e.g., UTM Zone 10N / EPSG:32610 for Seattle)
   - Always verify and document the CRS being used
   - Transform coordinates when necessary for accurate spatial operations

2. **Mapping Best Practices:**
   - Include basemaps for context (streets, satellite imagery)
   - Use appropriate color schemes for heatmaps (avoid rainbow)
   - Add legends, scale bars, and north arrows
   - Consider colorblind-friendly palettes
   - Aggregate data appropriately to avoid overplotting

3. **Spatial Analysis:**
   - Use spatial joins to combine datasets (crimes with neighborhoods, transit stops)
   - Consider buffer zones when analyzing proximity
   - Account for edge effects in hotspot analysis
   - Validate spatial relationships before analysis
   - Document any assumptions about spatial accuracy

4. **Performance Considerations:**
   - Use spatial indexing for large datasets
   - Simplify geometries when appropriate
   - Consider downsampling for interactive visualizations
   - Cache basemap tiles to reduce API calls

## Security Considerations

1. **API Keys and Secrets:**
   - Never commit API keys or credentials
   - Use environment variables or config files
   - Add sensitive files to `.gitignore`

2. **Data Access:**
   - Respect data usage terms
   - Implement appropriate access controls
   - Document data retention policies

3. **Privacy Protection:**
   - Never attempt to de-anonymize location data
   - Respect privacy redactions in the source data
   - Aggregate data appropriately to protect individual privacy
   - Follow all data use agreements and terms of service

## Project-Specific Notes

### Data Sources

This analysis integrates multiple public datasets to provide a robust, multi-dimensional view of crime and its potential correlations:

| Dataset Name | Source | Type | Purpose in Analysis |
|--------------|--------|------|---------------------|
| SPD Crime Data | Seattle Open Data Portal | Core | Primary incident data (time, location, type) |
| Geospatial Boundaries | Seattle Open Data Portal | Supplemental | Neighborhood boundaries, park locations for mapping |
| 911 Call Data/CAD | Seattle Open Data Portal | Supplemental | Analyze police response times and call volume |
| U.S. Census Data | data.census.gov | Contextual | Socio-economic context (income, poverty levels, demographics) |
| Local Weather Data | NOAA / NCEI | Contextual | Explore weather's impact on certain crime types |
| Public Transit Locations | King County Metro Data | Contextual | Analyze crime proximity to transit hubs and high-traffic areas |

**Important Links:**
- Seattle Open Data Portal: https://data.seattle.gov
- U.S. Census Data: https://data.census.gov
- NOAA National Centers for Environmental Information: https://www.ncei.noaa.gov
- King County Metro: https://kingcounty.gov/en/dept/metro

### Seattle Crime Data Characteristics

1. **Expected Data Fields (SPD Crime Data):**
   - Incident ID
   - Date/Time of occurrence
   - Crime type/category
   - Location (coordinates, address, neighborhood)
   - Case status
   - Report number
   - Offense description

2. **Analysis Focus Areas:**
   - **Temporal Analysis**: Crime trends over time, seasonal patterns, time-of-day variations, day-of-week patterns
   - **Geospatial Analysis**: Geographic hotspot identification, neighborhood-level analysis, proximity to transit/parks
   - **Crime Classification**: Distribution by crime type, severity patterns
   - **Contextual Correlations**: Relationship with socio-economic factors, weather patterns, transit accessibility
   - **Police Response**: Analysis of 911 call data, response times, clearance rates

3. **Data Considerations:**
   - Data reporting delays and updates
   - Changes in reporting practices over time
   - Privacy redactions in location data (approximate locations)
   - Crime reclassifications and UCR code changes
   - Missing or incomplete records
   - Seasonal variations in reporting
   - Population density differences across neighborhoods

## Troubleshooting

### Common Issues

1. **Data Loading Errors:**
   - Check file paths
   - Verify data format
   - Check encoding (UTF-8 vs others)

2. **Memory Issues:**
   - Use chunking for large files
   - Filter data early in pipeline
   - Consider using Dask for large datasets

3. **Visualization Issues:**
   - Clear matplotlib cache
   - Check backend configuration
   - Verify data types for plotting

## Additional Resources

### Seattle Crime Data Resources
- Seattle Open Data Portal: https://data.seattle.gov
- Seattle Police Department: https://www.seattle.gov/police
- Crime Statistics Research: Bureau of Justice Statistics
- King County Metro Data: https://kingcounty.gov/en/dept/metro
- U.S. Census Bureau: https://data.census.gov
- NOAA Climate Data: https://www.ncei.noaa.gov

### Learning Resources
- Pandas Documentation: https://pandas.pydata.org
- GeoPandas Documentation: https://geopandas.org
- Seaborn Tutorial: https://seaborn.pydata.org/tutorial.html
- Plotly Documentation: https://plotly.com/python/
- Folium Documentation: https://python-visualization.github.io/folium/
- Python Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/

### Geospatial Analysis Resources
- Spatial Data Science: https://www.spatialdata.science/
- Crime Mapping and Analysis: NIJ Crime Mapping Research Center

## Maintenance

**Last Updated:** 2025-12-01
**Status:** Project Planning Phase
**Next Steps:**
1. Set up project directory structure (data/, notebooks/, src/, outputs/)
2. Create requirements.txt with core dependencies (pandas, geopandas, plotly, etc.)
3. Set up .gitignore for data files and outputs
4. Download initial SPD crime dataset from Seattle Open Data Portal
5. Create initial exploratory data analysis notebook
6. Document data schema and fields in data/README.md
7. Begin data cleaning and preprocessing pipeline
8. Develop geospatial visualization prototypes

---

*This file should be updated as the project evolves to reflect current practices, structure, and conventions.*
