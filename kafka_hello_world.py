#!/usr/bin/env python3

"""
Kafka Hello World
"""

import kafka

def main():
    """
    Publishes a hello world message to a Kafka topic
    """
    print('connecting')
    producer = kafka.KafkaProducer(bootstrap_servers='localhost:9094')
    print('sending')
    for i in range(1000):
        producer.send('test', 'Hello, World!{}'.format(i).encode('utf-8'))
    print('flushing')
    producer.flush()
    print('done')

if __name__ == "__main__":
    main()
