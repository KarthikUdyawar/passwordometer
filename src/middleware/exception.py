import sys
from typing import Any

from src.middleware.logger import logger


class CustomException(Exception):
    def __init__(self, error_message: Any, error_detail: Any):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self) -> str:
        return self.error_message


def error_message_detail(error: Any, error_detail: Any) -> str:
    _, _, exc_tb = error_detail.exc_info()
    if exc_tb is None:
        raise CustomException(error, sys) from error
    file_name = exc_tb.tb_frame.f_code.co_filename
    logger.error(
        f"""Error occurred in python script name [{file_name}]
        line number [{exc_tb.tb_lineno}] error message [{str(error)}]"""
    )
    return str(error)


if __name__ == "__main__":
    try:
        _ = 1 / 0
    except Exception as e:
        logger.debug("Test CustomException")
        raise CustomException(e, sys) from e
    