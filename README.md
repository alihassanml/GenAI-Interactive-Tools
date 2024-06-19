# GenAI Interactive Tools

Welcome to the GenAI Interactive Tools repository! This project consists of two distinct generative AI applications: one for text-based question answering and another for image recognition. Both applications are visualized using Streamlit for a user-friendly interface.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

### 1. Text-Based Question Answering
This tool allows users to ask questions, and it provides answers using a generative AI model. It's designed to understand and generate human-like responses to a wide range of questions.

### 2. Image Recognition
This tool enables users to upload an image, and it identifies the content of the image using a trained AI model. It's capable of recognizing various objects and providing detailed descriptions.

## Features

- **Text-Based Question Answering:**
  - User-friendly interface to input questions
  - AI-generated answers in real-time

- **Image Recognition:**
  - Easy image upload functionality
  - Detailed analysis and description of uploaded images

- **Streamlit Visualization:**
  - Interactive and responsive web interface
  - Real-time display of AI responses

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/alihassanml/GenAI-Interactive-Tools.git
    cd GenAI-Interactive-Tools
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit application:

1. Start the Streamlit server:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to interact with the applications.

### Text-Based Question Answering

1. Navigate to the text question-answering section.
2. Input your question in the provided text box.
3. Press the "Submit" button to receive the AI-generated answer.

### Image Recognition

1. Navigate to the image upload section.
2. Upload an image using the file uploader.
3. The AI model will analyze the image and display the results.

## Contributing

We welcome contributions to improve and expand this project. To contribute, please fork the repository, create a new branch for your feature or bugfix, and submit a pull request.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to modify the content to better fit your specific project details or preferences.
