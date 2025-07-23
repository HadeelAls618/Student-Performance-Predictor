# Student Performance Prediction System

##  Project Overview

This project delivers a **production-ready ML system** that predicts student exam scores based on demographic and academic features such as gender, parental education, and test preparation status. The solution integrates **end-to-end MLOps practices**, including automated data pipelines, model deployment via Flask, and a CI/CD workflow for seamless delivery.



## Business Problem

Educational institutions need early insights into student performance to provide timely support and improve outcomes. Manual tracking is often inefficient and reactive. This system enables institutions to **automatically predict student performance**, helping educators proactively identify students who may need intervention.


##  ML Problem

The goal is to build a regression model that accurately predicts a student’s exam score using structured data inputs. The model is integrated into a **web-based interface** that allows real-time predictions.


## Dataset

- Source: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)  
- Features include: gender, parental level of education, lunch type, test preparation course, and scores in math, reading, and writing.



## Project Methodology

The project follows a four-stage ML workflow, emphasizing modularity, automation, and deployment readiness.


###  1. Data Pipeline

- Loaded and explored the dataset  
- Handled missing values and cleaned data  
- Applied **feature engineering**:
  - One-hot encoded categorical variables
  - Normalized numeric features  
- Split data into training and testing sets



### 2. Training Pipeline

- Trained multiple **regression models** to predict final exam scores  
- Selected the best-performing model using **MAE** and **R²** as evaluation metrics  
- Saved the trained model using serialization for deployment


###  3. Deployment & CI/CD Pipeline

* Developed a **Flask web application** to serve the trained model, allowing users to input student details and receive predicted exam scores instantly.
* Deployed the app to **AWS Elastic Beanstalk** for scalable, production-grade hosting.
* Implemented a complete **CI/CD pipeline** to automate testing, building, and deployment using:

  * **Docker** for containerization
  * **AWS ECR & EC2** for image storage and hosting
  * **GitHub Actions** for end-to-end automation

This setup ensures fast, reliable, and maintainable model updates in a real-world environment.


## Summary

This project implements a complete ML system for predicting student performance with CI/CD-enabled deployment. Educational institutions can use this tool to support proactive interventions and improve outcomes.

Key highlights include:

-  **End-to-End ML Pipeline**: From data preprocessing to real-time prediction  
-  **Web App Deployment**: Flask-based interface with AWS hosting  
- **MLOps Ready**: Automated builds, Dockerized app, CI/CD pipelines  
-  **User-Friendly**: Lightweight interface for non-technical users


##  Contact

Feel free to connect if you have questions or want to collaborate!

-  [LinkedIn](https://www.linkedin.com/in/hadeel-als)  
-  [alsaadonhadeel@gmail.com](mailto:alsaadonhadeel@gmail.com)

