# Passwordometer

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/downloads/release/python-31012/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-6.5-orange)](https://jupyter.org/install)
[![MongoDB](https://img.shields.io/badge/MongoDB-5.0-green)](https://www.mongodb.com/)

[![Logo][product-screenshot]](https://example.com)

[product-screenshot]: imgs/logo_1_dark.png

To predict the strength of the password

[**Explore the docs »**](https://github.com/KarthikUdyawar/Passwordometer)

[View Demo](https://github.com/KarthikUdyawar/Passwordometer)
·
[Report Bug](https://github.com/KarthikUdyawar/Passwordometer/issues)
·
[Request Feature](https://github.com/KarthikUdyawar/Passwordometer/pulls)

---

## Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About The Project

[![Product Name Screen Shot][product-screenshot-1]](https://example.com)

[product-screenshot-1]: imgs/logo_1.png

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

---

### Built With

This project was built using the following technologies and libraries:

- [Python](https://www.python.org/): A popular programming language used for data analysis, machine learning, and general-purpose development.
- [Jupyter Notebook](https://jupyter.org/): An interactive development environment that allows you to create and share documents containing live code, equations, visualizations, and narrative text.
- [MongoDB](https://www.mongodb.com/): A flexible and scalable NoSQL database.

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

These libraries played a crucial role in various stages of the project, including data processing, feature engineering, model training, evaluation, and visualization.

---

## Getting Started

This section provides instructions on how to set up the project locally. Follow the steps below to get a local copy up and running.

### Prerequisites

Before proceeding with the installation, ensure that you have the following prerequisites installed:

- Python (version 3.10.6)
- Jupyter Notebook (version 6.5.2)
- MongoDB (version 5.0.5)

You can check the versions of Python and Jupyter Notebook by running the following commands in the terminal:

```bash
python --version
jupyter notebook --version
mongod --version
```

### Installation

Follow the steps below to install and set up the project:

1. **Create a Kaggle API key:**

   By visiting [Kaggle API](https://www.kaggle.com/settings/account) and clicking on the "Create New API Token" button. This will download a file named `kaggle.json` containing your API credentials.

2. **Clone the repository:**

   ```bash
   git clone https://github.com/KarthikUdyawar/Passwordometer.git
   ```

3. **Install the required dependencies**

   By navigating to the project directory and running the following command:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file**

   Create a file named .env in the project directory and enter your Kaggle API key information in the following format:

   ```bash
   KAGGLE_USERNAME=your_username
   KAGGLE_KEY=your_api_key
   ```

5. **Generate the Kaggle keys**

   Generate the Kaggle keys file by running the following command:

   ```bash
   python src/utils/generate_kaggle_keys.py
   ```

---

## Usage

You can use the following code snippet as an example to understand how to use the project:

```python
from src.pipe.pipeline import Pipeline
from src.interface.config import CustomData
from src.middleware.exception import CustomException

pipeline = Pipeline()
custom_data = CustomData()

print("Main menu\n1. Push data\n2. Train pipeline\n3. Predict pipeline\n")
choice = int(input("Enter the choice: "))

if choice == 1:
    pipeline.push_data()
elif choice == 2:
    pipeline.train()
elif choice == 3:
    input_data = str(input("Enter the password: "))
    password = custom_data.data2df(input_data)
    strength = pipeline.predict(password)
    value = custom_data.array2data(strength)
    print(f"\nPassword: {input_data} Strength: {value}")
else:
    raise CustomException("Invalid input", sys)
```

This code snippet demonstrates the basic usage of the project. It creates an instance of the `Pipeline` class and interacts with the user through a menu-based system. The user can choose to push data, train the pipeline, or predict the strength of a password.

Make sure to customize the code according to your specific requirements, such as modifying the input prompts or handling exceptions.

_For more examples, please refer to the [Documentation](https://github.com/KarthikUdyawar/Passwordometer/blob/release-0.17/notebooks/README.md)_

---

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

---

## Contact

Project Link: [![GitHub](https://img.shields.io/badge/GitHub-Repo-blueviolet?logo=github)](https://github.com/KarthikUdyawar/Passwordometer)
