import sys

import pytest

from src.middleware.exception import CustomException
from src.middleware.exception import error_message_detail
from src.middleware.logger import logger


def test_custom_exception() -> None:
    with pytest.raises(CustomException):
        try:
            _ = 1 / 0
        except Exception as e:
            logger.debug("Test CustomException")
            raise CustomException(e, sys) from e


def test_error_message_detail() -> None:
    error = ZeroDivisionError("division by zero")
    try:
        raise error
    except Exception as e:
        message = error_message_detail(e, sys)
        assert isinstance(message, str)


if __name__ == "__main__":
    pytest.main()
