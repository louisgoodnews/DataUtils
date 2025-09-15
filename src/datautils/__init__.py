"""
Author: Louis Goodnews
Date: 2025-09-15
"""

from typing import Final, Literal

from .core.core import DataConversionUtils, DataIdentificationUtils


__all__: Final[list[str]] = [
    "DataConversionUtils",
    "DataIdentificationUtils",
]

__version__: Final[Literal["0.1.0"]] = "0.1.0"
