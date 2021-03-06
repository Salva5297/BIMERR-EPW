import os
import json


def removeFileJSON():
    if os.path.exists("converter/DataStorage/metadata.json"):
        os.remove("converter/DataStorage/metadata.json")
        return
    else:
        return

def createFileJson(dataset,epwName):
    documentJSON=open("converter/DataStorage/metadata.json", "a+")
    documentJSON.write("""{
    "@context": "http://www.w3.org/ns/csvw",
    "skipRows": 8,
    "tables":[]}
    """)
    documentJSON.close()

    url = epwName + ".csv"

    a_dict = {
    "url" : url,
    "tableSchema": {
        "columns": [{
          "name": "Year",
          "datatype": "gYear"
        }, {
          "name": "Month",
          "required": True,
          "datatype": "gMonth"
        }, {
          "name": "Day",
          "required": True,
          "datatype":"gDay"
        }, {
          "name": "Hour",
          "required": True,
          "datatype": {
                "base": "number",
                "minimum": "1",
                "maximum": "24"
            }
        }, {
            "name": "Minute",
            "datatype": {
                "base": "number",
                "minimum": "1",
                "maximum": "60"
            }
        }, {
            "name": "DataSourceAndUncertaintyFlags",
            "datatype": "string"
        }, {
            "name": "DryBulbTemperature",
            "null": "99.9",
            "datatype": {
                "base": "number",
                "minimum": "-70",
                "maximum": "70"
            }
        }, {
            "name": "DewPointTemperature",
            "null": "99.9",
            "datatype": {
                "base": "number",
                "minimum": "-70",
                "maximum": "70"
            }
        }, {
            "name": "RelativeHumidity",
            "null": "999",
            "datatype": {
                "base": "number",
                "minimum": "0",
                "maximum": "110"
            }
        }, {
            "name": "AtmosphericStationPressure",
            "null": "999999",
            "datatype": {
                "base": "number",
                "minimum": "31000",
                "maximum": "120000"
            }
        }, {
            "name": "ExtraterrestrialHorizontalRadiation",
            "null": "9999",
            "datatype": {
                "base": "number",
                "minimum": "0"
            }
        }, {
            "name": "ExtraterrestrialDirectNormalRadiation",
            "null": "9999",
            "datatype": {
                "base": "number",
                "minimum": "0"
            }
        }, {
            "name": "HorizontalInfraredRadiationIntensity",
            "null": "9999",
            "datatype": {
                "base": "number",
                "minimum": "0"
            }
        }, {
            "name": "GlobalHorizontalRadiation",
            "null": "9999",
            "datatype": {
                "base": "number",
                "minimum": "0"
            }
            
        }, {
            "name": "DirectNormalRadiation",
            "null": "9999",
            "datatype": {
                "base": "number",
                "minimum": "0",
                "maximum": "9998"                
            }
            
        }, {
            "name": "DiffuseHorizontalRadiation",
            "datatype": {
                "base": "number",
                "minimum": "1",
                "maximum": "9998"                
            },
            "default": "0"
        }, {
            "name": "GlobalHorizontalIlluminance",
            "null": "999999",
            "datatype": {
                "base": "number",
                "minimum": "0",
                "maximum": "999899"                
            }
        }, {
            "name": "DirectNormalIlluminance",
            "null": "999999",
            "datatype": {
                "base": "number",
                "minimum": "0",
                "maximum": "999899"                
            }
        }, {
            "name": "DiffuseHorizontalIlluminance",
            "null": "999999",
            "datatype": {
                "base": "number",
                "minimum": "0",
                "maximum": "999899"                
            }
        }, {
            "name": "ZenithLuminance",
            "null": "9999",
            "datatype": {
                "base": "number",
                "minimum": "0",               
            }
        }, {
            "name": "WindDirection",
            "null": "999",
            "datatype": {
                "base": "number",
                "minimum": "0",
                "maximum": "360"                
            }
        }, {
            "name": "WindSpeed",
            "null": "99",
            "datatype": {
                "base": "number",
                "minimum": "0",
                "maximum": "40"                
            }
        }, {
            "name": "TotalSkyCover",
            "null": "99",
            "datatype": {
                "base": "number",
                "minimum": "0",
                "maximum": "10"                
            }
        }, {
            "name": "OpaqueSkyCover",
            "null": "99",
            "datatype": {
                "base": "number",
                "minimum": "0",
                "maximum": "10"                
            }
        }, {
            "name": "Visibility",
            "null": "9999",
            "datatype": "number"
        }, {
            "name": "CeilingHeight",
            "null": "99999",
            "datatype": "number"
        }, {
            "name": "PresentWeatherObservation",
            "null": "9",
            "datatype": {
                "base": "number",
                "minimum": "0",
                "maximum": "0"                
            }
        }, {
            "name": "PresentWeatherCodes",
            "datatype": {
                "base": "string",
                "minLength": "9",
                "maxLength": "9"                
            }
        }, {
            "name": "PrecipitableWater",
            "datatype": "string"
        }, {
            "name": "AerosolOpticalDepth",
            "null": "999",
            "datatype": "number"
        }, {
            "name": "SnowDepth",
            "null": "999",
            "datatype": {
                "base": "number",
                "minimum": "0"               
            }
        }, {
            "name": "DaysSinceLastSnowfall",
            "null": "99",
            "datatype": {
                "base": "number",
                "minimum": "0"               
            }
        }, {
            "name": "Albedo",
            "datatype": "string"
        }, {
            "name": "LiquidPrecipitationDepth",
            "datatype": {
                "base": "number",
                "minimum": "1"               
            },
            "default": "1.5"
        }, {
            "name": "LiquidPrecipitationQuantity",
            "datatype": {
                "base": "number",
                "minimum": "0"               
            }
        }]
      }
    }

    with open('converter/DataStorage/metadata.json') as f:
        data = json.load(f)

    data['tables'].append(a_dict)

    with open('converter/DataStorage/metadata.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    