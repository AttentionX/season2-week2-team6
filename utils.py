from enum import Enum

from openai.error import (
    APIConnectionError,
    APIError,
    ServiceUnavailableError,
    Timeout,
    RateLimitError,
)
from retrying import retry

OPENAI_RETRYABLE_ERRORS = (
    APIError,
    Timeout,
    RateLimitError,
    APIConnectionError,
    ServiceUnavailableError,
)


# Color enum
class Colors(Enum):
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    GREY = "\033[90m"
    RESET = "\033[0m"

def print_color(text, color, *args, **kwargs):
    print(f"{color.value}{text}{Colors.RESET.value}", *args, **kwargs)

