# teams-presence-mqtt
Get 

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

https://www.thingiverse.com/thing:4060603

ESPHome