# OMEGA
The main powerhouse of modern homes.

We are building Omega a computer brain powered by API.AI to understand natural human language and Google STT & TTS to translate human voice input into commands. OMEGA will control most of your home, and use smart sensing to turn off the lights when it detects no activity in the room, control heating and cooling all with simple voice commands or even on autopilot!

### Front End
We plan to use a simple dashboard that will be password protected and accessible to anyone on the network (port forwarding will make it live!) and using this manual commands and controls can be configured. Besides the dashboard a simple app will be used as the mic to control the home and speakers will be implemented around the home to broadcast messages (messages can be put into private mode so only the requester can hear it on their device).

### Back End
Control will be centered at a small Pine64 or possibly a Raspberry Pi, any micro computer really, and Python + Flask will be used to control the brain of the operations. [API.AI](http://api.ai) will take in the output from Google's Speech-to-Text Engine (STT) and process the human language. The brain will receive the intent of the user from API.AI and start following orders. 

### Current Stage
We are LOOKING FOR FUNDING!

At the moment, small parts of the brain work. Text based queries are working, but the mobile app, dashboard, and voice commands are all missing. Of course, the hardware parts are missing as well. We could do with some funding in order to get started!

~ PROJECT HAS BEEN RENAMED FROM SAL9000 TO OMEGA ~

#### Updates
_Feb. 3rd 2016_ - Voice recognition with understanding of intents is working now. The updates will be pushed after things are more stable.




