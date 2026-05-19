from kafka import KafkaConsumer
import json


consumer=KafkaConsumer(
    'predictions',
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x:json.loads(x.decode("utf-8"))
)
print("Waiting for Prediction messages....")
for message in consumer:
    data=message.value
    print("Prediction Received:")
    print(f"Current Temp        : {data['CurrentTemp']}")
    print(f"Predicted Next Temp : {data['PredictedNextTemp']}")
    print("-" * 40)