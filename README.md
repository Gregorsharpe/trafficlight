This is a small project intended to run on a Raspberry Pi Zero W with a Pimoroni "pHAT" LED matrix accessory attached.
It listens to an external MQTT server for commands passed on a specified channel and modifys the display accordingly, similar to a traffic light.
When combined with a physical button interface, smarthome integration with a tool like Home Assistant or even the command line it serves as an excellent way to notify housemates of your availability during work hours.

Install:
pip3 install -r requirements.txt
python3 main.py