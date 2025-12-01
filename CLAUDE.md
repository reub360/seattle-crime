# CLAUDE.md - AI Assistant Guide for seattle-crime

## Project Overview

**seattle-crime** is a data analysis and visualization project focused on Seattle crime statistics. This is currently a new project in its initial setup phase.

### Project Goals
- Analyze Seattle crime data to identify patterns and trends
- Provide visualizations and insights into crime statistics
- Support data-driven decision making for public safety initiatives

## Repository Structure

### Current State
```
seattle-crime/
├── .git/                 # Git repository metadata
├── README.md            # Project overview
└── CLAUDE.md           # This file - AI assistant guide
```

### Recommended Future Structure
As the project develops, the following structure is recommended:

```
seattle-crime/
├── data/                # Raw and processed data files
│   ├── raw/            # Original, immutable data
│   ├── processed/      # Cleaned and transformed data
│   └── README.md       # Data sources and descriptions
├── notebooks/          # Jupyter notebooks for exploration
│   └── exploratory/    # Exploratory data analysis
├── src/                # Source code
│   ├── analysis/       # Data analysis scripts
│   ├── visualization/  # Visualization modules
│   ├── utils/          # Utility functions
│   └── __init__.py
├── tests/              # Test files
│   └── test_*.py
├── docs/               # Documentation
├── output/             # Generated outputs (reports, figures)
│   ├── figures/
│   └── reports/
├── .gitignore          # Git ignore patterns
├── requirements.txt    # Python dependencies
├── setup.py or pyproject.toml  # Package configuration
├── README.md           # Project overview
└── CLAUDE.md          # This file
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

### Recommended Tools (To be determined based on requirements)

**Data Processing:**
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing

**Visualization:**
- `matplotlib` - Basic plotting
- `seaborn` - Statistical visualizations
- `plotly` - Interactive visualizations

**Data Sources:**
- Seattle Open Data Portal
- Seattle Police Department data feeds

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

## Security Considerations

1. **API Keys and Secrets:**
   - Never commit API keys or credentials
   - Use environment variables or config files
   - Add sensitive files to `.gitignore`

2. **Data Access:**
   - Respect data usage terms
   - Implement appropriate access controls
   - Document data retention policies

## Project-Specific Notes

### Seattle Crime Data Characteristics

1. **Data Sources:**
   - Seattle Police Department Crime Data
   - Seattle Open Data Portal (data.seattle.gov)
   - FBI UCR (Uniform Crime Reporting) for context

2. **Data Fields to Expect:**
   - Incident ID
   - Date/Time of occurrence
   - Crime type/category
   - Location (coordinates, address, neighborhood)
   - Case status

3. **Common Analyses:**
   - Crime trends over time
   - Geographic hotspot analysis
   - Crime type distribution
   - Temporal patterns (time of day, day of week, seasonal)
   - Clearance rates

4. **Considerations:**
   - Data reporting delays
   - Changes in reporting practices
   - Privacy redactions in location data
   - Crime reclassifications

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

### Learning Resources
- Pandas Documentation: https://pandas.pydata.org
- Seaborn Tutorial: https://seaborn.pydata.org/tutorial.html
- Python Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/

## Maintenance

**Last Updated:** 2025-12-01
**Status:** Initial Setup
**Next Steps:**
1. Set up project structure
2. Identify and document data sources
3. Create requirements.txt with dependencies
4. Set up .gitignore
5. Begin exploratory data analysis

---

*This file should be updated as the project evolves to reflect current practices, structure, and conventions.*
