from taskiq_nats import NatsBroker

broker = NatsBroker(servers="nats://127.0.0.1:4222", queue="taskiq_queue")