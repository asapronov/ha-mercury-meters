import logging

import voluptuous as vol

from homeassistant.components.switch import SwitchEntity, PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME, CONF_SENSORS
import homeassistant.helpers.config_validation as cv
from . import DOMAIN, REQ_LOCK

_LOGGER = logging.getLogger(__name__)


CONF_METER_SN = "serial_number"
CONF_METER_MODEL = "model"


METER_SCHEMA = vol.Schema(
	{


        vol.Required(CONF_METER_SN): cv.string,
        vol.Required(CONF_METER_MODEL, default=0): cv.positive_int,


        vol.Required(CONF_CODE_OFF): vol.All(cv.ensure_list_csv, [cv.positive_int]),
		vol.Required(CONF_CODE_ON): vol.All(cv.ensure_list_csv, [cv.positive_int]),
		vol.Optional(CONF_LENGTH, default=32): cv.positive_int,
		vol.Optional(CONF_SIGNAL_REPETITIONS, default=15): cv.positive_int,
		vol.Optional(CONF_PROTOCOL, default=2): cv.positive_int,
		vol.Optional(CONF_ENABLE_RECEIVE, default=False): cv.boolean,
	}
)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
	{
		vol.Required(CONF_SWITCHES): vol.Schema({cv.string: SWITCH_SCHEMA}),
	}
)