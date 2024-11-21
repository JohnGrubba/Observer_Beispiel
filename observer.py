from publisher import Publisher
import datetime
from datetime import datetime
from abc import ABC


class Observer(ABC):
    def __init__(self, name: str):
        self.name = name
        self.data = []

    def update(self, data):
        value = data["value"]
        print(f"{self.name} received: {value}")
        self.data.append(data)

    def subscribe(self, publisher: Publisher):
        publisher.add_subscriber(self)


class TempMonitor(Observer):
    def __init__(self) -> None:
        super().__init__("TempMonitor")

    def display_temp_history(self):
        for i, temp in enumerate(self.data):
            print(f"{i+1}: {temp}°C")


class FileLoggingMonitor(Observer):
    def __init__(self) -> None:
        super().__init__("FileLoggingMonitor")

    def update(self, data):
        super().update(data)
        recieved_timestamp = datetime.fromtimestamp(data["timestamp"]).strftime(
            "%Y-%m-%d %H:%M:%S.%f"
        )
        value = data["value"]
        with open("temperature_history.csv", "a") as f:
            f.write(f"{recieved_timestamp},{value}\n")


class YoutubeAccount(Observer):
    def __init__(self) -> None:
        super().__init__("YoutubeAccount")

    def update(self, data):
        super().update(data)
        value = data["value"]
        print(f"Chill guy just dropped a new vid: {value}")
