import uuid
import json
from confluent_kafka import Producer

producer_config = {'bootstrap.servers':'localhost:9092'}
producer = Producer(producer_config)

order = {
    "order_id" : str(uuid.uuid4()),
    "user" : "diddy",
    "item": "baby oil",
    "quantity": 100
}

def delivery_report(err,msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivery Successful: {msg.value().decode("utf-8")}")
        print(dir(msg))

value = json.dumps(order).encode("utf-8") # convert json to bytes
producer.produce(
    topic="orders",
    value=value,
    callback=delivery_report
) # save value to topic calls orders, automatically creates topic if not exists
producer.flush() # makes sure queued orders get sent before program end