import sys
from logger import CustomLogger


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    logger = CustomLogger("exception")
    return logger.error(
        f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    )


if __name__ == "__main__":
    logger = CustomLogger("exception")
    try:
        a = 1 / 0
    except Exception as e:
        logger.debug("Test CustomException")
        raise CustomException(e, sys) from e
