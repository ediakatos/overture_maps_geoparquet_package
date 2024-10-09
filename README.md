
# Overture Maps GeoParquet Project

This project processes GeoJSON files to extract bounding boxes
and download corresponding data in GeoParquet format using the Overture Maps API.

## Project Structure

```text
├── countries
├── json
│   └── zwe.json
├── LICENSE
├── Makefile
├── poetry.lock
├── poetry.toml
├── pyproject.toml
├── README.md
├── requirements.txt
├── src
│   ├── downloader.py
│   ├── __init__.py
│   └── utils
│       ├── extract_bbox.py
│       └── __init__.py
└── tests
    ├── example
    │   ├── __init__.py
    │   └── test_example.py
    └── __init__.py
```

## Requirements

- Python 3.10+
- Poetry

## Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install project dependencies:

    ```sh
    make .venv
    ```

3. Add pre-commit hooks:

    ```sh
    make hooks
    ```

## Usage

### Running the Application

To run the application:

```sh
make run
```

### Running Tests

To run unit tests:

```sh
make test
```

### Running Lint Tests

To run lint tests:

```sh
make lint
```

### Cleaning Up

To remove the virtual environment:

```sh
make clean
```

### Installing Additional Requirements

To install additional requirements from `requirements.txt`:

```sh
make install-requirements
```

## Available Make Commands

- `make help` - Print help
- `make .venv` - Install project dependencies
- `make hooks` - Add pre-commit hooks
- `make test` - Run unit tests
- `make lint` - Run lint tests
- `make clean` - Remove the virtual environment
- `make install-requirements` - Install additional requirements from `requirements.txt`
- `make run` - Run the application

## License
