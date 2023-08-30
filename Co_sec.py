__author__ = "Sofien"
__version__ = "1.0"

import enetsdk as Enet
import enetsdk as ent
import enetsdk as Enet

from tiermap.tier_mapper import TierMapper
from tiermap import exceptions
from enetsdk.Framework.cm_handler import EMSHandler
from enet_sdk_cm.enet_cm_writer import EdenNetCMWriter, CMChangeUpdate, CMChangeCreate, CMChangeDelete
from enet_sdk_cm.enet_neighbor_manager import EdenNetCMNeighborManager, NeighborFilter, INTER_RAT, INTRA_FREQUENCY, INTER_FREQUENCY
from enet_sdk_cm.enet_cm_writer import EdenNetCMWriter, RollbackFilter
from datetime import datetime, timedelta
from enetconfig.config import ConfigManager
from datetime import datetime, timedelta
from enetconfig.config import ConfigManager
import sys

from enet_sdk_cm.enet_neighbor_manager import EdenNetCMNeighborManager, NeighborFilter, INTER_RAT, INTRA_FREQUENCY, INTER_FREQUENCY
from enet_sdk_cm.cm_reader import TierFilter, CellFilter, CustomCell
from enet_sdk_cm.cm_reader import MetadataFilterByDns

from enet_sdk_cm.dn_builder import SDKDNBuilder
import json

from enetcosectors.cosectors import CosectorCache

#=============================================================
# Framework Functions
#=============================================================
Parameter_GUI = [
    (
         "KPI name", #Parameter Name
         "Name of KPI to retrieve and display.", #Parameter Description
         Enet.ENET_PARAM_TYPE_KPI, #Parameter Type
         "Voice_Calls_Completed", #Default Value
         None # Acceptable Value. Ignore for this parameter type
    ),
    (
         "KPI Threshold", #Parameter Name
         "Threshold for selected KPI values before the module take action.", #Parameter Description
         Enet.ENET_PARAM_TYPE_INT_RANGE, #Parameter Type
         10, #Default Value
         [0,100,10] # Acceptable Value. (min,max,step)
    )
]

def GetEventTypes():
#     """Return a list of trigger types"""
#     """This script can be triggered by an Operator initiated or KPI arrival event"""
    return [Enet.ENET_SON_EVT_TIME]

def get_trigger_info(module_instance):
    trigger_interval = 2
    return {"interval": trigger_interval, "is_recurring": True}


def GetDesc():
    """Return the description of this module"""
    return "This is a Basic_Info Module."


def GetVersion():
    """Return the current version of this module"""
    return __version__
    
def GetScopeRules():
    return dict(
        tech=['NR','LTE','UMTS', 'GSM'], 
        multi_vendor=True, 
        multi_tech=True, 
        multi_oss=True,
        vendor=['nokia', 'ericsson'], 
        closed_loop=True, 
      # maintenance_window_support = {"Enable": True,"schedule_provision": "in_maintenance_window"}
               ) 

def GetParameters():  
    return Enet.ScriptParametersFromTuples(Parameter_GUI)

def ScriptMain(script_data,reserved):
    """Return the description of this module"""
  
    params = script_data.GetParameters()
    son_mode = params['SON Operation Mode']
    print("SON Operation Mode", son_mode)
    event = script_data.GetEvent()
    print ("event",event)

# Retrieving cosectors and cosites is done using the get_cosectors() and get_cosite() functions.
    cosectors = CosectorCache.create(script_data)
    targets = script_data.GetTargets()

    for cell in targets:
        print("{}'s Cosectors: {}".format(cell, cosectors.get_cosectors(cell)))
      #  print("{}'s Cosites: {}".format(cell, cosectors.get_cosites(cell)))

