import json
import sys
from shapely.geometry import shape

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_bbox.py <path_to_tcd.json>")
        sys.exit(1)

    geojson_path = sys.argv[1]

    with open(geojson_path, 'r') as f:
        data = json.load(f)

    if data['type'] == 'FeatureCollection':
        features = data['features']
        geometries = [shape(feature['geometry']) for feature in features]
    elif data['type'] == 'Feature':
        geometries = [shape(data['geometry'])]
    else:
        print("Unsupported GeoJSON type")
        sys.exit(1)

    combined_geom = geometries[0]
    for geom in geometries[1:]:
        combined_geom = combined_geom.union(geom)

    minx, miny, maxx, maxy = combined_geom.bounds

    print(f"{minx},{miny},{maxx},{maxy}")

if __name__ == '__main__':
    main()
