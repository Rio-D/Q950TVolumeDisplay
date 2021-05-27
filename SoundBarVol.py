import aiohttp
import pysmartthings
import asyncio
import time

token = '8258335a-1d42-4300-a8cb-75442561b1f9'

def setOFFScreen():
    print("Setting screen to off here")

def setOFFScreen():
    print("Setting screen to off here")

def setMuteScreen():
    print("Setting screen to mute here")

def setVolumeScreen(volume):
    print("Set Volume Here")

async def acount():
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        print(len(devices))

        device = devices[0]
        print(device.device_id)
        print(device.name)
        print(device.label)

        refreshTime = 1

        await device.status.refresh()

        previousSwitch = device.status.switch
        previousVolume = device.status.volume
        previousMute = device.status.mute

        i = 1
        while i == 1:
            await device.status.refresh()
            if previousSwitch != device.status.switch:
                previousSwitch = device.status.switch
                if device.status.switch == True:
                    refreshTime = 0.1
                    setVolumeScreen(device.status.volume)
                else:
                    refreshTime = 1
                    setOFFScreen()


                # Set OFF Image

            print(device.status.switch)
            print(device.status.volume)
            print(device.status.mute)
            time.sleep(refreshTime) 

        
        


asyncio.run(acount())
