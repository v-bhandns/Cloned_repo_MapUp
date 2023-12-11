import os
import requests
import argparse
from dotenv import load_dotenv

load_dotenv()

TOLLGURU_API_KEY = os.getenv("TOLLGURU_API_KEY")
TOLLGURU_API_URL = os.getenv("TOLLGURU_API_URL")
UPLOAD_ENDPOINT = "/gps-tracks-csv-upload"

def upload_gps_tracks(vehicle_file):
    
def main():
    parser = argparser.ArgumentParser(description="Upload GPS tracks to TollGuru API.")
    #parser = argparser.ArgumentParser(description='Process GS data and extract trip information.')
    #parser.add_argument('--to_process',help='Path to the Parquet file to be processed',required=True)
    #parser.add_argument('--output_dir',help='Output directory to store resulting CSV files',required=True)
    #args = parser.parse_args()
    parser.add_argument('--process_output_dir',help="Directory containing processed CSV files",required=True)
    args = parser.parser_args()
    
    for csv_file in os.listdir(args.process_output_dir):
        if csv_file.endwith(".CSV"):
            csv_path = os.path.join(args.process_output_dir,csv_file)
            
        uplaod_gps_tracks(csv_path)
        
if __name__ == "__main__":
    main()
