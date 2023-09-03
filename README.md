# Diversify

## Overview
This is a portfolio management project focused on developing software that optimizes investment strategies by diversifying investments across multiple asset classes to maximize returns.

## Libraries Used
pandas
numpy
pickle
tensorflow
Tools
FastAPI

## Features
The final GUI for this project will include the following features:
Dropdown Menu: A dropdown menu where users can select the stock they wish to invest in.
Toggle Bars: Two toggle bars that allow users to indicate if they want to invest in gold and real estate, respectively.

## Models
For this project, three separate models have been trained:
Stock Model: A model dedicated to predicting stock investments.
Gold Model: A model designed to predict gold investments.
Real Estate Model: A model specialized in predicting real estate investments.

## API Integration
The three trained models are going to be released as APIs using FastAPI. These APIs will serve as the backend for the project and will be seamlessly integrated into the frontend for easy access and investment decision-making.

## File Structure
The project is organized into the following folders and files:
Data folder: Contains the data on which the models are trained.
Model folder: Houses the three pre-trained model files.
Model code: Contains the code used to develop and train the models.
