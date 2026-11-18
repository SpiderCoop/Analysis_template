"""
Description:   Provides functions to interact with external APIs, handling requests and responses efficiently.
Author:        David Jiménez Cooper - SpiderCoop
Date:          2026-09-30
"""

from econ_api_bridge.banxico import Banxico_SIE
from econ_api_bridge.inegi import INEGI_BIE

from config import BANXICO_TOKEN, INEGI_TOKEN

inegi_bie = INEGI_BIE(INEGI_TOKEN)
banxico_sie = Banxico_SIE(BANXICO_TOKEN)