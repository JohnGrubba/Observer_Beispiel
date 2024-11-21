import random
import threading
from typing import Set
import time
from abc import ABC


class Publisher(ABC):
    def __init__(self) -> None:
        self.observers: Set = set()

    def add_subscriber(self, subscriber):
        self.observers.add(subscriber)

    def _publish(self, data):
        print(f"Publishing: {data}")
        for observer in self.observers:
            observer.update(data)


class TemperatureDevice(Publisher):
    def __publish_thread(self):
        while True:
            self.previous_temperature += random.randint(-1, 1)
            self._publish(
                {"value": self.previous_temperature, "timestamp": time.time()}
            )
            time.sleep(random.random() * 2)

    @staticmethod
    def __random_temp():
        return random.randint(5, 40)

    def __init__(self):
        super().__init__()
        self.previous_temperature = TemperatureDevice.__random_temp()
        threading.Thread(target=self.__publish_thread).start()


class YoutubeChillGuy(Publisher):
    def __publish_thread(self):
        while True:
            self._publish(
                {"video_id": random.randint(1, 1000), "timestamp": time.time()}
            )
            time.sleep(60)

    def __init__(self):
        super().__init__()
        threading.Thread(target=self.__publish_thread).start()
