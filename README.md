# Project Name

A brief description of your project, what it does, and why it's useful.

![Project Logo or Screenshot](url-to-image.png)  <!-- Optional Image -->

---

## Table of Contents

1. [Introduction](#introduction)
2. [files](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Contributing](#contributing)
6. [License](#license)

---
## Introduction

This repository contains analysis on data about energy burnt during exercise in Calories. The data in ```exercise.csv``` shows different characteristics of the person during the exercise. It contains ``` 'age','body_temp', 'duration','gender','heart_rate','height', 'weight'```. Then it says if a person with these characteristics exercises, how much energy in Calories is burnt. The energy is stored in the file ```calories.csv``` and the two files are connected to eachother by an ```ID``` column. Although both files are ordered in the same way from top to bottom. The model predicts how much energy a person will burn given the data about his body during the sport session.

---
## files
* README.md 
    you can find about the problem, what I did for my project, instructions about executing it, and files of the project.
* Data
       There are two ```csv``` files. ```calories.csv``` and ```exercise.csv```. These files complete each other. ```exercise.csv``` contains features and ```calories.csv``` contains target.
* Notebook ( ```Notebook.ipynb```) with
      Here you can see how I loaded the files, the EDA( exploring the data, cleaning, featue combinations, finding correlation,ploting distribution) process, applying different models to data( Linear Regression, Polynomial Regression, Random Forest,           XGBoost) and choosing the best one(Polynimial Regression) and applying it to data to find the most important featue. Then I saved data and model in a ```model.bin``` file for containerizing them.
* Script ```train.py```
        The file with the final model and codes for saving the result into a file
* Script ```predict.py``` 
        The code for loading the model and serving it, using an instance of fetures, via a web service(using Falsk)
* Files with dependencies
        ```Pipenv``` and ```Pipenv.lock```
*```dockerfile``` for running the service
* Deployment
       image of how I served the model using ```gunicorn``` inside ```docker``` and communicating with it through ```predict-test.py```

### Prerequisites

List any dependencies or software required to run the project. For example:

- Python 3.12+
- Docker (if applicable)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/projectname.git
