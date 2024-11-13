
# Overture Maps Geoparquet Package

![PyPI](https://img.shields.io/pypi/v/overture_maps_geoparquet_package)
![License](https://img.shields.io/pypi/l/overture_maps_geoparquet_package)
![Python](https://img.shields.io/pypi/pyversions/overture_maps_geoparquet_package)

## Overview

The **Overture Maps Geoparquet Package** is a Python library designed for downloading and processing geospatial data from Overture Maps in a user-friendly way. This package allows users to specify an Area of Interest (AOI) through a GeoJSON file, automatically extract its bounding box, and download relevant geospatial data types, such as buildings, land use, and infrastructure, in GeoParquet format.

## Features

- **Automated Bounding Box Extraction**: Parses a GeoJSON file and extracts the bounding box for easy area targeting.
- **Flexible Data Downloading**: Downloads various data types (e.g., buildings, infrastructure) in GeoParquet format for efficient storage and analysis.
- **Easy Command-Line and Script Integration**: The package provides a simple interface, allowing users to start the download process with a single function call.
- **Data Organization**: Downloads are organized into folders based on the AOI and data type, keeping data management straightforward.

## Installation

To install the package, use `pip`:

```bash
pip install overture_maps_geoparquet_package
```

## Usage

Here’s a quick guide on how to use the package:

1. **Prepare a GeoJSON File**

   Create a GeoJSON file that defines your area of interest (AOI). Save it in your project directory (e.g., `my_area.json`).

2. **Run the Download Function**

   Import and call `download_overture_data`, passing the path to your GeoJSON file:

   ```python
   from overture_maps_geoparquet_package import download_overture_data

   # Download geospatial data for the specified area
   download_overture_data("my_area.json")
   ```

   This will:
   - Extract the bounding box from your GeoJSON file.
   - Download geospatial data (e.g., buildings, land use, infrastructure) for the AOI.
   - Save the data in organized folders within the current directory.

### Example

```python
from overture_maps_geoparquet_package import download_overture_data

# Specify the path to your GeoJSON file
geojson_path = "path/to/your_area.json"

# Start the download process
download_overture_data(geojson_path)
```

This code will automatically download the specified data types in GeoParquet format, organized by type.

## Data Types Supported

The following data types are downloaded for each AOI:
- **address**
- **building**
- **division**
- **infrastructure**
- **land use**
- **water**
- And more...

Each type is saved in a folder structure organized by data category.

## Project Structure

The project follows a standard layout:
```
overture_maps_geoparquet_package/
├── json/                 # Stores GeoJSON files
├── overture_data/        # Downloaded data, organized by AOI and type
├── src/                  # Source code for the package
├── tests/                # Unit tests
├── README.md             # Project documentation
├── pyproject.toml        # Project configuration
└── requirements.txt      # Dependency management
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for feature requests, bug fixes, or improvements.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the GPL-3.0 License. See the `LICENSE` file for more details.

## Contact

For questions, please contact **ediakatos@mapaction.org**.
