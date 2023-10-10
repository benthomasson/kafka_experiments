#!/usr/bin/env python3

from kafka import KafkaConsumer

print("Starting consumer")
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9094'], auto_offset_reset='earliest', enable_auto_commit=True,
                         auto_commit_interval_ms=1000, group_id='my-group')
print("Consumer started")
print('waiting for message 1')
for msg in consumer:
    print(msg)
    print('waiting for message 2')

