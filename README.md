# Assignment 1 - Real-Time Streaming with Apache Kafka

## Overview
This project demonstrates a real-time weather streaming pipeline using Apache Kafka, Faust, and Machine Learning.

Weather data is streamed row-by-row from a CSV dataset into Kafka topics. A Faust stream processor consumes the data, applies a trained ML model, and publishes prediction results into another Kafka topic. A consumer continuously reads and displays predictions in real time.

---

## Technologies Used
- Apache Kafka
- Faust Streaming
- Python 3.12
- Docker
- Pandas
- Scikit-learn
- Joblib

---

## Dataset
Weather Dataset (Oshawa/Toronto)

ML Task:
Predict next-hour temperature.

---

## Project Architecture

```text
Producer
   ↓
raw-weather topic
   ↓
Faust Stream Processor
   ↓
predictions topic
   ↓
Consumer
````

---

## Files

* producer.py → Sends weather data to Kafka
* processing.py → Faust stream processor with ML prediction
* consumer.py → Reads prediction results
* weather_model.pkl → Trained ML model
* requirements.txt → Dependencies
* docker-compose.yml → Kafka setup

---

## Kafka Topics

* raw-weather
* predictions

---

## Install Dependencies

```bash
py -3.12 -m pip install -r requirements.txt
```

---

## Run Kafka

```bash
docker-compose up -d
```

Kafka UI:

```text
http://localhost:8080
```

---

## Run Project

### Terminal 1

```bash
py -3.12 -m faust -A processing worker -l info
```

### Terminal 2

```bash
py -3.12 consumer.py
```

### Terminal 3

```bash
py -3.12 producer.py
```

---

## Output

* Producer streams weather events
* Faust processes ML predictions
* Consumer displays live prediction results
---

## Video Demo

Google Drive Link:

https://drive.google.com/file/d/1OEUU2qxGiUqhK4Z_fRJTmjPF0-30T6VY/view?usp=sharing

[Watch Video Demo](https://drive.google.com/file/d/1OEUU2qxGiUqhK4Z_fRJTmjPF0-30T6VY/view?usp=sharing)

## Author

Paras Sharma
101040066

