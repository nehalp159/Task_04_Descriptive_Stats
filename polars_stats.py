import polars as pl
import os

def analyze_dataset_polars(filename):
    """analyze dataset using polars"""
    print(f"\n{'='*60}")
    print(f"Polars Analysis for the file: {filename}")
    print(f"{'='*60}")
    
    # read CSV file
    df = pl.read_csv(filename)
    
    print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"\nColumn names: {df.columns}")
    
    # basic information about dataset
    print("\n" + "-"*40)
    print("Dataset Schema")
    print("-"*40)
    print(df.schema)
    
    # using describe() for all columns
    print("\n" + "-"*40)
    print("All Columns Statistics (using describe())")
    print("-"*40)
    stats = df.describe()
    print(stats)
    
    # using n_unique() for all columns (equivalent to nunique())
    print("\n" + "-"*40)
    print("Unique Values Per Column (using n_unique())")
    print("-"*40)
    unique_counts = []
    for col in df.columns:
        unique_count = df[col].n_unique()
        unique_counts.append({"column": col, "unique_values": unique_count})
    unique_df = pl.DataFrame(unique_counts)
    print(unique_df)
    
    # categorical columns analysis with value_counts equivalent
    print("\n" + "-"*40)
    print("Categorical Columns Analysis (using value_counts equivalent)")
    print("-"*40)
    
    # get categorical columns
    categorical_cols = [col for col in df.columns if df[col].dtype == pl.Utf8]
    
    for col in categorical_cols:
        print(f"\n=== Column: {col} ===")
        print(f"Unique values (n_unique()): {df[col].n_unique()}")
        print(f"Null values: {df[col].null_count()}")
        
        # value counts (Polars equivalent)
        print(f"\nTop 10 values (value_counts):")
        value_counts = (
            df.group_by(col)
            .agg(pl.count().alias("count"))
            .sort("count", descending=True)
            .head(10)
        )
        print(value_counts)
        
        # percentage distribution
        total_non_null = df[col].drop_nulls().len()
        if total_non_null > 0:
            print(f"\nPercentage distribution:")
            value_counts_pct = (
                df.group_by(col)
                .agg(pl.count().alias("count"))
                .with_columns(
                    (pl.col("count") / total_non_null * 100).alias("percentage")
                )
                .sort("count", descending=True)
                .head(5)
            )
            print(value_counts_pct)

def group_by_analysis_polars(filename, group_columns):
    """perform group-by analysis using polars"""
    print(f"\n{'='*60}")
    print(f"Polars Group-By Analysis: {filename}")
    print(f"Grouping by: {', '.join(group_columns)}")
    print(f"{'='*60}")
    
    # Read the CSV file
    df = pl.read_csv(filename)
    
    # check if group columns exist
    missing_cols = [col for col in group_columns if col not in df.columns]
    if missing_cols:
        print(f"Warning: Columns {missing_cols} not found in dataset")
        return
    
    # group the data and get counts
    group_counts = (
        df.group_by(group_columns)
        .agg(pl.count().alias("count"))
        .sort("count", descending=True)
    )
    
    print(f"Number of groups: {len(group_counts)}")
    
    # show top 10 groups by size
    print("\nTop 10 groups by size:")
    print(group_counts.head(10))
    
    # show statistics for numeric columns by group
    numeric_cols = [col for col in df.columns if df[col].dtype in [pl.Int64, pl.Float64, pl.Int32, pl.Float32]]
    
    if numeric_cols:
        print("\nGroup statistics for numeric columns:")
        
        # create aggregation expressions
        agg_exprs = []
        for col in numeric_cols:
            agg_exprs.extend([
                pl.col(col).count().alias(f"{col}_count"),
                pl.col(col).mean().alias(f"{col}_mean"),
                pl.col(col).min().alias(f"{col}_min"),
                pl.col(col).max().alias(f"{col}_max")
            ])
        
        if agg_exprs:
            group_stats = df.group_by(group_columns).agg(agg_exprs).head(10)
            print(group_stats)

def main():
    """main function to run all analyses"""
    # define the data directory
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
            analyze_dataset_polars(filepath)
            
            # check which columns exist for group-by analysis
            df = pl.read_csv(filepath)
            
            if 'page_id' in df.columns:
                group_by_analysis_polars(filepath, ['page_id'])
                
            if 'page_id' in df.columns and 'ad_id' in df.columns:
                group_by_analysis_polars(filepath, ['page_id', 'ad_id'])
                
        except FileNotFoundError:
            print(f"\nError: Could not find file {filepath}")
            print("Make sure the file is in the 'data' folder")
        except Exception as e:
            print(f"\nError analyzing {csv_file}: {str(e)}")

if __name__ == "__main__":
    main()