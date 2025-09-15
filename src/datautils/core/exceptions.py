"""
Author: Louis Goodnews
Date: 2025-09-15
"""

from typing import Any, Final, Union


__all__: Final[list[str]] = ["DataConversionError", "DataIdentificationError"]


class DataConversionError(Exception):
    """
    Base exception class. Raised when a data conversion fails with any semi arbitrary error.
    """

    def __init__(
        self,
        value: Any,
        type_: Union[str, type],
    ) -> None:
        """
        Initialize the exception with the value and target.

        Args:
            value (Any): The value to convert.
            type_ (Union[str, type]): The target type to convert to.

        Returns:
            None
        """

        # Use the type name if target is a type, otherwise use the string representation
        super().__init__(
            f"Failed to convert {value} to {type_ if isinstance(type_, str) else type_.__name__}"
        )


class DataIdentificationError(Exception):
    """
    Raised when a data identification fails.
    """
