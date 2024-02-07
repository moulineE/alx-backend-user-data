#!/usr/bin/env python3
"""a function that returns the log message obfuscated"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    returns the log message obfuscated
    :param fields:
    :param redaction:
    :param message:
    :param separator:
    :return:
    """
    for field in fields:
        pattern = '({}=)(.*?)({})'.format(field, separator)
        message = re.sub(pattern, r'\1{}\3'.format(redaction), message)
    return message
