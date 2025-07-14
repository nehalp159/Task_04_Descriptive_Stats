import csv
import math
from collections import Counter
import os

def read_csv_file(filename):
    """read csv file & return headers & data"""
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            data.append(row)
    return headers, data

def is_numeric(value):
    """check if value can be converted to a number"""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def calculate_mean(numbers):
    """calculate average of a list of numbers"""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def calculate_std_dev(numbers):
    """calculate standard deviation"""
    if not numbers or len(numbers) < 2:
        return None
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    return math.sqrt(variance)

def analyze_column(data, column_name):
    """analyze single column of data"""
    values = [row[column_name] for row in data if row[column_name]]
    
    # check if column is numeric
    numeric_values = []
    for val in values:
        if is_numeric(val):
            numeric_values.append(float(val))
    
    results = {
        'column': column_name,
        'count': len(values),
        'missing': len(data) - len(values)
    }
    
    if numeric_values and len(numeric_values) == len(values):
        # this is numeric column
        results['type'] = 'numeric'
        results['mean'] = calculate_mean(numeric_values)
        results['min'] = min(numeric_values)
        results['max'] = max(numeric_values)
        results['std_dev'] = calculate_std_dev(numeric_values)
    else:
        # this is text/categorical column
        results['type'] = 'categorical'
        value_counts = Counter(values)
        results['unique_values'] = len(value_counts)
        results['most_common'] = value_counts.most_common(5)
    
    return results

def analyze_dataset(filename):
    """analyze entire dataset"""
    print(f"\n{'='*60}")
    print(f"Analyzing the file: {filename}")
    print(f"{'='*60}")
    
    headers, data = read_csv_file(filename)
    print(f"Total rows: {len(data)}")
    print(f"Total columns: {len(headers)}")
    
    # analyze each column
    print("\n" + "-"*40)
    print("Column Analysis")
    print("-"*40)
    
    for column in headers:
        results = analyze_column(data, column)
        
        print(f"\nColumn: {results['column']}")
        print(f"  Type: {results['type']}")
        print(f"  Count: {results['count']}")
        print(f"  Missing: {results['missing']}")
        
        if results['type'] == 'numeric':
            print(f"  Mean: {results['mean']:.2f}")
            print(f"  Min: {results['min']:.2f}")
            print(f"  Max: {results['max']:.2f}")
            if results['std_dev']:
                print(f"  Std Dev: {results['std_dev']:.2f}")
        else:
            print(f"  Unique values: {results['unique_values']}")
            print(f"  Most common values:")
            for value, count in results['most_common']:
                print(f"    '{value}': {count} times")

def group_by_analysis(filename, group_columns):
    """analyze data grouped by specific columns"""
    print(f"\n{'='*60}")
    print(f"Group-By Analysis: {filename}")
    print(f"Grouping by: {', '.join(group_columns)}")
    print(f"{'='*60}")
    
    headers, data = read_csv_file(filename)
    
    # create groups
    groups = {}
    for row in data:
        # create a key from group columns
        key = tuple(row.get(col, 'NA') for col in group_columns)
        if key not in groups:
            groups[key] = []
        groups[key].append(row)
    
    print(f"Number of groups: {len(groups)}")
    
    # show top 5 groups by size
    sorted_groups = sorted(groups.items(), key=lambda x: len(x[1]), reverse=True)
    print("\nTop 5 groups by size:")
    for i, (key, group_data) in enumerate(sorted_groups[:5]):
        print(f"  Group {i+1}: {key} - {len(group_data)} rows")

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
            analyze_dataset(filepath)
            
            # group-by analysis (checking if columns exist)
            headers, _ = read_csv_file(filepath)
            
            if 'page_id' in headers:
                group_by_analysis(filepath, ['page_id'])
                
            if 'page_id' in headers and 'ad_id' in headers:
                group_by_analysis(filepath, ['page_id', 'ad_id'])
                
        except FileNotFoundError:
            print(f"\nError: Could not find file {filepath}")
            print("Make sure the file is in the 'data' folder")
        except Exception as e:
            print(f"\nError analyzing {csv_file}: {str(e)}")

if __name__ == "__main__":
    main()