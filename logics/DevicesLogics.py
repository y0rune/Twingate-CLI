import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils
import DevicesTransformers
import StdResponses
import StdAPIUtils

def get_device_list_resources(sessionname,token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"

    Body = """{
          devices(after: null, first:100) {
            edges {
              node {
                id
                name
                isTrusted
                osName
                deviceType
              }
            }
            pageInfo {
              startCursor
              hasNextPage
            }
          }
        }"""

    return True,api_call_type,Headers,Body


def device_list(outputFormat,sessionname):
    StdAPIUtils.generic_api_call_handler(outputFormat,sessionname,get_device_list_resources,{},DevicesTransformers.GetListAsCsv)