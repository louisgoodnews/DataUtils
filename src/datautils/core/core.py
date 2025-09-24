"""
Author: Louis Goodnews
Date: 2025-09-15
"""

import json

from collections import Counter, defaultdict, deque
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from frozendict import frozendict
from pathlib import Path
from typing import Any, Final, Literal, Mapping, Optional, Set, Union
from uuid import UUID

from .exceptions import DataConversionError


__all__: Final[list[str]] = [
    "DataConversionUtils",
    "DataIdentificationUtils",
]


class DataConversionUtils:
    """
    A collection of utility functions for data conversion.
    """

    @classmethod
    def bytes_to_str(
        cls,
        value: bytes,
    ) -> str:
        """
        Convert bytes to a string.

        Args:
            value (bytes): The bytes to convert.

        Returns:
            str: The string representation of the bytes.
        """

        return value.decode(encoding="utf-8")

    @classmethod
    def complex_to_str(
        cls,
        value: complex,
    ) -> str:
        """
        Convert a complex number to a string.

        Args:
            value (complex): The complex number to convert.

        Returns:
            str: The string representation of the complex number.
        """

        return cls.to_str(value=value)

    @classmethod
    def convert_to_str(
        cls,
        value: Any,
        format: Literal["json", "simple"] = "simple",
    ) -> str:
        """
        Convert a value to a string.

        Args:
            value (Any): The value to convert.
            format (Literal["json", "simple"]): The format to use. Defaults to "simple".

        Returns:
            str: The string representation of the value.
        """

        # Check if the value is a primitive type
        if DataIdentificationUtils.is_primitive_type(value=value):
            # Convert the value to a string
            return cls.to_str(value=value)

        # Check if the value is a date
        elif DataIdentificationUtils.is_date(value=value):
            # Convert the date to a string
            return cls.date_to_str(value=value)

        # Check if the value is a datetime
        elif DataIdentificationUtils.is_datetime(value=value):
            # Convert the datetime to a string
            return cls.datetime_to_str(value=value)

        # Check if the value is a decimal
        elif DataIdentificationUtils.is_decimal(value=value):
            # Convert the decimal to a string
            return cls.decimal_to_str(value=value)

        # Check if the value is a dictionary
        elif DataIdentificationUtils.is_dict(value=value):
            # Convert the dictionary to a string
            return cls.dict_to_str(
                format=format,
                value=value,
            )

        # Check if the value is a list
        elif DataIdentificationUtils.is_list(value=value):
            # Convert the list to a string
            return cls.list_to_str(
                format=format,
                value=value,
            )

        # Check if the value is a path
        elif DataIdentificationUtils.is_path(value=value):
            # Convert the path to a string
            return cls.path_to_str(value=value)

        # Check if the value is a time
        elif DataIdentificationUtils.is_time(value=value):
            # Convert the time to a string
            return cls.time_to_str(value=value)

        # Check if the value is a timedelta
        elif DataIdentificationUtils.is_timedelta(value=value):
            # Convert the timedelta to a string
            return cls.timedelta_to_str(value=value)

        # Check if the value is a timezone
        elif DataIdentificationUtils.is_timezone(value=value):
            # Convert the timezone to a string
            return cls.timezone_to_str(value=value)

        # Check if the value is a set
        elif DataIdentificationUtils.is_set(value=value):
            # Convert the set to a string
            return cls.set_to_str(
                format=format,
                value=value,
            )

        # Check if the value is a UUID
        elif DataIdentificationUtils.is_uuid(value=value):
            # Convert the UUID to a string
            return cls.uuid_to_str(value=value)

        # Default to string conversion
        return cls.to_str(value=value)

    @classmethod
    def counter_to_str(
        cls,
        value: Counter,
    ) -> str:
        """
        Convert a counter to a string.

        Args:
            value (Counter): The counter to convert.

        Returns:
            str: The string representation of the counter.
        """

        return cls.dict_to_str(value=value)

    @classmethod
    def date_to_str(
        cls,
        value: date,
        format: Optional[str] = None,
    ) -> Optional[str]:
        """
        Convert a date to a string.

        Args:
            value (date): The date to convert.
            format (Optional[str]): The format to use. Defaults to None.

        Returns:
            Optional[str]: The string representation of the date or None if the value is not a date.
        """

        # Check if the passed value is a date object
        if not isinstance(
            value,
            date,
        ):
            # Return None if the value is not a date
            return None

        # Return the string representation of the date
        return value.strftime(format=format) if format else value.isoformat()

    @classmethod
    def datetime_to_str(
        cls,
        value: datetime,
        format: Optional[str] = None,
    ) -> Optional[str]:
        """
        Convert a datetime to a string.

        Args:
            value (datetime): The datetime to convert.
            format (Optional[str]): The format to use. Defaults to None.

        Returns:
            Optional[str]: The string representation of the datetime or None if the value is not a datetime.
        """

        # Check if the passed value is a datetime object
        if not isinstance(
            value,
            datetime,
        ):
            # Return None if the value is not a datetime
            return None

        # Return the string representation of the datetime
        return value.strftime(format=format) if format else value.isoformat()

    @classmethod
    def decimal_to_str(
        cls,
        value: Decimal,
    ) -> str:
        """
        Convert a decimal to a string.

        Args:
            value (Decimal): The decimal to convert.

        Returns:
            str: The string representation of the decimal.
        """

        return cls.to_str(value=value)

    @classmethod
    def defaultdict_to_str(
        cls,
        value: defaultdict,
        format: Literal["json", "simple"] = "simple",
    ) -> str:
        """
        Convert a defaultdict to a string.

        Args:
            value (defaultdict): The defaultdict to convert.
            format (Literal["json", "simple"]): The format to use. Defaults to "simple".

        Returns:
            str: The string representation of the defaultdict.
        """

        return cls.dict_to_str(
            format=format,
            value=value,
        )

    @classmethod
    def deque_to_str(
        cls,
        value: deque,
        format: Literal["json", "simple"] = "simple",
    ) -> str:
        """
        Convert a deque to a string.

        Args:
            value (deque): The deque to convert.
            format (Literal["json", "simple"]): The format to use. Defaults to "simple".

        Returns:
            str: The string representation of the deque.
        """

        return cls.list_to_str(
            format=format,
            value=value,
        )

    @classmethod
    def deserialize(
        cls,
        value: str,
    ) -> Any:
        """
        Deserialize a string to its original type.

        Args:
            value (str): The string to deserialize.

        Returns:
            Any: The original type of the string.
        """

        def _deserialize(value: Any) -> Any:
            """ """

            # Check if the value is a boolean
            if DataIdentificationUtils.could_be_bool(value=value):
                # Return the boolean value
                return cls.str_to_bool(value=value)

            # Check if the value is a complex number
            elif DataIdentificationUtils.could_be_complex(value=value):
                # Return the complex value
                return cls.str_to_complex(value=value)

            # Check if the value is a date
            elif DataIdentificationUtils.could_be_date(value=value):
                # Return the date value
                return cls.str_to_date(value=value)

            # Check if the value is a datetime
            elif DataIdentificationUtils.could_be_datetime(value=value):
                # Return the datetime value
                return cls.str_to_datetime(value=value)

            # Check if the value is a decimal
            elif DataIdentificationUtils.could_be_decimal(value=value):
                # Return the decimal value
                return cls.str_to_decimal(value=value)

            # Check if the value is a deque
            elif DataIdentificationUtils.could_be_deque(value=value):
                # Return the deque value
                return cls.str_to_deque(value=value)

            # Check if the value is a dictionary
            elif DataIdentificationUtils.could_be_dict(value=value):
                # Return the dictionary value
                return {
                    key: _deserialize(value=value)
                    for (
                        key,
                        value,
                    ) in cls.str_to_dict(value=value).items()
                }

            # Check if the value is a default dictionary
            elif DataIdentificationUtils.could_be_defaultdict(value=value):
                # Return the default dictionary value
                return defaultdict(
                    _deserialize(value=value), cls.str_to_defaultdict(value=value)
                )

            # Check if the value is a fraction
            elif DataIdentificationUtils.could_be_fraction(value=value):
                # Return the fraction value
                return cls.str_to_fraction(value=value)

            # Check if the value is a frozendict
            elif DataIdentificationUtils.could_be_frozendict(value=value):
                # Return the frozendict value
                return frozendict(
                    {
                        key: _deserialize(value=value)
                        for (
                            key,
                            value,
                        ) in cls.str_to_frozendict(value=value).items()
                    }
                )

            # Check if the value is a frozenset
            elif DataIdentificationUtils.could_be_frozenset(value=value):
                # Return the frozenset value
                return frozenset(
                    _deserialize(value=value)
                    for value in cls.str_to_frozenset(value=value)
                )

            # Check if the value is a set
            elif DataIdentificationUtils.could_be_set(value=value):
                # Return the set value
                return set(
                    _deserialize(value=value) for value in cls.str_to_set(value=value)
                )

            # Check if the value is a time
            elif DataIdentificationUtils.could_be_time(value=value):
                # Return the time value
                return cls.str_to_time(value=value)

            # Check if the value is a timedelta
            elif DataIdentificationUtils.could_be_timedelta(value=value):
                # Return the timedelta value
                return cls.str_to_timedelta(value=value)

            # Check if the value is a timezone
            elif DataIdentificationUtils.could_be_timezone(value=value):
                # Return the timezone value
                return cls.str_to_timezone(value=value)

            # Check if the value is a UUID
            elif DataIdentificationUtils.could_be_uuid(value=value):
                # Return the UUID value
                return cls.str_to_uuid(value=value)

            # Check if the value is a path
            elif DataIdentificationUtils.could_be_path(value=value):
                # Return the path value
                return cls.str_to_path(value=value)

            # Check if the value is a counter
            elif DataIdentificationUtils.could_be_counter(value=value):
                # Return the counter value
                return cls.str_to_counter(value=value)

            # Check if the value is a bytes object
            elif DataIdentificationUtils.could_be_bytes(value=value):
                # Return the bytes object
                return cls.str_to_bytes(value=value)

        # Convert the string to a JSON object
        result: Union[dict[str, Any], list[Any]] = json.loads(value)

        # Check if the result is a dictionary
        if isinstance(
            result,
            dict,
        ):
            # Deserialize the dictionary
            return {
                key: _deserialize(value=value)
                for (
                    key,
                    value,
                ) in result.items()
            }

        # Check if the result is a list
        elif isinstance(
            result,
            list,
        ):
            # Deserialize the list
            return [_deserialize(value=value) for value in result]

    @classmethod
    def dict_to_str(
        cls,
        value: dict[str, Any],
        format: Literal["json", "simple"] = "simple",
    ) -> str:
        """
        Convert a dictionary to a string.

        Args:
            value (dict[str, Any]): The dictionary to convert.

        Returns:
            str: The string representation of the dictionary.
        """

        # Check if the format is supposed to be JSON
        if format == "json":
            # Return the string representation of the dictionary in JSON format
            return json.dumps(value)

        # Join the string representation of each element in the dictionary with ", "
        return ", ".join(map(str, value))

    @classmethod
    def frozendict_to_str(
        cls,
        value: Mapping[str, Any],
        format: Literal["json", "simple"] = "simple",
    ) -> str:
        """
        Convert a frozendict to a string.

        Args:
            value (Mapping[str, Any]): The frozendict to convert.

        Returns:
            str: The string representation of the frozendict.
        """

        return cls.dict_to_str(
            format=format,
            value=value,
        )

    @classmethod
    def frozenset_to_str(
        cls,
        value: frozenset[Any],
        format: Literal["json", "simple"] = "simple",
    ) -> str:
        """
        Convert a frozenset to a string.

        Args:
            value (frozenset[Any]): The frozenset to convert.
            format (Literal["json", "simple"]): The format to use. Defaults to "simple".

        Returns:
            str: The string representation of the frozenset.
        """

        # Check if the format is supposed to be JSON
        if format == "json":
            # Return the string representation of the frozenset in JSON format
            return json.dumps(value)

        # Join the string representation of each element in the frozenset with ", "
        return ", ".join(map(str, value))

    @classmethod
    def list_to_str(
        cls,
        value: list[Any],
        format: Literal["json", "simple"] = "simple",
    ) -> str:
        """
        Convert a list to a string.

        Args:
            value (list[Any]): The list to convert.
            format (Literal["json", "simple"]): The format to use. Defaults to "simple".

        Returns:
            str: The string representation of the list.
        """

        # Check if the format is supposed to be JSON
        if format == "json":
            # Return the string representation of the list in JSON format
            return json.dumps(value)

        # Join the string representation of each element in the list with ", "
        return ", ".join(
            map(
                str,
                value,
            )
        )

    @classmethod
    def path_to_str(
        cls,
        value: Path,
    ) -> str:
        """
        Convert a path to a string.

        Args:
            value (Path): The path to convert.

        Returns:
            str: The string representation of the path.
        """

        return cls.to_str(value=value)

    @classmethod
    def set_to_str(
        cls,
        value: set[Any],
        format: Literal["json", "simple"] = "simple",
    ) -> str:
        """
        Convert a set to a string.

        Args:
            value (set[Any]): The set to convert.
            format (Literal["json", "simple"]): The format to use. Defaults to "simple".

        Returns:
            str: The string representation of the set.
        """

        return cls.list_to_str(
            value=list(value),
            format=format,
        )

    @classmethod
    def serialize(
        cls,
        value: Any,
    ) -> str:
        """
        Serialize a value to a string.

        Args:
            value (Any): The value to serialize.

        Returns:
            str: The string representation of the value.
        """

        def _serialize(value: Any) -> Any:
            """
            Serialize a value to a string.

            Args:
                value (Any): The value to serialize.

            Returns:
                Any: The string representation of the value.
            """

            # Check if the value is a primitive type
            if DataIdentificationUtils.is_primitive_type(value=value):
                # Serialize a primitive type
                return cls.to_str(value=value)

            # Check if the value is a dictionary
            elif DataIdentificationUtils.is_dict(value=value):
                # Serialize a dictionary
                return {
                    key: _serialize(value=item)
                    for (
                        key,
                        item,
                    ) in value.items()
                }

            # Check if the value is a frozen dictionary
            elif DataIdentificationUtils.is_frozendict(value=value):
                # Serialize a frozen dictionary
                return {
                    key: _serialize(value=item)
                    for (
                        key,
                        item,
                    ) in value.items()
                }

            # Check if the value is a list
            elif DataIdentificationUtils.is_list(value=value):
                # Serialize a list
                return [_serialize(item) for item in value]

            # Check if the value is a counter
            elif DataIdentificationUtils.is_counter(value=value):
                # Serialize a counter
                return cls.counter_to_str(value=value)

            # Check if the value is a defaultdict
            elif DataIdentificationUtils.is_defaultdict(value=value):
                # Serialize a defaultdict
                return {
                    key: _serialize(value=item)
                    for (
                        key,
                        item,
                    ) in value.items()
                }

            # Check if the value is a deque
            elif DataIdentificationUtils.is_deque(value=value):
                # Serialize a deque
                return [_serialize(item) for item in value]

            # Check if the value is a set
            elif DataIdentificationUtils.is_set(value=value):
                # Serialize a set
                return [_serialize(item) for item in value]

            # Check if the value is a frozenset
            elif DataIdentificationUtils.is_frozenset(value=value):
                # Serialize a frozenset
                return [_serialize(item) for item in value]

            # Check if the value is a datetime
            elif DataIdentificationUtils.is_datetime(value=value):
                # Serialize a datetime
                return cls.datetime_to_str(value=value)

            # Check if the value is a date
            elif DataIdentificationUtils.is_date(value=value):
                # Serialize a date
                return cls.date_to_str(value=value)

            # Check if the value is a time
            elif DataIdentificationUtils.is_time(value=value):
                # Serialize a time
                return cls.time_to_str(value=value)

            # Check if the value is a timedelta
            elif DataIdentificationUtils.is_timedelta(value=value):
                # Serialize a timedelta
                return cls.timedelta_to_str(value=value)

            # Check if the value is a complex
            elif DataIdentificationUtils.is_complex(value=value):
                # Serialize a complex
                return cls.complex_to_str(value=value)

            # Check if the value is a bytes
            elif DataIdentificationUtils.is_bytes(value=value):
                # Serialize a bytes
                return cls.bytes_to_str(value=value)

            # Check if the value is a path
            elif DataIdentificationUtils.is_path(value=value):
                # Serialize a path
                return cls.path_to_str(value=value)

            # Check if the value is a UUID
            elif DataIdentificationUtils.is_uuid(value=value):
                # Serialize a UUID
                return cls.uuid_to_str(value=value)

            # Serialize a primitive type
            return cls.to_str(value=value)

        # Check if the value is a dictionary
        if DataIdentificationUtils.is_dict(value=value):
            # Serialize a dictionary
            return json.dumps(
                {
                    key: _serialize(value=item)
                    for (
                        key,
                        item,
                    ) in value.items()
                }
            )

        # Check if the value is a list
        elif DataIdentificationUtils.is_list(value=value):
            # Serialize a list
            return json.dumps([_serialize(item) for item in value])

        # Default to string conversion
        return cls.to_str(value=value)

    @classmethod
    def str_to_bool(
        cls,
        value: str,
    ) -> Optional[bool]:
        """
        Convert a string to a boolean.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[bool]: The boolean representation of the string or None if the string cannot be converted to a boolean.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        # Check if the string is in the list of true values
        if value.lower() in {
            "true",
            "1",
            "t",
            "y",
            "yes",
            "false",
            "0",
            "f",
            "n",
            "no",
        }:
            # Return True if the string is in the list of true values
            return value.lower() in {"true", "1", "t", "y", "yes"}

        # Return None if the string cannot be converted to a boolean
        return None

    @classmethod
    def str_to_bytes(
        cls,
        value: str,
    ) -> Optional[bytes]:
        """
        Convert a string to bytes.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[bytes]: The bytes representation of the string or None if the string cannot be converted to bytes.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to bytes
            return value.encode(encoding="utf-8")
        except UnicodeEncodeError:
            # Return None if the string cannot be converted to bytes
            return None

    @classmethod
    def str_to_complex(
        cls,
        value: str,
    ) -> Optional[complex]:
        """
        Convert a string to a complex number.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[complex]: The complex number representation of the string or None if the string cannot be converted to a complex number.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a complex number
            return complex(value)
        except ValueError:
            # Return None if the string cannot be converted to a complex number
            return None

    @classmethod
    def str_to_counter(
        cls,
        value: str,
    ) -> Optional[Counter]:
        """
        Convert a string to a counter.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[Counter]: The counter representation of the string or None if the string cannot be converted to a counter.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a counter
            return Counter(value)
        except ValueError:
            # Return None if the string cannot be converted to a counter
            return None

    @classmethod
    def str_to_date(
        cls,
        value: str,
        format: Optional[str] = None,
    ) -> Optional[date]:
        """
        Convert a string to a date.

        Args:
            value (str): The string to convert.
            format (Optional[str]): The format to use. Defaults to None.

        Returns:
            Optional[date]: The date representation of the string or None if the string cannot be converted to a date.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        # Check if no format is specified
        if format is None:
            try:
                # Attempt to convert the string to a date using ISO format
                return date.fromisoformat(value)
            except ValueError:
                # Return None if the string cannot be converted to a date
                return None

        try:
            # Attempt to convert the string to a date using the specified format
            return date.strptime(value, format)
        except ValueError:
            # Return None if the string cannot be converted to a date
            return None

    @classmethod
    def str_to_datetime(
        cls,
        value: str,
        format: Optional[str] = None,
    ) -> Optional[datetime]:
        """
        Convert a string to a datetime.

        Args:
            value (str): The string to convert.
            format (Optional[str]): The format to use. Defaults to None.

        Returns:
            Optional[datetime]: The datetime representation of the string or None if the string cannot be converted to a datetime.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        # Check if no format is specified
        if format is None:
            try:
                # Attempt to convert the string to a datetime using ISO format
                return datetime.fromisoformat(value)
            except ValueError:
                # Return None if the string cannot be converted to a datetime
                return None

        try:
            # Attempt to convert the string to a datetime using the specified format
            return datetime.strptime(value, format)
        except ValueError:
            # Return None if the string cannot be converted to a datetime
            return None

    @classmethod
    def str_to_decimal(
        cls,
        value: str,
    ) -> Optional[Decimal]:
        """
        Convert a string to a decimal.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[Decimal]: The decimal representation of the string or None if the string cannot be converted to a decimal.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a decimal
            return Decimal(value)
        except (ValueError, InvalidOperation):
            # Return None if the string cannot be converted to a decimal
            return None

    @classmethod
    def str_to_defaultdict(
        cls,
        value: str,
    ) -> Optional[defaultdict]:
        """
        Convert a string to a defaultdict.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[defaultdict]: The defaultdict representation of the string or None if the string cannot be converted to a defaultdict.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a defaultdict
            return defaultdict(cls.str_to_dict(value=value))
        except ValueError:
            # Return None if the string cannot be converted to a defaultdict
            return None

    @classmethod
    def str_to_deque(
        cls,
        value: str,
    ) -> Optional[deque]:
        """
        Convert a string to a deque.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[deque]: The deque representation of the string or None if the string cannot be converted to a deque.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a deque
            return deque(cls.str_to_list(value=value))
        except ValueError:
            # Return None if the string cannot be converted to a deque
            return None

    @classmethod
    def str_to_dict(
        cls,
        value: str,
    ) -> Optional[dict[str, Any]]:
        """
        Convert a string to a dictionary.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[dict[str, Any]]: The dictionary representation of the string or None if the string cannot be converted to a dictionary.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        # Check if the string starts with '{' and ends with '}'
        if not value.startswith("{") or not value.endswith("}"):
            # Return None if the string does not start with '{' or end with '}'
            return None

        try:
            # Attempt to convert the string to a dictionary
            return json.loads(value)
        except (ValueError, TypeError):
            # Return None if the string cannot be converted to a dictionary
            return None

    @classmethod
    def str_to_float(
        cls,
        value: str,
    ) -> Optional[float]:
        """
        Convert a string to a float.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[float]: The float representation of the string or None if the string cannot be converted to a float.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a float
            return float(value)
        except ValueError:
            # Return None if the string cannot be converted to a float
            return None

    @classmethod
    def str_to_fraction(
        cls,
        value: str,
    ) -> Optional[Fraction]:
        """
        Convert a string to a fraction.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[Fraction]: The fraction representation of the string or None if the string cannot be converted to a fraction.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a fraction
            return Fraction(value)
        except ValueError:
            # Return None if the string cannot be converted to a fraction
            return None

    @classmethod
    def str_to_frozendict(
        cls,
        value: str,
    ) -> Optional[frozendict]:
        """
        Convert a string to a frozen dictionary.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[frozendict]: The frozen dictionary representation of the string or None if the string cannot be converted to a frozen dictionary.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a frozen dictionary
            return frozendict(cls.str_to_dict(value=value))
        except (ValueError, TypeError):
            # Return None if the string cannot be converted to a frozen dictionary
            return None

    @classmethod
    def str_to_frozenset(
        cls,
        value: str,
    ) -> Optional[frozenset]:
        """
        Convert a string to a frozenset.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[frozenset]: The frozenset representation of the string or None if the string cannot be converted to a frozenset.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a frozenset
            return frozenset(cls.str_to_list(value=value))
        except (ValueError, TypeError):
            # Return None if the string cannot be converted to a frozenset
            return None

    @classmethod
    def str_to_int(
        cls,
        value: str,
    ) -> Optional[int]:
        """
        Convert a string to an integer.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[int]: The integer representation of the string or None if the string cannot be converted to an integer.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to an integer
            return int(value)
        except ValueError:
            # Return None if the string cannot be converted to an integer
            return None

    @classmethod
    def str_to_list(
        cls,
        value: str,
    ) -> Optional[list]:
        """
        Convert a string to a list.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[list]: The list representation of the string or None if the string cannot be converted to a list.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        # Check if the string starts with '[' and ends with ']'
        if not value.startswith("[") or not value.endswith("]"):
            # Return None if the string does not start with '[' or end with ']'
            return None

        try:
            # Attempt to convert the string to a list
            return json.loads(value)
        except (ValueError, TypeError):
            # Return None if the string cannot be converted to a list
            return None

    @classmethod
    def str_to_path(
        cls,
        value: str,
    ) -> Optional[Path]:
        """
        Convert a string to a path.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[Path]: The path representation of the string or None if the value is not a string.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        # Convert the string to a path
        path: Path = Path(value)

        try:
            # Attempt to resolve the path
            path.resolve()

            # Return the path if resolving it succeeds
            return path
        except FileNotFoundError:
            # Return None if the path does not exist
            return None

    @classmethod
    def str_to_set(
        cls,
        value: str,
    ) -> Optional[Set]:
        """
        Convert a string to a set.

        Args:
            value (str): The string to convert.

        Returns:
             Optional[Set]: The set representation of the string or None if the string cannot be converted to a set.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        # Check if the string starts with '{' and ends with '}'
        if not value.startswith("{") or not value.endswith("}"):
            # Return None if the string cannot be converted to a set
            return None

        # Check if the string could be split by ':' (potentially being a dictionary)
        if ":" in value:
            # Return None if the string cannot be converted to a set
            return None

        # Attempt to split the string by ','
        parts = value[1:-1].split(",")

        # Check if the string could not be split by ','
        if not parts:
            # Return None if the string cannot be converted to a set
            return None

        # Return the set of parts
        return set(parts)

    @classmethod
    def str_to_time(
        cls,
        value: str,
    ) -> Optional[time]:
        """
        Convert a string to a time.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[time]: The time representation of the string or None if the string cannot be converted to a time.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a time using ISO format
            return time.fromisoformat(value)
        except ValueError:
            # Return None if the string cannot be converted to a time
            return None

    @classmethod
    def str_to_timedelta(
        cls,
        value: str,
    ) -> Optional[timedelta]:
        """
        Convert a string to a timedelta.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[timedelta]: The timedelta representation of the string or None if the string cannot be converted to a timedelta.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        # Import the parse_duration function from isodate locally
        from isodate import parse_duration

        try:
            # Attempt to convert the string to a timedelta using isodate
            return parse_duration(datestring=value)
        except ValueError:
            # If conversion fails, pass and try to convert manually
            pass

        try:
            # Attempt to obtain days and time
            (
                days,
                time,
            ) = value.split(",")

            # Attempt to obtain hours, minutes, and seconds
            (
                hours,
                minutes,
                seconds,
            ) = time.split(":")

            # Check if all parts are digits
            if not all(
                [
                    days.isdigit(),
                    hours.isdigit(),
                    minutes.isdigit(),
                    seconds.isdigit(),
                ]
            ):
                # Return None if the string cannot be converted to a timedelta
                return None

            # Attempt to convert the string to a timedelta
            return timedelta(
                days=int(days),
                hours=int(hours),
                minutes=int(minutes),
                seconds=int(seconds),
            )
        except ValueError:
            # Return None if the string cannot be converted to a timedelta
            return None

    @classmethod
    def str_to_timezone(
        cls,
        value: str,
    ) -> Optional[timezone]:
        """
        Convert a string to a timezone.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[timezone]: The timezone representation of the string or None if the string cannot be converted to a timezone.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a timezone
            return timezone(value)
        except (ValueError, TypeError):
            # Return None if the string cannot be converted to a timezone
            return None

    @classmethod
    def str_to_tuple(
        cls,
        value: str,
    ) -> Optional[tuple]:
        """
        Convert a string to a tuple.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[tuple]: The tuple representation of the string or None if the string cannot be converted to a tuple.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        # Check if the string starts with '(' and ends with ')'
        if not value.startswith("(") or not value.endswith(")"):
            # Return None if the string cannot be converted to a tuple
            return None

        # Check if the string could be split by ':' (potentially being a dictionary)
        if ":" in value:
            # Return None if the string cannot be converted to a tuple
            return None

        # Attempt to split the string by ','
        parts = value[1:-1].split(",")

        # Check if the string could not be split by ','
        if not parts:
            # Return None if the string cannot be converted to a tuple
            return None

        # Return the tuple representation of the string
        return tuple(parts)

    @classmethod
    def str_to_uuid(
        cls,
        value: str,
    ) -> Optional[UUID]:
        """
        Convert a string to a UUID.

        Args:
            value (str): The string to convert.

        Returns:
            Optional[UUID]: The UUID representation of the string or None if the value is not a string.
        """

        # Check if the value is a string
        if value is None or not isinstance(
            value,
            str,
        ):
            # Return None if the value is not a string
            return None

        try:
            # Attempt to convert the string to a UUID
            return UUID(value)
        except ValueError:
            # Return None if the string is not a valid UUID
            return None

    @classmethod
    def time_to_str(
        cls,
        value: time,
        format: Optional[str] = None,
    ) -> Optional[str]:
        """
        Convert a time to a string.

        Args:
            value (time): The time to convert.
            format (Optional[str]): The format to use. Defaults to None.

        Returns:
            Optional[str]: The string representation of the time or None if the value is not a time.
        """

        # Check if the passed value is a time object
        if not isinstance(
            value,
            time,
        ):
            # Return None if the value is not a time
            return None

        # Return the string representation of the time
        return value.strftime(format=format) if format else value.isoformat()

    @classmethod
    def timedelta_to_str(
        cls,
        value: timedelta,
    ) -> str:
        """
        Convert a timedelta to a string.

        Args:
            value (timedelta): The timedelta to convert.

        Returns:
            str: The string representation of the timedelta.
        """

        # Return the string representation of the timedelta
        return cls.to_str(value=value)

    @classmethod
    def timezone_to_str(
        cls,
        value: timezone,
    ) -> str:
        """
        Convert a timezone to a string.

        Args:
            value (timezone): The timezone to convert.

        Returns:
            str: The string representation of the timezone.
        """

        return cls.to_str(value=value)

    @classmethod
    def to_bool(
        cls,
        value: Any,
    ) -> bool:
        """
        Convert a value to a boolean.

        Args:
            value (Any): The value to convert.

        Returns:
            bool: The boolean representation of the value.
        """

        # Convert the value to a boolean
        return bool(value)

    @classmethod
    def to_bytes(
        cls,
        value: Any,
    ) -> bytes:
        """
        Convert a value to bytes.

        Args:
            value (Any): The value to convert.

        Returns:
            bytes: The byte representation of the value.
        """

        # Convert the value to bytes
        return bytes(value)

    @classmethod
    def to_date(
        cls,
        value: Any,
    ) -> date:
        """
        Convert a value to a date.

        Args:
            value (Any): The value to convert.

        Returns:
            date: The date representation of the value.
        """

        try:
            # Attempt to convert the value to a date
            return date(value)
        except ValueError as ve:
            # Raise a DataConversionError if the value cannot be converted to a date
            raise DataConversionError(type_=date, value=value) from ve

    @classmethod
    def to_datetime(
        cls,
        value: Any,
    ) -> datetime:
        """
        Convert a value to a datetime.

        Args:
            value (Any): The value to convert.

        Returns:
            datetime: The datetime representation of the value.
        """

        try:
            # Attempt to convert the value to a datetime
            return datetime(value)
        except ValueError as ve:
            # Raise a DataConversionError if the value cannot be converted to a datetime
            raise DataConversionError(type_=datetime, value=value) from ve

    @classmethod
    def to_decimal(
        cls,
        value: Any,
    ) -> Decimal:
        """
        Convert a value to a decimal.

        Args:
            value (Any): The value to convert.

        Returns:
            Decimal: The decimal representation of the value.
        """

        try:
            # Attempt to convert the value to a decimal
            return Decimal(value)
        except ValueError as ve:
            # Raise a DataConversionError if the value cannot be converted to a decimal
            raise DataConversionError(type_=Decimal, value=value) from ve

    @classmethod
    def to_fraction(
        cls,
        value: Any,
    ) -> Fraction:
        """
        Convert a value to a fraction.

        Args:
            value (Any): The value to convert.

        Returns:
            Fraction: The fraction representation of the value.
        """

        try:
            # Attempt to convert the value to a fraction
            return Fraction(value)
        except ValueError as ve:
            # Raise a DataConversionError if the value cannot be converted to a fraction
            raise DataConversionError(type_=Fraction, value=value) from ve

    @classmethod
    def to_path(
        cls,
        value: Any,
    ) -> Path:
        """
        Convert a value to a path.

        Args:
            value (Any): The value to convert.

        Returns:
            Path: The path representation of the value.
        """

        return Path(value)

    @classmethod
    def to_str(
        cls,
        value: Any,
        encoding: Literal["utf-8", "ascii"] = "utf-8",
    ) -> str:
        """
        Convert a value to a string.

        Args:
            value (Any): The value to convert.
            encoding (Literal["utf-8", "ascii"]): The encoding to use. Defaults to "utf-8".

        Returns:
            str: The string representation of the value.
        """

        # Convert the value to a string and encode it using the specified encoding
        return str(value).encode(encoding=encoding).decode(encoding=encoding)

    @classmethod
    def to_time(
        cls,
        value: Any,
    ) -> time:
        """
        Convert a value to a time.

        Args:
            value (Any): The value to convert.

        Returns:
            time: The time representation of the value.
        """

        try:
            # Attempt to convert the value to a time
            return time(value)
        except ValueError as ve:
            # Raise a DataConversionError if the value cannot be converted to a time
            raise DataConversionError(type_=time, value=value) from ve

    @classmethod
    def to_timedelta(
        cls,
        value: Any,
    ) -> timedelta:
        """
        Convert a value to a timedelta.

        Args:
            value (Any): The value to convert.

        Returns:
            timedelta: The timedelta representation of the value.
        """

        try:
            # Attempt to convert the value to a timedelta
            return timedelta(value)
        except ValueError as ve:
            # Raise a DataConversionError if the value cannot be converted to a timedelta
            raise DataConversionError(type_=timedelta, value=value) from ve

    @classmethod
    def to_uuid(
        cls,
        value: Any,
    ) -> UUID:
        """
        Convert a value to a UUID.

        Args:
            value (Any): The value to convert.

        Returns:
            UUID: The UUID representation of the value.
        """

        try:
            # Attempt to convert the value to a UUID
            return UUID(value)
        except ValueError as ve:
            # Raise a DataConversionError if the value cannot be converted to a UUID
            raise DataConversionError(type_=UUID, value=value) from ve

    @classmethod
    def uuid_to_str(
        cls,
        value: UUID,
    ) -> str:
        """
        Convert a UUID to a string.

        Args:
            value (UUID): The UUID to convert.

        Returns:
            str: The string representation of the UUID.
        """

        return cls.to_str(value=value)


class DataIdentificationUtils:
    """
    A collection of utility functions for data processing.
    """

    @classmethod
    def could_be_bool(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a boolean.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a boolean, False otherwise.
        """

        try:
            # Attempt to convert the value to a boolean
            bool(value)

            # Return True if the value could be converted to a boolean
            return True
        except ValueError:
            # Return False if the value could not be converted to a boolean
            return False

    @classmethod
    def could_be_bytes(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to bytes.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to bytes, False otherwise.
        """

        try:
            # Attempt to convert the value to bytes
            bytes(value)

            # Return True if the value could be converted to bytes
            return True
        except ValueError:
            # Return False if the value could not be converted to bytes
            return False

    @classmethod
    def could_be_complex(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a complex number.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a complex number, False otherwise.
        """

        try:
            # Attempt to convert the value to a complex number
            complex(value)

            # Return True if the value could be converted to a complex number
            return True
        except ValueError:
            # Return False if the value could not be converted to a complex number
            return False

    @classmethod
    def could_be_counter(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a counter.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a counter, False otherwise.
        """

        try:
            # Attempt to convert the value to a counter
            Counter(value)

            # Return True if the value could be converted to a counter
            return True
        except ValueError:
            # Return False if the value could not be converted to a counter
            return False

    @classmethod
    def could_be_date(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a date.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a date, False otherwise.
        """

        try:
            # Attempt to convert the value to a date
            date(value)

            # Return True if the value could be converted to a date
            return True
        except ValueError:
            # Return False if the value could not be converted to a date
            return False

    @classmethod
    def could_be_datetime(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a datetime.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a datetime, False otherwise.
        """

        try:
            # Attempt to convert the value to a datetime
            datetime(value)

            # Return True if the value could be converted to a datetime
            return True
        except ValueError:
            # Return False if the value could not be converted to a datetime
            return False

    @classmethod
    def could_be_decimal(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a decimal.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a decimal, False otherwise.
        """

        try:
            # Attempt to convert the value to a decimal
            Decimal(value)

            # Return True if the value could be converted to a decimal
            return True
        except ValueError:
            # Return False if the value could not be converted to a decimal
            return False

    @classmethod
    def could_be_defaultdict(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a defaultdict.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a defaultdict, False otherwise.
        """

        try:
            # Attempt to convert the value to a defaultdict
            defaultdict(value)

            # Return True if the value could be converted to a defaultdict
            return True
        except ValueError:
            # Return False if the value could not be converted to a defaultdict
            return False

    @classmethod
    def could_be_deque(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a deque.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a deque, False otherwise.
        """

        try:
            # Attempt to convert the value to a deque
            deque(value)

            # Return True if the value could be converted to a deque
            return True
        except ValueError:
            # Return False if the value could not be converted to a deque
            return False

    @classmethod
    def could_be_dict(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a dictionary.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a dictionary, False otherwise.
        """

        try:
            # Attempt to convert the value to a dictionary
            dict(value)

            # Return True if the value could be converted to a dictionary
            return True
        except ValueError:
            # Return False if the value could not be converted to a dictionary
            return False

    @classmethod
    def could_be_float(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a float.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a float, False otherwise.
        """

        try:
            # Attempt to convert the value to a float
            float(value)

            # Return True if the value could be converted to a float
            return True
        except ValueError:
            # Return False if the value could not be converted to a float
            return False

    @classmethod
    def could_be_fraction(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a fraction.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a fraction, False otherwise.
        """

        try:
            # Attempt to convert the value to a fraction
            Fraction(value)

            # Return True if the value could be converted to a fraction
            return True
        except ValueError:
            # Return False if the value could not be converted to a fraction
            return False

    @classmethod
    def could_be_frozendict(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a frozendict.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a frozendict, False otherwise.
        """

        try:
            # Attempt to convert the value to a frozendict
            frozendict(value)

            # Return True if the value could be converted to a frozendict
            return True
        except ValueError:
            # Return False if the value could not be converted to a frozendict
            return False

    @classmethod
    def could_be_frozenset(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a frozenset.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a frozenset, False otherwise.
        """

        try:
            # Attempt to convert the value to a frozenset
            frozenset(value)

            # Return True if the value could be converted to a frozenset
            return True
        except ValueError:
            # Return False if the value could not be converted to a frozenset
            return False

    @classmethod
    def could_be_int(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to an integer.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to an integer, False otherwise.
        """

        try:
            # Attempt to convert the value to an integer
            int(value)

            # Return True if the value could be converted to an integer
            return True
        except ValueError:
            # Return False if the value could not be converted to an integer
            return False

    @classmethod
    def could_be_list(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a list.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a list, False otherwise.
        """

        try:
            # Attempt to convert the value to a list
            list(value)

            # Return True if the value could be converted to a list
            return True
        except ValueError:
            # Return False if the value could not be converted to a list
            return False

    @classmethod
    def could_be_path(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a path.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a path, False otherwise.
        """

        try:
            # Attempt to convert the value to a path
            Path(value)

            # Return True if the value could be converted to a path
            return True
        except ValueError:
            # Return False if the value could not be converted to a path
            return False

    @classmethod
    def could_be_set(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a set.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a set, False otherwise.
        """

        try:
            # Attempt to convert the value to a set
            set(value)

            # Return True if the value could be converted to a set
            return True
        except ValueError:
            # Return False if the value could not be converted to a set
            return False

    @classmethod
    def could_be_time(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a time.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a time, False otherwise.
        """

        try:
            # Attempt to convert the value to a time
            time(value)

            # Return True if the value could be converted to a time
            return True
        except ValueError:
            # Return False if the value could not be converted to a time
            return False

    @classmethod
    def could_be_timedelta(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a timedelta.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a timedelta, False otherwise.
        """

        try:
            # Attempt to convert the value to a timedelta
            timedelta(value)

            # Return True if the value could be converted to a timedelta
            return True
        except ValueError:
            # Return False if the value could not be converted to a timedelta
            return False

    @classmethod
    def could_be_timezone(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a timezone.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a timezone, False otherwise.
        """

        try:
            # Attempt to convert the value to a timezone
            timezone(value)

            # Return True if the value could be converted to a timezone
            return True
        except ValueError:
            # Return False if the value could not be converted to a timezone
            return False

    @classmethod
    def could_be_tuple(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a tuple.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a tuple, False otherwise.
        """

        try:
            # Attempt to convert the value to a tuple
            tuple(value)

            # Return True if the value could be converted to a tuple
            return True
        except ValueError:
            # Return False if the value could not be converted to a tuple
            return False

    @classmethod
    def could_be_uuid(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value could be converted to a UUID.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value could be converted to a UUID, False otherwise.
        """

        try:
            # Attempt to convert the value to a UUID
            UUID(value)

            # Return True if the value could be converted to a UUID
            return True
        except ValueError:
            # Return False if the value could not be converted to a UUID
            return False

    @classmethod
    def identify(
        cls,
        value: Any,
    ) -> str:
        """
        Identify the type of the value.

        Args:
            value (Any): The value to identify.

        Returns:
            str: The type of the value.
        """

        # Return the type of the value
        return type(value).__name__

    @classmethod
    def identify_in_str(
        cls,
        value: str,
    ) -> Optional[type]:
        """
        Identify the type of information contained within a string.

        Args:
            value (str): The string to identify.

        Returns:
            Optional[type]: The type of the string or None if the type cannot be identified.
        """

        # Check if the string can successfully be converted to a boolean
        if DataConversionUtils.str_to_bool(value=value):
            # Return bool if the string can be converted to a boolean
            return bool

        # Check if the string can successfully be converted to a complex
        elif DataConversionUtils.str_to_complex(value=value):
            # Return complex if the string can be converted to a complex
            return complex

        # Check if the string can successfully be converted to a dictionary
        elif DataConversionUtils.str_to_dict(value=value):
            # Return dict if the string can be converted to a dictionary
            return dict

        # Check if the string can successfully be converted to a float
        elif DataConversionUtils.str_to_float(value=value):
            # Return float if the string can be converted to a float
            return float

        # Check if the string can successfully be converted to an integer
        elif DataConversionUtils.str_to_int(value=value):
            # Return int if the string can be converted to an integer
            return int

        # Check if the string can successfully be converted to a list
        elif DataConversionUtils.str_to_list(value=value):
            # Return list if the string can be converted to a list
            return list

        # Check if the string can successfully be converted to a set
        elif DataConversionUtils.str_to_set(value=value):
            # Return set if the string can be converted to a set
            return set

        # Check if the string can successfully be converted to a tuple
        elif DataConversionUtils.str_to_tuple(value=value):
            # Return tuple if the string can be converted to a tuple
            return tuple

        # Check if the string can successfully be converted to a date
        elif DataConversionUtils.str_to_date(value=value):
            # Return date if the string can be converted to a date
            return date

        # Check if the string can successfully be converted to a datetime
        elif DataConversionUtils.str_to_datetime(value=value):
            # Return datetime if the string can be converted to a datetime
            return datetime

        # Check if the string can successfully be converted to a time
        elif DataConversionUtils.str_to_time(value=value):
            # Return time if the string can be converted to a time
            return time

        # Check if the string can successfully be converted to a timedelta
        elif DataConversionUtils.str_to_timedelta(value=value):
            # Return timedelta if the string can be converted to a timedelta
            return timedelta

        # Check if the string can successfully be converted to a timezone
        elif DataConversionUtils.str_to_timezone(value=value):
            # Return timezone if the string can be converted to a timezone
            return timezone

        # Check if the string can successfully be converted to a uuid
        elif DataConversionUtils.str_to_uuid(value=value):
            # Return uuid if the string can be converted to a uuid
            return UUID

        # Check if the string can successfully be converted to a path
        elif DataConversionUtils.str_to_path(value=value):
            # Return path if the string can be converted to a path
            return Path

        # Check if the string can successfully be converted to bytes
        elif DataConversionUtils.str_to_bytes(value=value):
            # Return bytes if the string can be converted to bytes
            return bytes

        # Return None if the string cannot be converted at all
        return None

    @classmethod
    def identify_numeric_type(
        cls,
        value: Any,
    ) -> Optional[type]:
        """
        Identifies the numeric type of the value.

        Args:
            value (Any): The value to identify.

        Returns:
            Optional[type]: The numeric type of the value, or None if the value is not numeric.
        """

        # Check if the value could be an int
        if cls.could_be_int(value=value):
            # Return int if the value could be an int
            return int
        # Check if the value could be a float
        elif cls.could_be_float(value=value):
            # Return float if the value could be a float
            return float
        # Check if the value could be a complex
        elif cls.could_be_complex(value=value):
            # Return complex if the value could be a complex
            return complex
        # Check if the value could be a decimal
        elif cls.could_be_decimal(value=value):
            # Return Decimal if the value could be a decimal
            return Decimal

        # Return None if the value is not numeric
        return None

    @classmethod
    def is_bool(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a boolean.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a boolean, False otherwise.
        """

        # Check if the value is an instance of bool
        return cls.is_instance(
            type_=bool,
            value=value,
        )

    @classmethod
    def is_bytes(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is an instance of bytes.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is an instance of bytes, False otherwise.
        """

        # Check if the value is an instance of bytes
        return cls.is_instance(
            type_=bytes,
            value=value,
        )

    @classmethod
    def is_complex(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is an instance of complex.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is an instance of complex, False otherwise.
        """

        # Check if the value is an instance of complex
        return cls.is_instance(
            type_=complex,
            value=value,
        )

    @classmethod
    def is_counter(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a counter.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a counter, False otherwise.
        """

        # Check if the value is an instance of Counter
        return cls.is_instance(
            type_=Counter,
            value=value,
        )

    @classmethod
    def is_date(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a date.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a date, False otherwise.
        """

        # Check if the value is an instance of date
        return cls.is_instance(
            type_=date,
            value=value,
        )

    @classmethod
    def is_datetime(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a datetime.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a datetime, False otherwise.
        """

        # Check if the value is an instance of datetime
        return cls.is_instance(
            type_=datetime,
            value=value,
        )

    @classmethod
    def is_decimal(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a decimal.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a decimal, False otherwise.
        """

        # Check if the value is an instance of Decimal
        return cls.is_instance(
            type_=Decimal,
            value=value,
        )

    @classmethod
    def is_defaultdict(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a defaultdict.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a defaultdict, False otherwise.
        """

        # Check if the value is an instance of defaultdict
        return cls.is_instance(
            type_=defaultdict,
            value=value,
        )

    @classmethod
    def is_deque(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a deque.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a deque, False otherwise.
        """

        # Check if the value is an instance of deque
        return cls.is_instance(
            type_=deque,
            value=value,
        )

    @classmethod
    def is_dict(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a dictionary.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a dictionary, False otherwise.
        """

        # Check if the value is an instance of dict
        return cls.is_instance(
            type_=dict,
            value=value,
        )

    @classmethod
    def is_float(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a float.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a float, False otherwise.
        """

        # Check if the value is an instance of float
        return cls.is_instance(
            type_=float,
            value=value,
        )

    @classmethod
    def is_fraction(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a fraction.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a fraction, False otherwise.
        """

        # Check if the value is an instance of Fraction
        return cls.is_instance(
            type_=Fraction,
            value=value,
        )

    @classmethod
    def is_frozendict(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a frozendict.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a frozendict, False otherwise.
        """

        # Check if the value is an instance of frozendict
        return cls.is_instance(
            type_=frozendict,
            value=value,
        )

    @classmethod
    def is_frozenset(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a frozenset.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a frozenset, False otherwise.
        """

        # Check if the value is an instance of frozenset
        return cls.is_instance(
            type_=frozenset,
            value=value,
        )

    @classmethod
    def is_instance(
        cls,
        value: Any,
        type_: Union[type, tuple[type, ...]],
    ) -> bool:
        """
        Checks if the value is an instance of the given type.

        Args:
            value (Any): The value to check.
            type_ (Union[type, tuple[type, ...]]): The type to check against.

        Returns:
            bool: True if the value is an instance of the given type, False otherwise.
        """

        return isinstance(value, type_)

    @classmethod
    def is_int(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is an integer.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is an integer, False otherwise.
        """

        # Check if the value is an instance of int
        return cls.is_instance(
            type_=int,
            value=value,
        )

    @classmethod
    def is_list(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a list.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a list, False otherwise.
        """

        # Check if the value is an instance of list
        return cls.is_instance(
            type_=list,
            value=value,
        )

    @classmethod
    def is_none(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is None.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is None, False otherwise.
        """

        # Check if the value is None
        return value is None

    @classmethod
    def is_path(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a path.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a path, False otherwise.
        """

        # Check if the value is an instance of Path
        return cls.is_instance(
            type_=Path,
            value=value,
        )

    @classmethod
    def is_primitive_type(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a primitive type.

        This method checks if the given value is an instance of a primitive type.
        Primitive types include int, float and bool.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a primitive type, False otherwise.
        """

        # Check if the value is an instance of a primitive type
        return cls.is_instance(
            type_=(
                int,
                float,
                bool,
            ),
            value=value,
        )

    @classmethod
    def is_set(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a set.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a set, False otherwise.
        """

        # Check if the value is an instance of set
        return cls.is_instance(
            type_=set,
            value=value,
        )

    @classmethod
    def is_str(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a string.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a string, False otherwise.
        """

        # Check if the value is an instance of str
        return cls.is_instance(
            type_=str,
            value=value,
        )

    @classmethod
    def is_time(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a time.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a time, False otherwise.
        """

        # Check if the value is an instance of time
        return cls.is_instance(
            type_=time,
            value=value,
        )

    @classmethod
    def is_timedelta(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a timedelta.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a timedelta, False otherwise.
        """

        # Check if the value is an instance of timedelta
        return cls.is_instance(
            type_=timedelta,
            value=value,
        )

    @classmethod
    def is_timezone(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a timezone.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a timezone, False otherwise.
        """

        # Check if the value is an instance of timezone
        return cls.is_instance(
            type_=timezone,
            value=value,
        )

    @classmethod
    def is_tuple(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a tuple.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a tuple, False otherwise.
        """

        # Check if the value is an instance of tuple
        return cls.is_instance(
            type_=tuple,
            value=value,
        )

    @classmethod
    def is_uuid(
        cls,
        value: Any,
    ) -> bool:
        """
        Checks if the value is a UUID.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a UUID, False otherwise.
        """

        # Check if the value is an instance of UUID
        return cls.is_instance(
            type_=UUID,
            value=value,
        )
