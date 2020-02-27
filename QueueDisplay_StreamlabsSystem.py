#---------------------------------------
#   Import Libraries
#---------------------------------------
import sys
import json
import codecs
import os

#---------------------------------------
#   [Required] Script Information
#---------------------------------------
ScriptName = "Queue Display"
Website = "twitch.tv/encryptedthoughts"
Description = "A script to populate an overlay showing queue information in an overlay"
Creator = "EncryptedThoughts"
Version = "1.0.0"

# ---------------------------------------
#	Set Variables
# ---------------------------------------
SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")
ReadMe = os.path.join(os.path.dirname(__file__), "README.md")
ScriptSettings = None

# ---------------------------------------
#	Script Classes
# ---------------------------------------
class Settings(object):
    def __init__(self, settingsfile=None):
        with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
            self.__dict__ = json.load(f, encoding="utf-8")

    def Reload(self, jsonData):
        self.__dict__ = json.loads(jsonData, encoding="utf-8")

# ---------------------------------------
#	Functions
# ---------------------------------------
def UpdateQueue():

    payload = {}
    queue = Parent.GetQueue(10)
    count = 1
    for item in queue:
        payload[str(count)] = queue[item]
        count += 1

    Parent.Log(ScriptName, str(payload))

    Parent.BroadcastWsEvent("EVENT_QUEUE_UPDATE", json.dumps(payload))
    return

def ChangeQueueStatus(status):
    payload = { "status": status }
    Parent.BroadcastWsEvent("EVENT_QUEUE_STATUS", json.dumps(payload))
    return

#---------------------------------------
#   [Required] Initialize Data / Load Only
#---------------------------------------
def Init():
    global ScriptSettings
    ScriptSettings = Settings(SettingsFile)
    return

# ---------------------------------------
# Chatbot Save Settings Function
# ---------------------------------------
def ReloadSettings(jsondata):
    ScriptSettings.Reload(jsondata)
    return

def Execute(data):

    if data.IsChatMessage():
        if "!queue open" in data.Message.lower():
            if Parent.HasPermission(data.User,"Moderator",""):
                ChangeQueueStatus("Open")
        elif "!queue close" in data.Message.lower():
            if Parent.HasPermission(data.User,"Moderator",""):
                ChangeQueueStatus("Closed")
    
    UpdateQueue();

    return

def Tick():
    return

# ---------------------------------------
# Script UI Button Functions
# ---------------------------------------
def OpenReadMe():
    os.startfile(ReadMeFile)
    return
