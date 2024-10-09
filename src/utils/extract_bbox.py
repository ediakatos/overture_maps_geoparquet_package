import json
import sys
from shapely.geometry import shape

def process_geojson(geojson_path):
    try:
        with open(geojson_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {geojson_path}: {e}")
        return None

    if data['type'] == 'FeatureCollection':
        features = data['features']
        geometries = [shape(feature['geometry']) for feature in features]
    elif data['type'] == 'Feature':
        geometries = [shape(data['geometry'])]
    else:
        print(f"Unsupported GeoJSON type in {geojson_path}")
        return None

    combined_geom = geometries[0]
    for geom in geometries[1:]:
        combined_geom = combined_geom.union(geom)

    minx, miny, maxx, maxy = combined_geom.bounds
    return f"{minx},{miny},{maxx},{maxy}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_bbox.py <path_to_geojson_file>")
        sys.exit(1)

    geojson_path = sys.argv[1]
    bbox = process_geojson(geojson_path)
    if bbox:
        print(bbox)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
