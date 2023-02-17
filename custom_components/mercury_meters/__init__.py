"""The RS-485 Electricity Meters integration.

Integration for reading the data from Electricity Meters
through it's build-in RS485 interface using ZigBee -> RS485 modem.

Current integration uses MQTT bus for communication.

Example of configuration.yaml entry:
# Electricity Counter
electro_meters:
  - type: mercury200.02
    serial_number: !secret mercury_serial # example: "04023330"
    topic: "zigbee2mqtt/electricity_meter" # the topic of MQTT zigbee2RS485 modem
"""

import logging
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
import threading
from . import BaseMeters

_LOGGER = logging.getLogger(__name__)

DOMAIN = "electro_meters"


METER_MODELS = ( "mercury200.02", "mercury230art")

REQ_LOCK = threading.Lock()
CONFIG_SCHEMA = vol.Schema(
	{

	},
	extra=vol.ALLOW_EXTRA,
)