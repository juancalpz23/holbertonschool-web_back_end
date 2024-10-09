#!/usr/bin/env python3
"""
Defines filter_datum function to obfuscate fields in a log message.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Hide specific fields in a log message by replacing them with redactions
    """

    return re.sub(f"({'|'.join(fields)})=.*?{separator}",
                  f"\\1={redaction}{separator}", message)
