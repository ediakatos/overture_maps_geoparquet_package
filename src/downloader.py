import subprocess
import os
import sys

def main():
    json_dir = './json'
    extract_bbox_script = './src/utils/extract_bbox.py'

    if not os.path.isdir(json_dir):
        print(f"{json_dir} is not a valid directory")
        sys.exit(1)

    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            geojson_path = os.path.join(json_dir, filename)
            try:
                print(f"Extracting bounding box for {filename}...")
                bbox = subprocess.check_output(['python', extract_bbox_script, geojson_path]).decode().strip()
                print(f"Bounding box for {filename}: {bbox}")
            except subprocess.CalledProcessError as e:
                print(f"Error extracting bounding box for {filename}: {e.output.decode()}")
                continue
            except Exception as e:
                print(f"Unexpected error extracting bounding box for {filename}: {e}")
                continue

            data_types = [
                'address',
                'building',
                'building_part',
                'division',
                'division_area',
                'division_boundary',
                'place',
                'segment',
                'connector',
                'infrastructure',
                'land',
                'land_cover',
                'land_use',
                'water'
            ]

            output_dir = 'overture_data'
            os.makedirs(output_dir, exist_ok=True)

            for data_type in data_types:
                print(f'Downloading {data_type} data for {filename}...')

                theme_dir = data_type.split('_')[0]
                data_output_dir = os.path.join(output_dir, theme_dir, data_type)
                os.makedirs(data_output_dir, exist_ok=True)

                output_file = os.path.join(data_output_dir, f'{data_type}.parquet')

                cmd = [
                    'overturemaps',
                    'download',
                    '--bbox', bbox,
                    '-f', 'geoparquet',
                    '-t', data_type,
                    '-o', output_file
                ]

                try:
                    subprocess.run(cmd, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error downloading {data_type} data for {filename}: {e.output.decode()}")
                    continue
                except Exception as e:
                    print(f"Unexpected error downloading {data_type} data for {filename}: {e}")
                    continue

if __name__ == "__main__":
    main()