# House Pricing & Affordability Analysis

## Overview
This project provides a comprehensive analysis of housing prices and affordability trends. It combines data visualization, statistical analysis, and predictive modeling to understand housing market dynamics and identify factors influencing property prices and affordability across different regions.

## Project Goals
- **Analyze Housing Price Trends**: Examine historical and current housing price patterns
- **Evaluate Affordability**: Assess housing affordability metrics relative to income levels
- **Identify Key Factors**: Determine which features most significantly impact house prices
- **Build Predictive Models**: Create models to forecast housing prices based on key features
- **Generate Insights**: Provide actionable insights for buyers, sellers, and policymakers

## Features
- Data cleaning and preprocessing of housing datasets
- Exploratory Data Analysis (EDA) with visualizations
- Statistical analysis of price distributions and correlations
- Predictive modeling using machine learning algorithms
- Affordability index calculations
- Interactive visualizations and dashboards
- Comparative analysis across regions/markets

## Technologies Used
- **Python 3.x**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization
- **Scikit-learn**: Machine learning and statistical models
- **Jupyter Notebook**: Interactive analysis and documentation
- **Scipy**: Statistical analysis

## Project Structure
```
House-Pricing-Affordability-Analysis/
├── README.md                      # Project documentation
├── data/                          # Data directory
│   ├── raw/                       # Raw input datasets
│   └── processed/                 # Cleaned/processed datasets
├── notebooks/                     # Jupyter notebooks
│   ├── 01_data_exploration.ipynb  # Initial data exploration
│   ├── 02_data_cleaning.ipynb     # Data cleaning and preprocessing
│   ├── 03_eda_analysis.ipynb      # Exploratory data analysis
│   ├── 04_statistical_analysis.ipynb  # Statistical tests and analysis
│   └── 05_predictive_modeling.ipynb   # ML models for price prediction
├── src/                           # Source code modules
│   ├── data_loader.py             # Data loading utilities
│   ├── data_preprocessing.py      # Data cleaning functions
│   ├── analysis.py                # Analysis functions
│   └── visualization.py           # Plotting and visualization utilities
├── visualizations/                # Generated plots and charts
├── models/                        # Trained model files
└── requirements.txt               # Python dependencies

```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip or conda package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/House-Pricing-Affordability-Analysis.git
   cd House-Pricing-Affordability-Analysis
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Analysis
1. Navigate to the notebooks directory
2. Start Jupyter:
   ```bash
   jupyter notebook
   ```
3. Open and run notebooks in sequence:
   - `01_data_exploration.ipynb` - Start here to understand the data
   - `02_data_cleaning.ipynb` - Process and clean the data
   - `03_eda_analysis.ipynb` - Explore patterns and relationships
   - `04_statistical_analysis.ipynb` - Perform statistical tests
   - `05_predictive_modeling.ipynb` - Build and evaluate models

### Using the Python Modules
```python
from src.data_loader import load_data
from src.analysis import calculate_affordability_index
from src.visualization import plot_price_trends

# Load and analyze data
df = load_data('data/raw/housing_data.csv')
affordability = calculate_affordability_index(df)
plot_price_trends(df)
```

## Data Sources
- Housing dataset sourced from public real estate databases
- Data includes property features, pricing, and market indicators
- Preprocessing includes handling missing values and outlier removal

## Key Findings
Results and detailed findings will be documented upon project completion.

## Methodology

### Data Processing
- Missing value handling
- Outlier detection and treatment
- Feature engineering
- Data normalization/scaling

### Analysis Approach
- Descriptive statistics
- Correlation analysis
- Time series analysis (if applicable)
- Distribution analysis

### Modeling
- Algorithm selection: Linear Regression, Random Forest, XGBoost
- Train/test split: 80/20
- Cross-validation: 5-fold cross-validation
- Performance metrics: RMSE, R², MAE

## Results & Visualizations
Key visualizations include:
- Price distribution histograms
- Scatter plots of price vs key features
- Time series of price trends
- Affordability heatmaps
- Model prediction accuracy plots

## Limitations
- Analysis based on available public datasets
- Results may vary based on geographic location and time period
- Model predictions should be used as estimates, not definitive values

## Future Work
- [ ] Expand to additional geographic regions
- [ ] Incorporate additional features (e.g., proximity to amenities)
- [ ] Develop real-time price prediction API
- [ ] Create interactive web dashboard
- [ ] Implement advanced ML models (XGBoost, Neural Networks)
- [ ] Add forecasting for future price trends

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
**Prativa**
- GitHub: [@prativa](https://github.com/prativa)
- Email: contact@example.com

## Acknowledgments
- Special thanks to all contributors and the open-source community
- Data sourced from public real estate databases
- Built with popular Python data science libraries

## Contact
For questions or inquiries about this project, please feel free to reach out via:
- GitHub Issues: [Create an issue](https://github.com/yourusername/House-Pricing-Affordability-Analysis/issues)
- Email: [your.email@example.com]

## Changelog
### Version 1.0.0 (Initial Release)
- Initial project setup
- Data loading and preprocessing
- Exploratory data analysis
- Statistical analysis
- Predictive modeling