import json
import logging
import subprocess
import sys
from pathlib import Path
from shapely.geometry import shape

def process_geojson(geojson_path: str) -> str:
    """Process a GeoJSON file and return its bounding box as a string."""
    with Path(geojson_path).open() as f:
        data = json.load(f)

    if data["type"] == "FeatureCollection":
        geometries = [shape(feature["geometry"]) for feature in data["features"]]
    elif data["type"] == "Feature":
        geometries = [shape(data["geometry"])]
    else:
        raise ValueError("Unsupported GeoJSON type")

    combined_geom = geometries[0]
    for geom in geometries[1:]:
        combined_geom = combined_geom.union(geom)

    minx, miny, maxx, maxy = combined_geom.bounds
    return f"{minx},{miny},{maxx},{maxy}"

def download_overture_data(geojson_path: str) -> None:
    """Main function to download Overture Maps data based on a GeoJSON file."""
    logging.basicConfig(level=logging.INFO)
    
    bbox = process_geojson(geojson_path)
    data_types = [
        "address", "building", "building_part", "division", "division_area",
        "division_boundary", "place", "segment", "connector", "infrastructure",
        "land", "land_cover", "land_use", "water"
    ]

    output_dir = Path("overture_data")
    output_dir.mkdir(exist_ok=True)

    for data_type in data_types:
        logging.info("Downloading %s data...", data_type)
        theme_dir = data_type.split("_")[0]
        data_output_dir = output_dir / theme_dir / data_type
        data_output_dir.mkdir(parents=True, exist_ok=True)
        output_file = data_output_dir / f"{data_type}.parquet"

        cmd = [
            "overturemaps", "download", "--bbox", bbox, "-f", "geoparquet",
            "-t", data_type, "-o", str(output_file),
        ]

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            logging.exception("Error downloading %s data", data_type)

