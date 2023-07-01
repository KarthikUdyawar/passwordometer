import pytest

from src.middleware.logger import logger


def test_logging() -> None:
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")


if __name__ == "__main__":
    pytest.main()
