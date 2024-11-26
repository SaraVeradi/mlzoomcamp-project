import requests
import json
url = 'http://localhost:9696/predict'

exc = {
 "gender": "male",
 "age": 26,
 "height": 2.11,
 "weight": 113.0,
 "duration": 15.0,
 "heart_rate": 103.0,
 "body_temp": 40.1,
 "bmi": 25.3812807439186}


response = requests.post(url, json=exc)
result = response.json()

print('calories')
print(json.dumps(result, indent=2))
