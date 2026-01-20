# sea-level-rise-analysis
# Sea Level Rise Analysis (1880–2050)

This project analyzes historical sea level data to identify long-term trends and project future sea level rise using linear regression techniques. The analysis compares overall historical trends with more recent patterns to highlight changes in the rate of sea level increase.

## Project Overview

Using data from the U.S. Environmental Protection Agency (EPA), this project:

- Visualizes observed sea level measurements from 1880 to 2013
- Applies linear regression to:
  - The full historical dataset
  - Data from the year 2000 onward
- Extends both regression models to predict sea level rise through 2050
- Demonstrates how trend assumptions affect long-term projections

## Dataset

- **Source**: EPA Sea Level Data  
- **File**: `epa-sea-level.csv`
- **Key Columns**:
  - `Year`
  - `CSIRO Adjusted Sea Level` (in inches)

The dataset is included locally in the repository for reproducibility.


## Visualizations

All plots and visual outputs are generated and displayed within the **Jupyter Notebook**:

📓 `notebooks/sea_level_analysis.ipynb`

The notebook contains:
- Scatter plots of observed sea levels
- Regression lines for:
  - Full historical data
  - Post-2000 data
- Extended projections to the year 2050

This repository intentionally avoids embedding static image outputs in order to preserve the full analytical context and reproducibility available in the notebook.


### How To Run
1. Open the notebook to view all charts and analysis:
```bash
jupyter notebook notebooks/sea_level_analysis.ipynb
```
OR

2. Run the python script step-by-step:
```
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git

# 2. Move into the project directory
cd your-repo-name

# 3. (Optional but recommended) Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 5. Install required dependencies
pip install -r requirements.txt

# 6. Run the main script
python src/sea_level_predictor.py

# OR run the test script
python tests/test_sea_level_predictor.py
```
### Tools
pandas
matplotlib
scipy



