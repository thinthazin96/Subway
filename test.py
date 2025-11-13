import requests
import json

# API endpoint 
url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts.json"

headers = {
    "Content-Type": "application/json"
}

filename = "TestAlerts.json"

# Send request
response = requests.get(url, headers=headers)

#if the respone is OK, get the data in JSON format.
if response.status_code == 200:
    data = response.json()

    # Save to JSON file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
 
    print(f"Delay alerts saved to '{filename}'")

else:
    print(f"❌ Error: {response.status_code} - {response.text}")
