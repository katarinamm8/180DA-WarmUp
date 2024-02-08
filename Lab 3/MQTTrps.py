import paho.mqtt.client as mqtt
import time

class RockPaperScissorsPlayer:
    def __init__(self, player_name):
        self.player_name = player_name

    def on_connect(self, client, userdata, flags, rc):
        print(f"{self.player_name} Connected with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        # Process results received from the server
        pass

player2 = RockPaperScissorsPlayer("Player2")
client2 = mqtt.Client("player2")
client2.on_connect = player2.on_connect
client2.on_message = player2.on_message
client2.connect('mqtt.eclipseprojects.io', 1883)
client2.loop_start()

while True:
    # Get user input and publish the choice to the server
    choice = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
    client2.publish("rock_paper_scissors/player2", choice, qos=1)
    time.sleep(1)
0
