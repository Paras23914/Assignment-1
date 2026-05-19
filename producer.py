from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient,NewTopic

import pandas as pd
import json
import time

try:
    admin=KafkaAdminClient(
        bootstrap_servers="localhost:9092"
    )
    topic=NewTopic(
        name="raw-weather",
        num_partitions=1,
        replication_factor=1
    )
    admin.create_topics(new_topics=[topic])
    print ("New Topic raw-weather created")
except Exception as e:
    print(e)

producer=KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer = lambda v: json.dumps(v).encode('utf-8')
)

df=pd.read_csv("Weather.csv")
df = df[[
    "Temp (C)",
    "Rel Hum (%)",
    "Wind Spd (km/h)",
    "Stn Press (kPa)"
]]
df=df.dropna()
# Just for test
# df=df.head(50)
for index,row in df.iterrows():
    data={
        "Temp": row["Temp (C)"],
        "Humidity": row["Rel Hum (%)"],
        "WindSpeed": row["Wind Spd (km/h)"],
        "Pressure": row["Stn Press (kPa)"]
    }
    print("a")
    producer.send(
        topic="raw-weather",
        value=data
    )

    print("Sent:",data)

    time.sleep(1)
producer.flush()