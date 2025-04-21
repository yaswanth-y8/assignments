from flask import Flask, request, jsonify, Response
import random
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

app = Flask(__name__)

def mock_weather(city):
    now = datetime.utcnow()
    forecast = []
    for i in range(3):  
        day = now + timedelta(days=i)
        forecast.append({
            "date": day.strftime("%d %b %Y"),
            "day": day.strftime("%a"),
            "high": str(random.randint(25, 40)),
            "low": str(random.randint(15, 25)),
            "text": random.choice(["Sunny", "Cloudy", "Rainy", "Partly Cloudy", "Thunderstorms"])
        })

    return {
        "query": {
           
            "results": {
                "channel": {
                    "title": f"Mock Weather - {city}",
                    "location": {
                        "city": city,
                        "country": "India"
                        
                    },
                    "wind": {
                        "chill": str(random.randint(2, 10)),
                        "direction": str(random.randint(0, 360)),
                        "speed": str(random.randint(5, 20))
                    },
                    "atmosphere": {
                        "humidity": str(random.randint(50, 90)),
                        "pressure": str(round(random.uniform(990, 1020), 1)),
                        "visibility": str(round(random.uniform(5, 20), 1))
                    },

                    "item": {
                        "condition": {
                            "temp": str(random.randint(20, 35)),
                            "text": random.choice(["Clear", "Rain", "Cloudy"])
                        },
                        "forecast": forecast
                    }
                }
            }
        }
    }

def dict_to_xml(tag, d):
    ele = ET.Element(tag)
    for k, v in d.items():
        t = type(v)
        if t == dict:
            ele.append(dict_to_xml(k, v))
        elif t == list:
            for i in v:
                ele.append(dict_to_xml(k, i))
        else:
            c = ET.Element(k)
            c.text = str(v)
            ele.append(c)
    
    return ele


@app.route('/<city>')
def weather(city):
    format_type = request.args.get('format', 'json').lower()
    data = mock_weather(city)

    if format_type == 'xml':
        xml_elem = dict_to_xml("response", data)
        xml_str = ET.tostring(xml_elem)
        headers = {'Content-Type': 'application/xml'}
        return Response(xml_str,200, headers)
    else:
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)  
