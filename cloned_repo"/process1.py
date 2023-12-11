import pandas as pd
import argparse
from datetime import datetime, timedelta

def identify_trips(df):
    
def main():
    parser = argparse.ArgumentParser(description='Process GS data and extract trip information.')
    parser.add_argument('--to_process',help='Path to the Parquet file to be processed',required=True)
    parser.add_argument('--output_dir',help='Output directory to store resulting CSV files',required=True)
    args = parser.parse_args()
    
    parquet_df=pd.read_csv(args.to_process)
    
    trips = identify_trips(parquet_df)
    
    for trip_number, trip_data in enumerate(trips):
        csv_filename = f"{trip_data['unit']}_{trip_number}.CSV"
        csv_path = f"{args.output_dir}/{csv_filename}"
        
        trip_data.to_csv(csv_path,index=False)
        
if __name__ == "__main__":
    main()
