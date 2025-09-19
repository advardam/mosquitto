import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"  # Replace with broker Pi IP
TOPIC = "test/topic"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    msg = input("Enter message to send: ")
    client.publish(TOPIC, msg)
    print("Message sent!")

