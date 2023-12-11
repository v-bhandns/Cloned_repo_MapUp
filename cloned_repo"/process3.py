import os
import json
import csv
import argparse

def extract_transform_data(json_folder,output_file):
    all_data=[]
    
    for json_file in os.listdir(json_folder):
        if json_file.endwith(".json"):
            json_path = os.path.join(json_folder,json_file)
            
            with open(json_path,'r') as file:
                try:
                    json_data = json.load(file)
                    transformed_data = transform_json_data(json_data,json_file)
                    all_data.extend(transformed_data)
                except json.JSONDecodeError as e:
                    print(f'Error decoding JSON file {json_file}:{e}')
                    
    csv_filename = os.path.join(output_dir, 'transformed_data.csv')
    save_to_csv(all_data,csv_filename)
    
def transform_json_data(json_data, json_file):
    
def save_to_csv(data,csv_filename):
    with open(csv_filename,'w',newline='') as csvfile:
        fieldnames = ['unit','trip_id','toll_loc_id_start','toll_loc_id_end','toll_loc_name_start','toll_loc_name_end','toll_system_type',
                     'entry_time','exit_time','tag_cost','cash_cost','license_plate_cost']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        writer.writerows()
        
def main():
    parser = argparse.ArgumentParser(description='Extract and transform toll information from JSON files.')
    parser.add_argument('json_folder',help='Path to the JSON files folder',type=str)
    parser.add_argument('output_dir',help='Folder where the final transformed_data.csv will be stored',type=str)
    args = parser.parse_args()
    
    extract_transform_data(args.json_folder, args.output_dir)
    
if __name__ == "__main__":
    main()
