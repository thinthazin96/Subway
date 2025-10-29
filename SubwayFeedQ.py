import requests
import json

# API endpoint 
url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw.json"

headers = {
    "Content-Type": "application/json"
}

# Send GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to JSON

    # Save the data as a JSON file
    with open("Q_Train_Arrival.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("✅ Data saved successfully as 'Q_Train_Arrival.json'")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")
