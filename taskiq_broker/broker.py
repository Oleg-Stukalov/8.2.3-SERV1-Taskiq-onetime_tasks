from taskiq_nats import NatsBroker, PullBasedJetStreamBroker

# without NATS JetStream (only NATS Core)
###broker = NatsBroker(servers="nats://127.0.0.1:4222", queue="taskiq_queue")

# with NATS JetStream
broker = PullBasedJetStreamBroker(servers="nats://127.0.0.1:4222", queue="taskiq_queue")
