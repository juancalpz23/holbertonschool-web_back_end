#!/usr/bin/env python3
"""
Defines filter_datum function to obfuscate fields in a log message.
"""

import logging
from typing import List, Tuple
from re import sub

# Update PII_FIELDS with the relevant sensitive fields from user_data.csv
PII_FIELDS: Tuple[str, ...] = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """
    Creates a logger named 'user_data' with logging level
    INFO that hides PII fields.

    Returns:
        logging.Logger: Configured logger object.
    """
    # Create logger
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create StreamHandler and set formatter
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(stream_handler)

    return logger


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to be redacted
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record and filter sensitive information.
        """
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Hide specific fields in a log message by replacing them with redactions.
    Adds a space after the separator for readability.
    """
    return sub(f"({'|'.join(fields)})=.*?{separator}",
               f"\\1={redaction}{separator}", message)
