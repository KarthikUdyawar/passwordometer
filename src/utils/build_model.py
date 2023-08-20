"""Build Model"""
import argparse
import json

from src.interface.config import config
from src.pipe.pipeline import Pipeline

# Generate kaggle.json
kaggle_credentials = {
    "username": config["KAGGLE_USERNAME"],
    "key": config["KAGGLE_KEY"],
}


# Save the credentials as kaggle.json
def generate_json(values: dict[str, str]) -> None:
    """Generate a JSON file with the provided values.

    Args:
        values (dict[str, str]): The dictionary containing key-value pairs
        to be written to the JSON file.
    """
    with open("kaggle.json", "w", encoding="utf-8") as file:
        json.dump(values, file)


def process_and_train() -> None:
    """This function utilizes the Pipeline class to perform data pushing and training."""
    pipeline = Pipeline()
    pipeline.push_data()
    pipeline.train()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and train the model")
    parser.add_argument(
        "--train",
        action="store_true",
        help="Whether to process and train the model",
    )
    args = parser.parse_args()

    generate_json(kaggle_credentials)

    if args.train:
        process_and_train()
