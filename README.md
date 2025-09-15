# DataUtils

A comprehensive Python utility library for data type identification, conversion, and manipulation.

## Features

- **Type Identification**: Robust type checking and identification for Python objects
- **Type Conversion**: Safe and consistent conversion between different data types
- **String Serialization**: Convert complex objects to string representations
- **Collection Utilities**: Specialized handling for various collection types
- **Date/Time Support**: Comprehensive date and time utilities

## Installation

```bash
git clone https://github.com/louisgoodnews/DataUtils.git
```

## Usage

```python
from datautils.core import DataIdentificationUtils, DataConversionUtils

# Type checking
value = "123"
if DataIdentificationUtils.could_be_int(value):
    num = int(value)

# Type conversion
json_str = DataConversionUtils.serialize({"key": "value"})
```

## Documentation

Full documentation is available at [CHANGELOG](CHANGELOG.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
