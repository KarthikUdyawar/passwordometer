# Passwordometer

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/downloads/release/python-31012/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-6.5-orange)](https://jupyter.org/install)
[![MongoDB](https://img.shields.io/badge/MongoDB-5.0-green)](https://www.mongodb.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.1-red)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-20.10.8-blue)](https://www.docker.com/)

[![Logo][product-screenshot]](https://github.com/KarthikUdyawar/Passwordometer)

[product-screenshot]: imgs/logo_1_dark.png

To predict the strength of the password

[**Explore the docs »**](https://github.com/KarthikUdyawar/Passwordometer)

[View Demo](https://github.com/KarthikUdyawar/Passwordometer)
·
[Report Bug](https://github.com/KarthikUdyawar/Passwordometer/issues)
·
[Request Feature](https://github.com/KarthikUdyawar/Passwordometer/pulls)

</div>

## Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [API Usage](#api-usage)
- [Docker Image](#docker-image)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## About The Project

[![Product Name Screen Shot][product-screenshot-1]](https://github.com/KarthikUdyawar/Passwordometer)

[product-screenshot-1]: imgs/meter.png

The Password Strength Prediction Project is aimed at developing a machine learning model that can predict the strength of passwords based on various features. With the increasing importance of password security, this project aims to provide a tool that can assess the strength of passwords and help users make informed decisions about their password choices.

The project involves the following key steps:

1. **Data Collection:** The project starts with the collection of a large dataset of passwords, including their corresponding strength labels. This dataset serves as the foundation for training and evaluating the machine learning models.

2. **Data Exploration:** The collected dataset is explored to gain insights and understand the patterns and characteristics of passwords. Data visualization techniques and statistical analysis are employed to analyze the dataset and identify key features.

3. **Feature Engineering:** Relevant features are extracted from the passwords to provide meaningful input to the machine learning models. Techniques such as password length, character counts, consecutive characters, and others are utilized to transform the raw passwords into feature vectors.

4. **Model Selection:** Various machine learning models are evaluated and compared to identify the most suitable model for password strength prediction. Different algorithms, including decision trees, random forests, gradient boosting, and others, are trained and evaluated on the dataset.

5. **Pipeline Development:** A machine learning pipeline is constructed, including data preprocessing and the selected model. The pipeline streamlines the data transformation and prediction process, providing a robust and scalable solution for password strength prediction.

6. **Model Evaluation and Prediction:** The trained model is evaluated using various performance metrics such as mean absolute error, mean squared error, root mean squared error, and R-squared. The final model is then used to predict the strength of passwords on new and unseen data.

The project notebooks provide a step-by-step walkthrough of each phase, along with detailed code implementations and explanations. By following the notebooks, users can replicate the project, customize it for their specific needs, and gain a deeper understanding of password strength prediction.

Please refer to the individual notebooks for more details and code implementation.

### Built With

This project was built using the following technologies and libraries:

- [Python](https://www.python.org/): A popular programming language used for data analysis, machine learning, and general-purpose development.
- [Jupyter Notebook](https://jupyter.org/): An interactive development environment that allows you to create and share documents containing live code, equations, visualizations, and narrative text.
- [MongoDB](https://www.mongodb.com/): A flexible and scalable NoSQL database.
- [Docker](https://www.docker.com/): A platform for developing, shipping, and running applications inside containers.

The project primarily utilizes Python programming language and Jupyter Notebook as the development environment. Python provides a robust ecosystem of libraries and tools for data analysis, machine learning, and model development. Jupyter Notebook offers an interactive environment for code development, data exploration, and documentation, making it well-suited for this project.

The following major libraries were used in the project:

- [Pandas](https://pandas.pydata.org/): A powerful data manipulation and analysis library.
- [NumPy](https://numpy.org/): A fundamental package for scientific computing with Python, providing support for arrays and mathematical operations.
- [Scikit-learn](https://scikit-learn.org/): A machine learning library that provides various algorithms and evaluation metrics.
- [Plotly](https://plotly.com/): An interactive data visualization library.
- [PyMongo](https://pymongo.readthedocs.io/): A Python driver for MongoDB that allows interaction with the database from Python.
- [LightGBM](https://lightgbm.readthedocs.io/): A gradient boosting framework for machine learning.
- [XGBoost](https://xgboost.readthedocs.io/): A gradient boosting framework for machine learning.
- [CatBoost](https://catboost.ai/): A gradient boosting framework for machine learning.
- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+.

These libraries played a crucial role in various stages of the project, including data processing, feature engineering, model training, evaluation, and visualization.

## Getting Started

This section provides instructions on how to set up the project locally. Follow the steps below to get a local copy up and running.

### Prerequisites

Before proceeding with the installation, ensure that you have the following prerequisites installed:

- Python (version 3.10.6)
- Jupyter Notebook (version 6.5.2)
- MongoDB (version 5.0.5)
- Docker (version 20.10.8)

You can check the versions of Python and Jupyter Notebook by running the following commands in the terminal:

```bash
python --version

jupyter notebook --version

mongod --version

docker --version
```

### Installation

Follow the steps below to install and set up the project:

1. **Create a Kaggle API key:**

   By visiting [Kaggle API](https://www.kaggle.com/settings/account) and clicking on the "Create New API Token" button. This will download a file named `kaggle.json` containing your API credentials.

2. **Clone the repository:**

   Clone the project repository using the following command:

   ```bash
   git clone https://github.com/KarthikUdyawar/Passwordometer.git
   ```

3. **Create a virtual environment and activate it:**

   To isolate project dependencies, create a virtual environment and activate it:

   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

4. **Install the required dependencies**

   Navigate to the project directory and install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. **Install Passwordometer package**

   Install the Passwordometer package using the following command:

   ```bash
   pip install .
   ```

6. **Create .env file**

   Create a .env file in the project directory and provide your Kaggle API key information and MongoDB URL:

   ```bash
   KAGGLE_USERNAME="your_username"
   KAGGLE_KEY="your_api_key"
   MONGODB_CONN_STRING = "mongodb://localhost:27017/"
   ```

7. **Build and train the model**

   Build and train the model by running the following command:

   ```bash
   python src/utils/build_model.py --train
   ```

## Usage

You can use the following code snippet as an example to understand how to use the project:

```python
"""Interactive program to calculate password strength using a pipeline."""

from src.pipe.pipeline import Pipeline
from src.interface.config import CustomData


def main():
    """Main function for the interactive program."""
    pipeline = Pipeline()
    custom_data = CustomData()

    while True:
        data = str(input("Enter the password (or 'exit' to quit): "))

        if data.lower() == "exit":
            print("Exiting the program.")
            break

        password = custom_data.data2df(data)
        strength = pipeline.predict(password)
        value = custom_data.array2data(strength)
        print(f"\nPassword: {data} Strength: {value}")


if __name__ == "__main__":
    main()
```

This code snippet demonstrates the basic usage of the project. It creates an instance of the `Pipeline` class and interacts with the user through a menu-based system. The user can choose to push data, train the pipeline, or predict the strength of a password.

Make sure to customize the code according to your specific requirements, such as modifying the input prompts or handling exceptions.

_For more examples, please refer to the [Code](https://github.com/KarthikUdyawar/passwordometer/blob/release-1.2/example/basic.py)_

### API Usage

The project now includes an API powered by [FastAPI](https://fastapi.tiangolo.com/), which allows you to interact with password-related functionalities programmatically. To use the API, follow these steps:

1. **Run the FastAPI server:**

   Navigate to the project directory and run the following command:

   ```bash
   uvicorn src.api.app:app --host 0.0.0.0 --port 8000
   ```

   This will start the FastAPI server, making the API endpoints accessible at [http://localhost:8000](http://localhost:8000).

2. **Access the API documentation:**

   Open your web browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to access the Swagger documentation for the API. Here, you can explore the available endpoints, view request and response schemas, and interact with the API using the built-in interface.

3. **API Endpoints:**

   - `POST /predict:` Predict the strength of a password by sending a JSON payload containing the password. The response will include the predicted strength.

   - `POST /generate:` Generate a random password based on specified parameters such as length.

   These endpoints provide programmatic access to the password strength prediction and password generation functionalities.

   _For more details, please refer to the [API documentation](http://localhost:8000/docs)._

## Docker Image

A Docker image for the Passwordometer API is available on [Docker Hub](https://hub.docker.com/repository/docker/kstar123/passwordometer-api/general). You can pull and run the image using the following command:

```bash
docker pull kstar123/passwordometer-api

docker run -d -p 8000:8000 --name passwordometer-api kstar123/passwordometer-api
```

This will start the FastAPI server inside a Docker container, and you can access the API endpoints at [http://localhost:8000](http://localhost:8000).

_For more details on using Docker, refer to the [Docker documentation](https://docs.docker.com/)._

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request against the `develop` branch. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. **Open an Issue:** Start by opening an issue to discuss your proposed changes or enhancements.
2. **Fork the Project:** Create your own fork of the project repository.
3. **Create a Feature Branch:** Create a feature branch in your fork (`git checkout -b feature/AmazingFeature`).
4. **Commit your Changes:** Make your desired changes and commit them (`git commit -m 'Add some AmazingFeature'`).
5. **Push to the Branch:** Push your changes to the feature branch (`git push origin feature/AmazingFeature`).
6. **Open a Pull Request:** Create a pull request against the `develop` branch of the original repository.

## License

Distributed under the MIT License. See [`LICENSE.txt`](https://github.com/KarthikUdyawar/passwordometer/blob/main/LICENSE) for more information.

## Acknowledgments

We would like to express our gratitude to the following open-source projects, libraries, and resources that contributed to the development of Passwordometer:

- [FastAPI](https://fastapi.tiangolo.com/): A fantastic web framework that made building our API a breeze.
- [Pandas](https://pandas.pydata.org/): An essential library for data manipulation and analysis in Python.
- [Scikit-learn](https://scikit-learn.org/): A versatile library for machine learning and data mining tasks.
- [Docker](https://www.docker.com/): Enabling seamless deployment and containerization of our project.
- [GitHub](https://github.com/): For providing a platform for collaboration and version control.
- [Plotly](https://plotly.com/): For helping us create interactive data visualizations.
- [NumPy](https://numpy.org/): An indispensable package for scientific computing in Python.
- [Jupyter Notebook](https://jupyter.org/): For providing an interactive environment for our data analysis and exploration.
- [MongoDB](https://www.mongodb.com/): Powering our NoSQL database needs.
- [Stack Overflow](https://stackoverflow.com/): A treasure trove of knowledge where we found solutions to many challenges.
- [Google Fonts](https://fonts.google.com/): For providing beautiful fonts that enhance our project's design.
- [Unsplash](https://unsplash.com/): A source of high-quality images that we used for our visuals.
- [OpenAI](https://openai.com/): For developing GPT-3, which provided assistance in generating text and ideas.

We are also grateful for the valuable tutorials, guides, and Stack Overflow threads that helped us overcome challenges and learn new concepts along the way.

Lastly, a big thank you to the open-source community for their continuous contributions to the software development ecosystem.

## Contact

If you have any questions, suggestions, or feedback about Passwordometer, feel free to reach out to us:

- **Project Author:** [Karthik Udyawar](mailto:karthikajitudy@gmail.com)
- **GitHub Repo:** [Passwordometer](https://github.com/KarthikUdyawar/Passwordometer)
- **Kaggle:** [Karthik Udyawar](https://www.kaggle.com/karthikudyawar)
- **Docker Hub** [kstar123](https://hub.docker.com/r/kstar123/passwordometer-api)

We are open to collaboration and appreciate any contributions to the project. If you encounter any issues or have ideas for enhancements, please don't hesitate to create an issue or pull request on the GitHub repository.

We value your input and look forward to hearing from you!
