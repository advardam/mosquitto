import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"  # Replace with broker Pi IP
TOPIC = "test/topic"

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)

client.subscribe(TOPIC)
print("Listening for messages...")

client.loop_forever()

