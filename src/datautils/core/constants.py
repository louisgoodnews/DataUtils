"""
Author: Louis Goodnews
Date: 2025-09-15
"""

from typing import Final


__all__: Final[list[str]] = ["PYDANTIC_AVAILABLE"]


try:
    from pydantic import BaseModel

    PYDANTIC_AVAILABLE: Final[bool] = True
except ImportError:
    PYDANTIC_AVAILABLE: Final[bool] = False
