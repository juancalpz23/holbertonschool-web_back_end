#!/usr/bin/env python3
"""
Defines filter_datum function to obfuscate fields in a log message.
"""

import logging
from typing import List
from re import sub


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Hide specific fields in a log message by replacing them with redactions.
    """

    return sub(f"({'|'.join(fields)})=.*?{separator}",
               f"\\1={redaction}{separator}", message)


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
