# Blog Post about World Development Indicators (WDI) and Happy Planet Index (HPI)

This project covers the CRISP-DM process for my blog post about relations between the World Development Indicators and the Happy Planet Index (as placeholder for the well-being of a country).

It includes data preprocessing, correlation analyses and a multiple linear regression model. The multiple linear regression model is only used to perform backward elimination in order to confirm the most crucial indicators which were identified in the correlation matrix before. It is not used for predictions.

The main question is whether the Gross Domestic Product (GDP) is a meaningful indicator for the well-being of a country.

The datasets to be analyzed are
* the Happy Planet Index for 2016 (see https://happyplanetindex.org/),
* the World Development Indicators (1960 - 2019) by the World Bank (see https://datacatalog.worldbank.org/dataset/world-development-indicators)

My Blog Post can be found on Medium (so far only the draft as my account is too new to publish): https://medium.com/@max_58709/is-gdp-a-meaningful-measure-for-the-well-being-of-a-country-and-its-citizens-283aa23130f9

This project was conducted in the course of my Data Scientist Nanodegree at Udacity (www.udacity.com).


## Prerequisites

Jupyter Notebook

Python 3

## Getting Started

Download or clone this repository.

Start Jupyter Notebook.

Navigate to the "Blog_Post/jupyter_notebooks" folder.

Open Notebooks of interest.

## CRISP-DM

### Business Understanding
The Gross Domestic Product (GDP) is a widely used measure when it comes to comparing nations and living standards between nations. However, it solely concentrates on economic factors. I therefore ask the following questions:

  * Is GDP a meaningful measure for the well-being of a country?
  * Are there other, maybe more important indicators?
  * Which are the most important fields governments should focus on, in order to improve the well-being of both their inhabitants and their country in general?

### Understanding the dataset
This step is performed in the Jupyter Notebook __"01_Data Exploration"__.

The main characteristics of the WDI Dataset are:
  * 88 topics of indicators covering a total of 1,429 indicators.
  * time series from 1960 - 2019
  * not only states but also totals for sub-regions and islands --> need to reduce country column to only countries
  * more than 50% of data missing in 49 years, including 2017-2019
  --> The correlation analyses will be made for the year 2016, as data quality is much better than for more recent years.

As placeholder for the well-being of a country the Happy Planet Index will be utilized.

### Data Preparation
In order to perform the correlation analyses between WDI and the HPI the two datasets need to be combined. Furthermore, the data has to be properly selected and cleaned.

The following steps are performed in the Jupyter Notebook __"02_Data Preprocessing"__:

**Combine datasets**

  * select year 2016 from WDI dataset
  * find non-matching country names between WDI and HPI datasets
  * create matching table for non-matching countries
  * join WDI and HPI datasets (left join on country name, WDI is base DataFrame)

**Deal with missing data**

  * remove columns (indicators) with more than 50% of missing data
  * select indicators for the analyses
  * impute column mean for remaining NaN values --> there are no columns with more than 10% NaN values
  * no categorical variables --> no need to create dummy variables
  * create (and save) custom dataframes for 2016 and for 6 manually created indicator groups with 42 manually chosen indicators

### Modeling / Analyses

In the Jupyter Notebook __"03_Correlation GDP HPI"__ and the notebooks starting with __"04_Multiple Linear Regression"__ both correlation analyses are made and a multiple linear regression model is built.

The code in the notebooks starting with "04_Multiple Linear Regression" is identical, but the analyzed datasets differ. The custom dataframes from __"02_Data Preprocessing"__ are used for the analyses of economic, education, environment, infrastructure and politics indicators.

**Correlation**

A correlation matrix is crafted with Seaborn and correlation coefficients are printed to evaluate
  1. the correlation of all indicators (in the group) with the HPI
  2. the correlation of the indicators which are left after the backwards elimination in the multiple linear regression model

**Multiple lineal regression model**

By utilizing the scikit-learn library the following steps are performed to build a linear regression model:

  * standardize features with StandardScaler
  * split dataset into X (matrix of independent variables) and y (vector of dependent variable)
  * use statsmodels library and method of ordinary least squares (OLS) to evaluate model and importance of independent variables before and after backwards elimination
  * backwards elimination 1: remove the independent variables where P-values in the multiple linear regression model are below a certain significance level (standard value = 5%)
  * backwards elimination 2: like backwards elimination1 but ensuring adjusted R² is improved
  * for some datasets there are multicolinearity problems. However, these can be ignored, as the regression model is not used for prediction but for confirming the findings of the correlation matrix.

### Results

The initial questions are answered by the analyses in the Jupyter Notebook __"03_Correlation GDP HPI"__ and the notebooks starting with __"04_Multiple Linear Regression"__.

* Is GDP a meaningful measure for the well-being of a country?
  Correlation matrix and correlation coefficients in __"03_Correlation GDP HPI"__ show that there is no significant correlation between "GDP growth  (annual %)", "GDP per capita, PPP (current international $)" and "Happy Planet Index"

* Are there other, maybe more important indicators?
  The notebooks starting with __"04_Multiple Linear Regression"__ show that there are WDI with significant correlation coefficients relating to HPI. The five best correlation coefficients (absolute value > 0.4) are found for
    * Life expectancy at birth, total (years)
    * Access to electricity (% of population)
    * Primary completion rate, total (% of relevant age group)
    * People using at least basic drinking water services (% of population)
    * People using at least basic sanitation services (% of population)

* Which are the most important fields governments should focus on, in order to improve the well-being of both their inhabitants and their country in general?
  * 3 of the 5 strongest HPI-correlating indicators are from the health group
  * health, infrastructure and education groups show the highest absolute correlation coefficients
  * in the other groups negative correlation coefficients prevail, which absolute values are lower than the absolute values of the top positive coefficients

### Presentation

The Jupyter Notebook __"03_Correlation GDP HPI"__ and the notebooks starting with __"04_Multiple Linear Regression"__ provide correlation matrices which are created with seaborn. They are then saved into into jpg files to be included in the blog article on medium.

My Blog Post can be found on Medium (so far only the draft as my account is too new to publish): https://medium.com/@max_58709/is-gdp-a-meaningful-measure-for-the-well-being-of-a-country-and-its-citizens-283aa23130f9


## Used libraries

* numpy
* pandas
* matplotlib.pyplot
* seaborn

* sklearn.preprocessing
* sklearn.model_selection
* sklearn.linear_model

* statsmodels.regression.linear_model


## Author

* **Max Maelicke** - (https://github.com/MaxMaelicke)


## Acknowledgments

Many thanks for the free and openly accessible data to
* the New Economics Foundation for the Happy Planet Index (see https://happyplanetindex.org/),
* the World Bank for the World Development Indicators (1960 - 2019) (see https://datacatalog.worldbank.org/dataset/world-development-indicators)

Many thanks to Drazen Zaric for his article about Better Heatmaps and Correlation Matrix Plots in Python (see https://towardsdatascience.com/better-heatmaps-and-correlation-matrix-plots-in-python-41445d0f2bec).

And finally many thanks to the guys providing pandas and its documentation and to the community of stackoerflow.
