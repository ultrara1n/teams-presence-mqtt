import requests
import json
import time
import os
import paho.mqtt.client as mqtt

def getAccessToken(clientId, refreshToken, redirectUri):
    grant_type = 'refresh_token'
    scope = 'offline_access presence.read'

    payload = {'client_id' : clientId, 'refresh_token' : refreshToken, 'grant_type' : grant_type, 'scope' : scope, 'redirect_uri' : redirectUri}

    getAccessToken = requests.post('https://login.microsoftonline.com/organizations/oauth2/v2.0/token', data=payload)

    response = getAccessToken.json()

    timestamp = time.time()

    accessTokenExpireDate = timestamp + response['expires_in']

    saveToken(accessTokenExpireDate, response['access_token'])

    return response['access_token'] 

def saveToken(expireTimestamp, accessToken):
    tokenData = {}

    tokenData['expire_timestamp'] = expireTimestamp
    tokenData['access_token'] = accessToken

    with open('token.json', 'w') as outfile:
        json.dump(tokenData, outfile)

def getPresence(accessToken):
    presenceRequestHeaders = {'Authorization' : 'Bearer ' + accessToken}

    getPresence = requests.get('https://graph.microsoft.com/v1.0/me/presence', headers=presenceRequestHeaders)

    presenceResponseJson = getPresence.json()

    presenceData = {}
    presenceData['availability'] = presenceResponseJson['availability']
    presenceData['activity'] = presenceResponseJson['activity']

    return presenceData

#load settings
settingsFile = open('settings.json', 'r')
settingsJson = json.loads(settingsFile.read())

mqttClient = mqtt.Client()
mqttClient.username_pw_set(settingsJson['mqtt_username'], settingsJson['mqtt_password'])
mqttClient.connect(settingsJson['mqtt_host'], settingsJson['mqtt_port'], 60)
mqttClient.loop_start()

if os.path.isfile('token.json'):
    tokenFile = open('token.json', 'r')
    try:
        tokenJson = json.loads(tokenFile.read())

        if tokenJson['expire_timestamp'] <= time.time():
            accessToken = getAccessToken(settingsJson['client_id'], settingsJson['refresh_token'], settingsJson['redirect_uri'])
        else:
            accessToken = tokenJson['access_token']

    except ValueError:
        accessToken = getAccessToken(settingsJson['client_id'], settingsJson['refresh_token'], settingsJson['redirect_uri'])
else:
    accessToken = getAccessToken(settingsJson['client_id'], settingsJson['refresh_token'], settingsJson['redirect_uri'])

presenceData = getPresence(accessToken)

mqttClient.publish('home/buero/teams', json.dumps(presenceData))