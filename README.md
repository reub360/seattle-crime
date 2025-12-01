# Project Overview
This repository hosts a comprehensive data analysis project utilizing publicly available crime incident data from the Seattle Police Department. The goal is to identify trends, patterns, and potential correlations in criminal activity across different neighborhoods and time periods within Seattle, WA. The analysis aims to transform raw data into actionable insights, providing a data-driven perspective on public safety dynamics in the city.

## Analysis Objectives

- Data Cleaning and Preprocessing: To clean, validate, and structure the raw Seattle crime data for analytical use.
- Exploratory Data Analysis (EDA): To uncover initial patterns, anomalies, and relationships within the dataset using statistical methods and data visualization.
- Trend Identification: To analyze temporal trends (e.g., time of day, day of week, seasonal variations) and spatial patterns (e.g., crime hotspots) in different types of criminal activity.
- Geospatial Analysis/Crime Mapping: To visualize the geographical distribution of crimes to identify specific high-risk areas in Seattle.
- Contextual Correlation: To integrate external socio-economic and environmental datasets to test hypotheses about the drivers of crime (e.g., income inequality, proximity to transit hubs, weather).
- Reporting: To present key findings and insights in a clear, accessible format (e.g., reports, interactive dashboards) that can inform discussions around public safety resource allocation.

## Key Outputs & Deliverables
- Interactive Dashboards: Visualizations (e.g., built with Tableau or Python libraries like Plotly) showcasing crime frequency, types, and locations, accessible via a hosted link.
- Analysis Notebooks: Jupyter notebooks detailing the entire analytical workflow, from data ingestion and cleaning to statistical modeling and visualization.
- Static Visualizations: High-quality maps and charts included in this README and a separate outputs/ folder.
- Technical Report (PDF): A detailed document summarizing methodologies, assumptions, results, and limitations of the analysis.
- Cleaned Datasets: Processed and anonymized datasets ready for further analysis by other researchers/developers (stored in a data/processed directory).

## Data Sources
- This analysis integrates multiple public datasets to provide a robust, multi-dimensional view of crime and its potential correlations.

|Dataset Name|	Source	|Type|	Purpose in Analysis|
|--|--|--|--|
|SPD Crime Data|Seattle Open Data Portal|Core|Primary incident data (time, location, type).|
|Geospatial Boundaries|Seattle Open Data Portal|Supplemental|Neighborhood boundaries, park locations for mapping.|
|911 Call Data/CAD|Seattle Open Data Portal|Supplemental|Analyze police response times and call volume.|
|U.S. Census Data|data.census.gov|Contextual|Socio-economic context (income, poverty levels, demographics).|
|Local Weather Data|NOAA / NCEI|Contextual|Explore weather's impact on certain crime types.|
|Public Transit Locations|King County Metro Data|Contextual|Analyze crime proximity to transit hubs and high-traffic areas.|


## Methodology
- TBD

## Usage & Replication
- TBD
