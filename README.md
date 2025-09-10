# 🧠 Digit Recognition Web App using ANN + Docker + Cloud Deployment

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Overview
This project is a web-based digit recognition system built using an Artificial Neural Network (ANN) trained on the MNIST dataset. The app is developed with Streamlit and containerized using Docker for easy deployment. Optionally, it can be deployed to cloud platforms like Render, Railway, or Google Cloud Run.

---

## 🎥 Demo
Coming soon: [Live Demo Link](#)

---

## 🚀 Features
- 🎨 Draw or upload digit images
- 🔍 Real-time digit prediction using ANN
- 🐳 Dockerized for portability
- ☁️ Optional cloud deployment
- 📊 Clean UI with Streamlit

---

## 🛠️ Tech Stack
- **Python 3.9**
- **TensorFlow / Keras** – ANN model
- **Streamlit** – Web interface
- **Docker** – Containerization

---

## 📁 Project Structure
```
digit-recognition-ann/
│
├── model/
│   └── ann_model.h5
├── app/
│   ├── app.py
│   ├── utils.py
│   └── assets/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/digit-recognition-ann.git
cd digit-recognition-ann

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app/app.py
```

---

## 🐳 Docker Usage
```bash
# Build Docker image
docker build -t digit-ann-app .

# Run Docker container
docker run -p 8501:8501 digit-ann-app
```

---

## 🖼️ Screenshots
Coming soon: Add screenshots of the app UI and predictions.

---

## 📄 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author
**Vaibhav Balwant Singh**  
B.Tech CSE (AI/ML)
