import re

_address_pattern = re.compile(
    "^([a-zA-Z_][0-9a-zA-Z_]*)(\.[a-zA-Z_][0-9a-zA-Z_]*)*$"
)