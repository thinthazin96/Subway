import requests
import json

# MTA real-time feed for N, Q, R, and W lines
url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw.json"

headers = {
    "Content-Type": "application/json"
}

# Send GET request
response = requests.get(url, headers=headers)

if response.status_code == 200:
    try:
        data = response.json()  # Convert response to JSON

        q_line_data = []
        for entry in data.get("entity", []):
            trip_update = entry.get("trip_update")
            if not trip_update:
                continue

            trip = trip_update.get("trip")
            if not trip:
                continue

            if trip.get("route_id") == "Q":
                q_line_data.append(entry)

        # Save filtered data
        with open("Q_Train_Arrival.json", "w", encoding="utf-8") as f:
            json.dump(q_line_data, f, ensure_ascii=False, indent=4)

        print(f"✅ Saved {len(q_line_data)} Q line records as 'Q_Train_Arrival.json'")

    except json.JSONDecodeError:
        print("❌ Error: The API did not return valid JSON data.")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")
