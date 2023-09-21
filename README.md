# VitalAI Healthcare Platform - Backend Ai Server

![VitalAI Logo](https://github.com/Vital-Ai-GH/frontend-web/blob/main/src/assets/Vital-Ai-Cover-Logo.png)

Welcome to the backend repository of VitalAI, a revolutionary healthcare platform that aims to connect patients with licensed medical professionals through advanced Artificial Intelligence.
This repository contains a Python Flask backend server that integrates AI models for Question and Answering (Q&A), disease prediction, and drug recommendation. The server provides an interface for these functionalities through APIs.

## Table of Contents

- [Installation](#installation)
- [Database Setup](#database-setup)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Question and Answering (Q&A):** Utilizes AI models to answer questions based on provided context and questions.
- **Disease Prediction:** Predicts diseases based on given symptoms or medical history.
- **Drug Recommendation:** Recommends drugs based on the diagnosed diseases and patient information.

## Technologies Used

- **Python Flask:** A micro web framework used for creating APIs.
- **AI Models:** Utilizes various AI models for Q&A, disease prediction, and drug recommendation.
- **RESTful API:** API endpoints are designed following RESTful principles for efficient communication.

## Installation

Clone the repository

```bash
git clone https://github.com/Vital-Ai-GH/backend-ai-server.git

cd backend-ai-healthcare
```

## Database Setup

Before running the backend, you need to configure the database connections.

## Run Server

```bash
python app.py
```

### Q&A API

Send a POST request to /api/qa with the context and question in the request body to get the answer.

### Disease Prediction API

Send a POST request to /api/disease-prediction with the symptoms in the request body to predict the disease.

### Drug Recommendation API

Send a POST request to /api/drug-recommendation with the diagnosed_disease and patient_info in the request body to get drug recommendations.

## API Documentation (coming soon)

## Contributing

We welcome contributions to improve VitalAI! Feel free to open issues, submit pull requests, or provide feedback to help us enhance our platform.

## License

VitalAI is released under the [MIT License](https://opensource.org/licenses/MIT).

---

For more information about the front-end of VitalAI, please visit the [frontend repository](https://github.com/Vital-Ai-GH/frontend-web/tree/main). If you have any questions or need support, contact us at [nyamekessesamuel@duck.com](mailto:nyamekessesamuel@duck.com). Thank you for being a part of the VitalAI community!
