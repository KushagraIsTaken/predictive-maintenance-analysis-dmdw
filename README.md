# Predictive Maintenance Analytics App

This Streamlit application predicts machine failures using a Random Forest model trained on the AI4I 2020 Predictive Maintenance Dataset. The app allows users to input machine parameters and receive predictions about potential failures and their causes.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Project Information](#project-information)

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/predictive-maintenance-AI4I.git
   cd predictive-maintenance-AI4I
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have the trained model file `random_forest_model.pkl` in the same directory as the app.

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your web browser and go to `http://localhost:8501` to use the application.

4. Enter the required machine parameters and click "Predict" to see the results.


For a live demo of this app, visit: [[HuggingFace](https://huggingface.co/spaces/KushagraisTaken/predictive-maintenance-AI4I)]

## Project Information

- **Project**: Predictive Maintenance Analytics
- **Submitted to**: Dr. Mukesh Kumar
- **Program**: Data Mining & Data Warehousing Course
- **Author**: Kushagra Agrawal
- **Date**: October 2024
- **Contact**: kush4409@gmail.com

For any questions or issues, please open an issue on the GitHub repository or contact the author directly.
