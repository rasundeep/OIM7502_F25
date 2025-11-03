# Plotnine: Exploring the Grammar of Graphics in Python

This project explores the seven layers of the Grammar of Graphics using the `plotnine` library — a Python implementation of `ggplot2`.  
It serves as a tutorial for data scientists to understand how layered visualizations can be constructed from data, aesthetics, and geometric mappings.




## Objective

The aim  of this demo is to apply the **seven layers of the Grammar of Graphics** to real-world data and illustrate how `plotnine` builds data visualizations through modular components:
1. Data  
2. Aesthetics  
3. Geometric Objects  
4. Statistical Transformations  
5. Scales  
6. Coordinate Systems  
7. Facets


## Dataset


The very first step in the Grammar of Graphics is the Data Layer. For this demo I would be using the Boston Housing dataset.  This contains data about  housing values and socio economic conditions for various  neighborhoods in the Boston area
Each row represents a single observation..


Objective

To apply the Grammar of Graphics principles through the Plotnine package and demonstrate how visualizations evolve layer-by-layer to reveal insights from a real-world dataset.


**DATA Dictionary**

CRIM – Per capita crime rate by town

ZN – Proportion of residential land zoned for large lots

INDUS – Proportion of non-retail business acres per town

CHAS – Dummy variable indicating proximity to the Charles River (1 = yes, 0 = no)

NOX – Nitric oxide concentration (pollution level)

RM – Average number of rooms per dwelling

AGE – Proportion of older buildings (built before 1940)

DIS – Weighted distance to employment centers

RAD – Accessibility to radial highways

TAX – Property tax rate per $10,000

PTRATIO – Pupil-teacher ratio

LSTAT – Percentage of lower-status population

MEDV – Median value of owner-occupied homes (in $1000s)

ISHIGHVAL – Binary flag (1 = high-value home, 0 = lower-value home) 


## Demonstrated Visual Layers

Each section in the Jupyter notebook illustrates a specific layer of the Grammar of Graphics:

| Layer | Concept | Visualization Example |
|--------|----------|------------------------|
| Data | Foundation of the plot | Display of first rows using `df.head()` |
| Aesthetics | Variable mapping | Scatterplot of `RM` vs `MEDV` |
| Geometric Objects | Visual shapes | `geom_point()` + `geom_smooth()` |
| Statistical Transformations | Summaries | `geom_histogram()` |
| Scales | Transformations | `scale_x_log10()` |
| Coordinate Systems | Plot re-mapping | `geom_boxplot()` + `coord_flip()` |
| Facets | Subplots by group | `facet_wrap("~CHAS")` |
| Theme | Subplots by group | `facet_wrap("~CHAS")` |





Plotnine is a data visualization library for Python built on top of Matplotlib, and it implements the principles of the Grammar of Graphics.
It was inspired by the R package ggplot2, developed by Hadley Wickham, and provides a declarative syntax for creating complex graphics through layering.

Key Features

Layered syntax: Add multiple components (geom, scale, facet, etc.) with the + operator.

Grammar of Graphics foundation: Every visualization is composed of seven layers — data, aesthetics, geometric objects, statistical transformations, scales, coordinates, and facets.

Integration: Works seamlessly with Pandas DataFrames, making it ideal for exploratory data analysis (EDA).

Customization: Offers flexible control over colors, labels, and themes (e.g., theme_minimal(), theme_xkcd()).