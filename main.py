from observer import TempMonitor, FileLoggingMonitor
from publisher import TemperatureDevice


print("Welcome to Temperatur Sensor Observer!")
device1 = TemperatureDevice()
device2 = TemperatureDevice()

obs1 = TempMonitor()
obs1.subscribe(device1)
obs1.subscribe(device2)

ob2 = FileLoggingMonitor()
ob2.subscribe(device1)
ob2.subscribe(device2)


while True:
    input("Press Enter to stop...\n")

    print("Displaying the history of temperatures recorded by the observer: ")
    obs1.display_temp_history()
