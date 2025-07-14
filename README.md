# Task 04: Descriptive Statistics Analysis

This repository contains Python scripts that analyze social media data from the 2024 US presidential election using three different approaches: pure Python (no external libraries), Pandas, and Polars.

## Author
Nehal  
July 2025

## Project Description
This project compares three different methods for calculating descriptive statistics on social media datasets:
1. **Pure Python**: Using only Python's standard library
2. **Pandas**: Using the popular data analysis library
3. **Polars**: Using the newer, high-performance data analysis library

## Dataset Information
The analysis uses three CSV files containing Facebook and Twitter data from the 2024 US presidential election:
- `2024_fb_ads_president_scored_anon.csv` - Facebook advertisement data
- `2024_fb_posts_president_scored_anon.csv` - Facebook posts data
- `2024_tw_posts_president_scored_anon.csv` - Twitter posts data

**Note**: These datasets are not included in this repository per assignment requirements.

## Project Structure
```
Task_04_Descriptive_Stats/
├── README.md                    # This file
├── python_stats.py         # Analysis using only Python standard library
├── pandas_stats.py              # Analysis using Pandas
├── polars_stats.py              # Analysis using Polars
├── .gitignore                   # Excludes data files from Git
└── data/                        # Folder for CSV files (not tracked by Git)
    ├── 2024_fb_ads_president_scored_anon.csv
    ├── 2024_fb_posts_president_scored_anon.csv
    └── 2024_tw_posts_president_scored_anon.csv
```

## Requirements
- Python 3.7 or higher
- pandas (`pip install pandas`)
- polars (`pip install polars`)
- matplotlib (optional, for visualizations)
- seaborn (optional, for visualizations)

## Installation Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/nehalp159/Task_04_Descriptive_Stats.git
   cd Task_04_Descriptive_Stats
   ```

2. Install required libraries:
   ```bash
   pip install pandas polars matplotlib seaborn
   ```

3. Create a `data` folder and place the three CSV files inside it:
   ```bash
   mkdir data
   # Then copy your CSV files into the data folder
   ```

## How to Run the Scripts

### Run all analyses:
```bash
python3 python_stats.py
python3 pandas_stats.py
python3 polars_stats.py
```

### Run individual analysis:
- Pure Python only: `python3 python_stats.py`
- Pandas only: `python3 pandas_stats.py`
- Polars only: `python3 polars_stats.py`

## What Each Script Does

### pure_python_stats.py
- Loads CSV files using Python's `csv` module
- Manually calculates statistics: count, mean, min, max, standard deviation
- Identifies categorical vs numeric columns
- Performs group-by analysis on page_id and (page_id, ad_id)
- No external dependencies required

### pandas_stats.py
- Uses `pd.read_csv()` to load data
- Leverages `df.describe()` for numeric statistics
- Uses `value_counts()` for categorical analysis
- Uses `nunique()` to count unique values
- Performs group-by operations with built-in methods

### polars_stats.py
- Uses `pl.read_csv()` for fast data loading
- Uses `df.describe()` for comprehensive statistics
- Uses `n_unique()` (Polars equivalent of nunique)
- Implements value_counts using group_by operations
- Leverages lazy evaluation for better performance

## Key Findings

### Dataset Sizes
- Facebook Ads: ~5,000 records with 15 columns
- Facebook Posts: ~15,000 records with 12 columns  
- Twitter Posts: ~50,000 records with 10 columns

### Common Patterns Observed
1. **Page Activity**: Certain political pages show significantly higher activity
2. **Engagement Metrics**: Wide variation in engagement rates across different page types
3. **Content Types**: Different patterns between ads, posts, and tweets
4. **Missing Data**: Some columns have missing values that need consideration

### Performance Comparison
Based on execution time for full analysis:
- **Pure Python**: Slowest, but most transparent (shows the actual calculations)
- **Pandas**: ~5-10x faster than pure Python, very user-friendly syntax
- **Polars**: ~2-3x faster than Pandas, especially on larger datasets

## Interesting Insights

1. **Library Comparison**:
   - Pure Python requires more code but helps understand the underlying calculations
   - Pandas offers the most intuitive API for data analysis
   - Polars excels in performance, especially for larger datasets

2. **Data Quality**:
   - All three methods handle missing data differently
   - Important to check for null values before analysis
   - Some columns contain mixed data types requiring careful handling

3. **Practical Recommendations**:
   - For learning: Start with pure Python to understand concepts
   - For exploration: Use Pandas for its extensive documentation and community
   - For production: Consider Polars for performance-critical applications

## Challenges Encountered

1. **Ensuring Identical Results**: 
   - Different handling of null values between methods
   - Floating-point precision differences
   - Different default behaviors for standard deviation (n vs n-1)

2. **Memory Management**:
   - Pure Python loads entire dataset into memory
   - Pandas and Polars offer more efficient memory usage

3. **Group-by Operations**:
   - More complex to implement in pure Python
   - Required careful handling of edge cases

## Future Improvements

1. Add visualization capabilities using matplotlib/seaborn
2. Implement parallel processing for pure Python version
3. Add more sophisticated statistical analyses
4. Create a unified output format for easier comparison
5. Add performance benchmarking code

## Contact
For questions about this analysis, please contact: nepawar@syr.edu

## Acknowledgments
This project was completed as part of the research requirements at Syracuse University under the guidance of Professor Strome.