from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_transaction():
    return {
        'transaction_id': random.randint(1000, 9999),
        'user_id': random.randint(1, 100),
        'amount': round(random.uniform(10.0, 5000.0), 2),
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

while True:
    txn = generate_transaction()
    producer.send('transactions', value=txn)
    print(f"Produced: {txn}")
    time.sleep(1)
