import pandas as pd
import os

def analyze_dataset_pandas(filename):
    """analyze dataset using pandas"""
    print(f"\n{'='*60}")
    print(f"Pandas Analysis for the file: {filename}")
    print(f"{'='*60}")
    
    # read CSV file
    df = pd.read_csv(filename)
    
    print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"\nColumn names: {list(df.columns)}")
    
    # basic information about dataset
    print("\n" + "-"*40)
    print("Dataset Info")
    print("-"*40)
    print(df.info())
    
    # using describe() for numeric columns
    print("\n" + "-"*40)
    print("Numeric Columns Statistics (using describe())")
    print("-"*40)
    numeric_stats = df.describe()
    print(numeric_stats)
    
    # additional percentiles
    print("\n" + "-"*40)
    print("Additional Percentiles")
    print("-"*40)
    print(df.describe(percentiles=[.1, .25, .5, .75, .9]))
    
    # using nunique() for all columns
    print("\n" + "-"*40)
    print("Unique Values Per Column (using nunique())")
    print("-"*40)
    unique_counts = df.nunique()
    print(unique_counts)
    
    # categorical columns analysis with value_counts()
    print("\n" + "-"*40)
    print("Categorical Clumns Analysis (using value_counts())")
    print("-"*40)
    
    # get categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    for col in categorical_cols:
        print(f"\n=== Column: {col} ===")
        print(f"Unique values (nunique()): {df[col].nunique()}")
        print(f"Missing values: {df[col].isna().sum()}")
        print(f"\nTop 10 values (value_counts()):")
        print(df[col].value_counts().head(10))
        
        # show percentage distribution for top values
        print(f"\nPercentage distribution (value_counts with normalize):")
        print(df[col].value_counts(normalize=True).head(5) * 100)

def group_by_analysis_pandas(filename, group_columns):
    """perform group-by analysis using pandas"""
    print(f"\n{'='*60}")
    print(f"Pandas Group-By Analysis: {filename}")
    print(f"Grouping by: {', '.join(group_columns)}")
    print(f"{'='*60}")
    
    # read CSV file
    df = pd.read_csv(filename)
    
    # check if group columns exist
    missing_cols = [col for col in group_columns if col not in df.columns]
    if missing_cols:
        print(f"Warning: Columns {missing_cols} not found in dataset")
        return
    
    # group the data
    grouped = df.groupby(group_columns)
    
    print(f"Number of groups: {len(grouped)}")
    
    # show group sizes
    group_sizes = grouped.size().sort_values(ascending=False)
    print("\nTop 10 groups by size:")
    print(group_sizes.head(10))
    
    # show statistics for numeric columns by group
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 0:
        print("\nGroup statistics for numeric columns:")
        print(grouped[numeric_cols].agg(['count', 'mean', 'min', 'max']).head(10))

def main():
    """main function to run all analyses"""
    # define data directory
    data_dir = "data"
    
    # list of CSV files to analyze
    csv_files = [
        "2024_fb_ads_president_scored_anon.csv",
        "2024_fb_posts_president_scored_anon.csv",
        "2024_tw_posts_president_scored_anon.csv"
    ]
    
    # analyze each file
    for csv_file in csv_files:
        filepath = os.path.join(data_dir, csv_file)
        
        try:
            # basic analysis
            analyze_dataset_pandas(filepath)
            
            # check which columns exist for group-by analysis
            df = pd.read_csv(filepath)
            
            if 'page_id' in df.columns:
                group_by_analysis_pandas(filepath, ['page_id'])
                
            if 'page_id' in df.columns and 'ad_id' in df.columns:
                group_by_analysis_pandas(filepath, ['page_id', 'ad_id'])
                
        except FileNotFoundError:
            print(f"\nError: Could not find file {filepath}")
            print("Make sure the file is in the 'data' folder")
        except Exception as e:
            print(f"\nError analyzing {csv_file}: {str(e)}")

if __name__ == "__main__":
    main()