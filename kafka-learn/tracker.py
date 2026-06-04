import json
import uuid
from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers":"localhost:9092",
    "group.id":"order-tracker", # identifies consumers of the same instance (ran multiple times to be faster) same app differenet application, automatically distributes load
    "auto.offset.reset": "earliest" # if cannot find the last left off, read from oldest
}

consumer = Consumer(consumer_config)
consumer.subscribe(["orders"])
print("Consumer is running and subscribed to orders")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error}")
            continue
        value = msg.value().decode("utf-8")
        order = json.loads(value) # json to python dict
        print(f"Recieved order: {order['quantity']} * {order['item']} from {order['user']}")
except KeyboardInterrupt:
    print(f"\nStopping Consumer")
finally:
    consumer.close()