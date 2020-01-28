"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("weather process_message is Complete!!")
        # TODO: Process incoming weather messages. Set the temperature and status.
        msg_value = message.value()
        self.temperature = msg_value["temperature"]
        self.status = msg_value["status"]

