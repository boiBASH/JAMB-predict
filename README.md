# D-nerd's Submission for DataFest'24 Datathon 3.0

**JAMB Score Prediction Using Machine Learning**

![image](https://github.com/user-attachments/assets/67f7f39f-254a-4fec-8b62-5827878c9acf)


## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Demo](#demo)

## Project Overview

This project is Team **D-nerd's** submission for **DataFest'24 Datathon 3.0**. It is a machine learning-based web app that predicts students' JAMB scores based on their grades in various subjects. The model is built using a **Random Forest** classifier and deployed through **Streamlit** for easy interaction.

The project includes a pre-trained `.pkl` model which takes the student's grades in core subjects and predicts their JAMB score. It is designed to provide insights into the possible outcomes for students preparing for JAMB exams.

## Features

- **Grade Input**: Users can input grades for subjects such as Mathematics, English, Biology, Physics, etc.
- **JAMB Score Prediction**: Predicts JAMB scores based on the input grades.
- **Download Predictions**: Users can download the prediction results as a CSV file.
- **Simple Interface**: User-friendly web interface built with Streamlit.

## Installation

### Prerequisites

- Python 3.x
- `joblib`, `pandas`, `scikit-learn`, and `streamlit`

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the Streamlit app by running the command in your terminal:

    ```bash
    streamlit run app.py
    ```

2. The web app interface will open in your default browser.

3. Input the student's grades for each subject and select the department (Arts, Science, or Commercial).

4. Click **Predict JAMB Score** to generate the score.

5. You can also download the prediction as a CSV file.

## Model Details

- **Model Used**: Random Forest Classifier
- **Training Data**: The model was trained on historical student grades and JAMB scores.
- **Input Features**: The model takes grades for the following subjects:
  - Biology, Chemistry, Civic Education, Commerce, Economics, English, Further Mathematics, Government, Geography, Literature in English, Mathematics, Physics.
  
  These grades are mapped from the Nigerian grading system (A1, B2, etc.) to numerical values.

- **Output**: Predicted JAMB score.

## Demo

You can access the live demo of the app here:  
[**JAMB Score Prediction App**](https://jambpredict.streamlit.app/)

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. For major changes, please open an issue to discuss what you would like to change.

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact:

- **Bashirudeen Opeyemi**: [Bashirudeenopeyemi772@gmail.com](mailto:Bashirudeenopeyemi772@gmail.com)
