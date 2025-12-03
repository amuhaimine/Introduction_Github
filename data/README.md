# NASA Software Defect Prediction Dataset

This directory contains the NASA software defect prediction datasets converted to CSV format.

## Dataset Source
- **Kaggle Dataset**: [Software Defect Prediction NASA](https://www.kaggle.com/datasets/aczy156/software-defect-prediction-nasa/data)
- **Original Source**: NASA MDP (Metrics Data Program)

## Dataset Description
The NASA software defect prediction dataset contains metrics and defect information for various NASA software projects. This data is commonly used for:
- Software defect prediction modeling
- Software quality assessment
- Machine learning research in software engineering

## Files Structure
After running the data download script, you'll find:
- `raw/` - Original downloaded files
- `processed/` - CSV converted files ready for analysis
- `metadata/` - Dataset description and column information

## Usage
1. Run the data download script: `python scripts/download_data.py`
2. The script will download and convert the data to CSV format
3. Use the CSV files in your analysis or machine learning models

## Data Format
The CSV files contain software metrics such as:
- McCabe complexity metrics
- Halstead metrics
- Lines of code metrics
- Defect indicators (target variable)