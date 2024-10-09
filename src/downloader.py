import subprocess
import os
import sys

def main():
    geojson_path = './json/tcd.json'
    extract_bbox_script = './src/utils/extract_bbox.py'

    try:
        bbox = subprocess.check_output(['python', extract_bbox_script, geojson_path]).decode().strip()
    except Exception as e:
        print(f"Error extracting bounding box: {e}")
        sys.exit(1)

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
        print(f'Downloading {data_type} data...')

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
            print(f'{data_type} data saved to {output_file}')
        except subprocess.CalledProcessError:
            print(f'Failed to download {data_type} data.')
        except Exception as e:
            print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
