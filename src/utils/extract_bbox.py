"""Utility script to extract bounding box from a GeoJSON file."""

import json
import logging
import sys
from pathlib import Path

from shapely.geometry import shape

ARG_COUNT = 2


def process_geojson(geojson_path: str) -> str | None:
    """Process a GeoJSON file and return its bounding box as a string."""
    try:
        with Path(geojson_path).open() as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.exception("Error reading %s", geojson_path)
        return None

    if data["type"] == "FeatureCollection":
        features = data["features"]
        geometries = [shape(feature["geometry"]) for feature in features]
    elif data["type"] == "Feature":
        geometries = [shape(data["geometry"])]
    else:
        logging.error("Unsupported GeoJSON type in %s", geojson_path)
        return None

    combined_geom = geometries[0]
    for geom in geometries[1:]:
        combined_geom = combined_geom.union(geom)

    minx, miny, maxx, maxy = combined_geom.bounds
    return f"{minx},{miny},{maxx},{maxy}"


def main() -> None:
    """Main function to extract bounding box from a GeoJSON file."""
    if len(sys.argv) != ARG_COUNT:
        logging.error("Usage: python extract_bbox.py <path_to_geojson_file>")
        sys.exit(1)

    geojson_path = sys.argv[1]
    bbox = process_geojson(geojson_path)
    if bbox:
        sys.stdout.write(bbox + "\n")  # Replace print statement with stdout.write
    else:
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
