# Blog Post about World Development Indicators (WDI) and Happy Planet Index (HPI)

This project covers the data preprocessing, correlation analyses and multiple linear regression model for my blog post about connections between the World Development Indicators and the Happy Planet Index (as placeholder for the well-being of a country).

The main question is whether the Gross Domestic Product (GDP) is a meaningful indicator for the well-being of a country.

The multiple linear regression model is only used to perform backward elimination in order to confirm the most crucial indicators which were identified in the correlation matrix before. It is not used for predictions.

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

## Jupyter Notebooks

The purpose of each notebook is described at the beginning of the notebook.

The main findings/achievements are:

**1. Data Exploration**
  * 88 topics of indicators covering a total of 1,429 indicators.
  * time series from 1960 - 2019
  * more than 50% of data missing in 49 years, including 2017-2019
  --> The analyses refer to the year 2016, as data quality was much better for 2016 than for the following years.

**2. Data Preprocessing**
  * Join WDI and HPI datasets (match differing country names)
  * Deal with missing data (remove columns (indicators) with more than 50% of missing data; impute column mean for remaining NaN values)
  * Create (and save) custom dataframes for 2016 and for 6 manually created indicator groups with 42 manually chosen indicators

**3. Correlation between GDP and HPI**
  * Correlation matrix with Seaborn to analyze correlation between "GDP growth  (annual %)", "GDP per capita, PPP (current international $)" and "Happy Planet Index"
  * no significant correlation coefficients

**4. Multiple Linear Regression and Correlation** (despite the name these notebooks also cover the correlation part)

The code in the notebooks starting with "04_Multiple Linear Regression" is identical, but the analyzed datasets differ. The custom dataframes from 02_Data Preprocessing are used for the analyses of economic, education, environment, infrastructure and politics indicators.
  * 3 strongest HPI-correlating indicators form the health group
  * health, infrastructure and education groups show the highest absolute correlation coefficients
  * in the other groups negative correlation coefficients prevail, which absolute values are lower than the absolute values of the top positive coefficients
  * For some datasets there are multicolinearity problems. However, these can be ignored, as the regression model is not used for prediction but for confirming the findings of the correlation matrix.
  * correlation matrices are created with seaborn and saved into jpg files


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
