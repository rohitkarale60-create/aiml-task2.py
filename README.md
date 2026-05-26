# AIML Task 2 - Data Cleaning (Titanic Dataset)

## Objective
Clean the Titanic dataset by handling missing values using Python and Pandas.

## Tools Used
- Python
- Pandas
- NumPy

## Dataset
Titanic Dataset (`Titanic-Dataset.csv`)

## Tasks Performed
- Loaded dataset using Pandas
- Checked missing values
- Filled missing values in `Age` with median
- Filled missing values in `Embarked` with mode
- Replaced missing values in `Cabin` with `"Unknown"`
- Verified missing values after cleaning
- Saved cleaned dataset as `cleaned_titanic.csv`

## Output
### Missing values before cleaning
- Age: 177
- Cabin: 687
- Embarked: 2

### Missing values after cleaning
- All missing values cleaned successfully

## Files in Repository
- `task2.py`
- `Titanic-Dataset.csv`
- `cleaned_titanic.csv`
- `README.md`

## How to Run
```bash
python task2.py
