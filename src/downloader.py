"""Downloader script for Overture Maps data."""

import logging
import shlex
import subprocess
import sys
from pathlib import Path


def main() -> None:
    """Main function to download Overture Maps data."""
    logging.basicConfig(level=logging.INFO)

    json_dir = Path("./json")
    extract_bbox_script = Path("./src/utils/extract_bbox.py")

    if not json_dir.is_dir():
        logging.error("%s is not a valid directory", json_dir)
        sys.exit(1)

    for filename in json_dir.iterdir():
        if filename.suffix == ".json":
            geojson_path = filename
            try:
                logging.info("Extracting bounding box for %s...", filename.name)
                bbox_command = [
                    sys.executable,
                    str(extract_bbox_script),
                    str(geojson_path),
                ]
                bbox = subprocess.check_output(bbox_command, text=True).strip()  # noqa: S603
                logging.info("Bounding box for %s: %s", filename.name, bbox)
            except subprocess.CalledProcessError:
                logging.exception("Error extracting bounding box for %s", filename.name)
                continue
            except (OSError, subprocess.SubprocessError):
                logging.exception(
                    "Unexpected error extracting bounding box for %s",
                    filename.name,
                )
                continue

            data_types = [
                "address",
                "building",
                "building_part",
                "division",
                "division_area",
                "division_boundary",
                "place",
                "segment",
                "connector",
                "infrastructure",
                "land",
                "land_cover",
                "land_use",
                "water",
            ]

            output_dir = Path("overture_data")
            output_dir.mkdir(exist_ok=True)

            for data_type in data_types:
                logging.info("Downloading %s data for %s...", data_type, filename.name)

                theme_code = filename.stem[-3:]
                theme_dir = data_type.split("_")[0]
                data_output_dir = output_dir / theme_code / theme_dir / data_type
                data_output_dir.mkdir(parents=True, exist_ok=True)

                output_file = data_output_dir / f"{data_type}.parquet"

                cmd = [
                    "overturemaps",
                    "download",
                    "--bbox",
                    shlex.quote(bbox),
                    "-f",
                    "geoparquet",
                    "-t",
                    data_type,
                    "-o",
                    str(output_file),
                ]

                try:
                    subprocess.run(cmd, check=True)  # noqa: S603
                except subprocess.CalledProcessError:
                    logging.exception(
                        "Error downloading %s data for %s",
                        data_type,
                        filename.name,
                    )
                    continue
                except (OSError, subprocess.SubprocessError):
                    logging.exception(
                        "Unexpected error downloading %s data for %s",
                        data_type,
                        filename.name,
                    )
                    continue


if __name__ == "__main__":
    main()
