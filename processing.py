from kafka.admin import KafkaAdminClient, NewTopic
import faust
import joblib
import asyncio

asyncio.set_event_loop(asyncio.new_event_loop())

try:
    admin=KafkaAdminClient(
        bootstrap_servers="localhost:9092"
    )
    topic=NewTopic(
        name="predictions",
        num_partitions=1,
        replication_factor=1
    )
    admin.create_topics(new_topics=[topic])
    print("Predictions topic created")
except Exception as e:
    if 'already exists' in str(e):
        print("Topic already exists")
    else: 
        raise

model=joblib.load('weather_model.pkl')

app=faust.App(
    "weather-app",
    broker="kafka://localhost:9092"
)

raw_topic= app.topic(
    "raw-weather",
    value_serializer="json"
)

prediction_topic=app.topic(
    "predictions",
    value_serializer="json"
)

@app.agent(raw_topic)
async def process(stream):
    async for event in stream:
        features=[[
            event["Temp"],
            event["Humidity"],
            event["WindSpeed"],
            event["Pressure"]
        ]]
        prediction=model.predict(features)[0]
        result={
            "CurrentTemp":event['Temp'],
            "PredictedNextTemp":round(prediction,2)
        }
        await prediction_topic.send(value=result)
        print(result)