# Password Strength Prediction Project

This project focuses on predicting the strength of passwords using machine learning techniques. The project is divided into multiple notebooks, each covering a specific aspect of the project. Below is a summary of each notebook:

## Table of Contents

- [Notebook 01: Fetch data](#notebook-01-fetch-data)
- [Notebook 02: Data Exploration](#notebook-02-data-exploration)
  - [Notebook 02.1: Clean data](#notebook-021-clean-data)
  - [Notebook 02.2: Create Sample Data](#notebook-022-create-sample-data)
  - [Notebook 02.3: Feature Engineering](#notebook-023-feature-engineering)
  - [Notebook 02.4: Descriptive Analysis](#notebook-024-descriptive-analysis)
- [Notebook 03: Select Base Model](#notebook-03-select-base-model)
- [Notebook 04: Make Pipeline](#notebook-04-make-pipeline)

## Notebook 01: Fetch data

In this notebook, we will fetch and preprocess the "rockyou.txt" dataset to analyze password strength. This dataset will serve as the foundation for our "Passwordometer" project.

## Notebook 02: Data Exploration

In this notebook, we explore the dataset to gain insights and understanding about the data. It includes visualizations and statistical analysis to identify patterns and trends in the password data.

### Notebook 02.1: Clean data

In this notebook, we will clean the password dataset obtained in the previous notebook. We will remove invalid passwords and perform basic data cleaning steps to ensure the quality and integrity of the data.

### Notebook 02.2: Create Sample Data

In this notebook, we will create a stratified sample of the clean password dataset obtained in the previous notebook. The stratified sample will ensure that we have representative samples from different password strength levels, allowing us to perform accurate analysis and modeling.

### Notebook 02.3: Feature Engineering

In this notebook, we will perform feature engineering on the stratified sample data obtained in the previous notebook. Feature engineering involves creating new meaningful features from the existing data that can improve the performance of our password strength prediction model.

### Notebook 02.4: Descriptive Analysis

In this notebook, we will perform descriptive analysis on the transformed sample data obtained in the previous notebook. Descriptive analysis involves exploring and summarizing the data to gain insights into the distribution, relationships, and patterns of the variables.

## Notebook 03: Select Base Model

In this notebook, we will select a base model for password strength prediction. We will evaluate various regression models using performance metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), R-squared (R2), and the training time (TT). The model with the best performance will be chosen as the base model for further improvement.

## Notebook 04: Make Pipeline

In this notebook, we will create a machine learning pipeline using scikit-learn. The pipeline will include data preprocessing steps and a decision tree regressor as the base model. The pipeline will be trained and evaluated on the password strength prediction task.

Feel free to explore each notebook in order to gain a comprehensive understanding of the project and the steps involved in password strength prediction.

For more details and code implementation, please refer to the respective notebooks.

**Note: The notebooks are organized in a sequential manner to provide a logical flow of the project. It is recommended to follow the notebooks in the given order to fully grasp the concepts and reproduce the results.**
