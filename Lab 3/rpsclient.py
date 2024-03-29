import paho.mqtt.client as mqtt

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

def on_message(client, userdata, message):
    print(message.payload.decode('utf-8'))

# MQTT setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# Connect to the MQTT broker
client.connect_async('mqtt.eclipseprojects.io')
client.loop_start()

# Game loop
while True:
    user_choice = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
    client.publish("ece180d/game", user_choice, qos=1)

# Stop the MQTT loop when the game ends
client.loop_stop()
client.disconnect()
