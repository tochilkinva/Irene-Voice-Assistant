# Core plugin
# author: Vladislav Janvarev

from voiceasscore import VoiceAssCore

# функция на старте
def start(core:VoiceAssCore):
    manifest = {
        "name": "Core plugin",
        "version": "1.7",

        "default_options": {
            "mpcIsUse": True,
            "mpcHcPath": "C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC64\mpc-hc64_nvo.exe",
            "mpcIsUseHttpRemote": False,

            "isOnline": False,
            #"ttsIndex": 0,
            "ttsEngineId": "pyttsx",
            "voiceAssNames": "ирина|ирины|ирину",
            "logPolicy": "cmd", # all | cmd | none
        },

    }
    return manifest

def start_with_options(core:VoiceAssCore,manifest:dict):
    #print(manifest["options"])
    options = manifest["options"]
    #core.setup_assistant_voice(options["ttsIndex"])

    core.mpcHcPath = options["mpcHcPath"]
    core.mpcIsUse = options["mpcIsUse"]
    core.mpcIsUseHttpRemote = options["mpcIsUseHttpRemote"]
    core.isOnline = options["isOnline"]

    core.voiceAssNames = options["voiceAssNames"].split("|")
    core.ttsEngineId = options["ttsEngineId"]
    core.logPolicy = options["logPolicy"]




    return manifest
