# Task 04: Descriptive Statistics Analysis

This repository includes Python scripts that use three distinct methods to evaluate social media data collected during the US presidential election of 2024: Polars, Pandas, and pure Python (no additional libraries).

## Author
Nehal  
July 2025

## Project Description
In order to determine descriptive statistics on social media datasets, this research project examines three distinct approaches:
1. **Pure Python**: Using only Python's standard library
2. **Pandas**: Using the popular data analysis library
3. **Polars**: Using the newer, high-performance data analysis library

## Dataset Information
Three CSV files with Twitter and Facebook data from the US presidential election of 2024 are used in the analysis:
- `2024_fb_ads_president_scored_anon.csv` - Facebook advertisement data
- `2024_fb_posts_president_scored_anon.csv` - Facebook posts data
- `2024_tw_posts_president_scored_anon.csv` - Twitter posts data

**Note**: These datasets are not included in this repository.

## Project Structure
```
Task_04_Descriptive_Stats/
├── README.md                    # This file
├── python_stats.py              # Analysis using only Python standard library
├── pandas_stats.py              # Analysis using Pandas
├── polars_stats.py              # Analysis using Polars
├── .gitignore                   # Excludes data files from Git
└── data/                        # Folder which contains CSV files (not tracked by Git)
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
1. Create a clone of this repository:
   ```bash
   git clone https://github.com/nehalp159/Task_04_Descriptive_Stats.git
   cd Task_04_Descriptive_Stats
   ```

2. Install the necessary libraries:
   ```bash
   pip install pandas polars matplotlib seaborn
   ```

3. Put all three CSV files into a `data` folder that has been created:
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
- Uses Python's `csv` module to load CSV files
- Manually computes statistics: count, mean, min, max, standard deviation
- Identifies numeric vs categorical columns
- Performs group-by analysis on page_id as well as (page_id, ad_id)
- There is no need for external dependencies

### pandas_stats.py
- Uses `pd.read_csv()` to load data
- Uses `df.describe()` to obtain numerical statistics
- Uses `value_counts()` to perform categorical analysis
- Uses `nunique()` to count unique values
- Performs group-by operations with built-in methods

### polars_stats.py
- Uses `pl.read_csv()` for fast data loading
- Uses `df.describe()` for comprehensive statistics
- Uses `n_unique()` (Polars equivalent of nunique)
- Implements value_counts using group_by operations
- Uses lazy evaluation to improve performance

## Key Findings

### Dataset Sizes
- **Facebook Ads**: 246,745 records with 41 columns
- **Facebook Posts**: 19,009 records with 56 columns  
- **Twitter Posts**: 27,304 records with 47 columns

### Common Patterns Observed

#### Facebook Ads Dataset:
- **Most active pages**: Top page had 55,503 ads (22.5% of all ads)
- **Currency**: 99.94% of ads were in USD
- **Platform distribution**: 86.9% used both Facebook and Instagram, 9.4% Facebook only
- **Peak activity**: October 27-28, 2024 saw the highest ad creation (16,000+ ads)
- **Top advertisers**: HARRIS FOR PRESIDENT (49,788 ads), HARRIS VICTORY FUND (32,612 ads)

#### Facebook Posts Dataset:
- **Dominant page**: One page accounted for 47.4% of all posts (9,013 posts)
- **Content types**: Links (44.8%), Photos (23.1%), Native Videos (17.7%)
- **Engagement**: Average likes: 2,377, Average comments: 901, Average shares: 320
- **Peak posting**: October 31, 2024 (103 posts)

#### Twitter Posts Dataset:
- **Platform usage**: Twitter Web App (54.7%), iPhone (31.1%), Sprout Social (10.7%)
- **Engagement metrics**: Average retweets: 1,322, Average likes: 6,913
- **View counts**: Average views: 507,084 (max: 333.5 million)
- **Peak activity**: October 2024 (3,586 tweets, 13.1% of total)

### Data Quality Issues
- **Missing data**: 
  - FB ads: 1,009 missing bylines
  - FB posts: 2,472 missing page categories, 949 missing scam scores
  - Twitter: 1,270 missing various illuminating scores

## Interesting Insights

### 1. **Library Comparison**:
- **Pure Python**: Provided total transparency but required a lot more code (around 200 lines)
- **Pandas**: Most user-friendly, using well-known patterns and moderately long (around 150 lines) code
- **Polars**: The most compact code (around 140 lines) using current syntax

### 2. **Performance Observations**:
- Each of the three methods processed the datasets without experiencing any memory problems
- Polars showed deprecation warnings for `pl.count()`, recommending `pl.len()` instead
- In pure Python, group-by operations were the most complicated and required manual dictionary management

### 3. **Data Characteristics**:
- Heavy concentration of activity from a few major players (the top 5 pages produced about 50% of the content)
- October 2024 showed peak activity across all platforms (pre-election spike)
- Binary categorical fields dominate the "illuminating" columns (mainly 0s and 1s)

### 4. **Platform-Specific Insights**:
- Ads on Facebook primarily targeted Instagram and Facebook at the same time
- The number of people who engaged with posts on Twitter varied greatly; some had millions of views
- Facebook posts were mostly link shares, indicating that they were widely used for content sharing

## Challenges Encountered

### 1. **Deprecation Warnings**:
- Polars displayed warnings for deprecated `pl.count()` function
- Need to update to use `pl.len()` in future versions

### 2. **Different Output Formats**:
- The output formatting varied slightly depending on the library
- Pandas and Polars showed more detailed statistics by default
- Pure Python required manual formatting of all output

### 3. **Memory Considerations**:
- Large datasets (more than 246K rows) needed effective memory management
- Pure Python loaded entire dataset into memory as dictionaries

### 4. **Type Handling**:
- Columns with mixed data types needed to be handled carefully
- String representations of lists/dictionaries in some columns
- String values were occasionally present in numerical columns

## Performance Comparison

According to execution (perceived subjectively):
- **Pure Python**: Noticeably slower on large datasets, but acceptable
- **Pandas**: Fast and efficient with good memory management
- **Polars**: Fastest execution, especially noticeable on the Facebook ads dataset

## Future Improvements

1. **Add timing benchmarks**: Use accurate timing measurements to compare performance
2. **Handle complex data types**: Parse JSON-like strings in delivery_by_region and demographic_distribution columns
3. **Add visualization module**: Create charts showing top pages, temporal trends, and engagement distributions
4. **Implement data cleaning**: Deal with missing values more methodically
5. **Add export functionality**: Create CSV or Excel files with summary statistics
6. **Create unified output format**: For ease of comparison, standardize the output from all three strategies
7. **Add command-line arguments**: Permit users to choose which datasets to examine
8. **Implement parallel processing**: For pure Python version to improve performance
9. **Add more statistical measures**: Include median, quartiles, and correlation analysis
10. **Create automated comparison report**: Create a comparison of the outcomes of the three approaches side by side

## Contact
For inquiries about this analysis, please contact: nepawar@syr.edu

## Acknowledgments
Under Professor Jonathan's guidance, the project completed as part of Syracuse University's research requirements.