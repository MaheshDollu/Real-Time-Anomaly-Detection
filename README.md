# 🔍 Real-Time Anomaly Detection using Kafka and Spark

This project implements a real-time anomaly detection pipeline using Apache Kafka for streaming data, Apache Spark for distributed processing, and a trained machine learning model for detecting anomalies on-the-fly.

---

## 🚀 Project Overview

This pipeline is built for real-time anomaly detection in streaming data environments. It captures live data from Kafka topics, processes it using Spark Structured Streaming, and flags anomalies using a trained machine learning model.

---

## ⚙️ Technologies Used

- **Python**
- **Apache Kafka** – Real-time data streaming
- **Apache Spark** – Structured Streaming for distributed processing
- **scikit-learn** – Model training
- **joblib** – Model serialization
- **VS Code** – Development environment

---

## 🛠️ Setup Instructions

### 1. Clone the repository


    git clone https://github.com/MaheshDollu/Real-Time-Anomaly-Detection.git
    cd Real-Time-Anomaly-Detection

### 2. Set up a Python environment

    python3 -m venv venv
  source venv/bin/activate        # On Windows: venv\Scripts\activate
  pip install -r requirements.txt

### 3. Start Kafka
Start Kafka locally (follow the official Kafka quickstart) or use a cloud-based Kafka service. Make sure:

ZooKeeper is running

Kafka broker is active

The topic for streaming is created

## 📈 Usage

### Train the Machine Learning Model:
Run the model training script to train and save your anomaly detection model in the saved_model/ directory.

### Start Kafka Producer (Optional):
Use the producer script to generate or simulate data and publish it to the Kafka topic. Ensure topic name and broker details are correctly configured in the script.

### Run the Spark Streaming Consumer:
Start the Spark consumer script to read from the Kafka topic, apply the trained model, and flag anomalies in real-time. Confirm the model path and Kafka configurations are correctly set.









