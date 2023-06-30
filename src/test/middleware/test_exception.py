import pytest
import sys
from src.middleware.logger import logger
from src.middleware.exception import CustomException, error_message_detail


def test_custom_exception():
    with pytest.raises(CustomException):
        try:
            a = 1 / 0
        except Exception as e:
            logger.debug("Test CustomException")
            raise CustomException(e, sys) from e


def test_error_message_detail():
    error = ZeroDivisionError("division by zero")
    exc_info = type(error), error, None
    try:
        raise error
    except Exception as e:
        message = error_message_detail(e, sys)
        assert isinstance(message, str)


if __name__ == "__main__":
    pytest.main()
