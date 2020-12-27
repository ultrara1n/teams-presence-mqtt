# teams-presence-mqtt
![communication flow](https://raw.githubusercontent.com/ultrara1n/teams-presence-mqtt/main/media/communication-flow.jpg)

## Prerequisites
You will need to create an app with sufficient privileges to authorize with and get the needed access/refresh tokens.

--> How to until refresh token here

## settings.json
Rename settings.json.example to settings.json and fill out all fields
Field | Description
--- | ---
check_every | Seconds to check again
mqtt_host | MQTT Host
mqtt_port | MQTT Port
mqtt_username | MQTT Username
mqtt_password | MQTT Password
client_id | Azure App Client-ID
redirect_uri | The redirect URI of your Azure App
refresh_token | Azure App refresh Token

## Integrate with Home Assistant
I'm using this config to get both status into my home automating system
```yaml
#Teams
- platform: mqtt
  name: "Teams Availability"
  state_topic: "home/buero/teams"
  value_template: '{{ value_json.availability }}'
- platform: mqtt
  name: "Teams Activity"
  state_topic: "home/buero/teams"
  value_template: '{{ value_json.activity }}'
```

## Build Teams status cube
Inspired by https://github.com/toblum/ESPTeamsPresence
### BOM
To put all the materials in, i've printed this nice cube from thingiverse https://www.thingiverse.com/thing:4060603

Material | Price | Source
--- | --- | ---
Wemos D1 compatible Board | 7,50€ | https://www.amazon.de/gp/product/B08BTYX1WL/
8x8 WS2812 LED Matrix | 10€ | https://www.amazon.de/gp/product/B078HYP681/
Cables | |

There are of course cheaper sources for the parts, but I had no patience to wait the few months for them to arrive, for example the ESP8266 Board here https://www.aliexpress.com/item/32822012864.html and the LED Matrix here https://www.aliexpress.com/item/32653027272.html

### Software and flashing

ESPHome

### Home Assistant Automation