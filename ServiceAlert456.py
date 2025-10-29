import requests
import json

# API endpoint 
url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts.json"

headers = {
    "Content-Type": "application/json"
}

target_lines = ["4", "5", "6"]
filename = "4_5_6_train_delay_alerts.json"

# Send request
response = requests.get(url, headers=headers)

#if the respone is OK, get the data in JSON format.
if response.status_code == 200:
    data = response.json()
    filtered_alerts = []

    # Loop to filter 4, 5 and 6 trains only
    for target_line in target_lines:
        
        for alert_entity in data.get("entity", []):
            info = alert_entity.get("alert", {})
            informed_entities = info.get("informed_entity", [])

            for entity in informed_entities:
                route = entity.get("route_id", "")
                if route == target_line:
                    header = info.get("header_text", {}).get("translation", [{}])[0].get("text", "")
                    description = info.get("description_text", {}).get("translation", [{}])[0].get("text", "")
                    full_text = (header + " " + description).lower()

                    if "delay" in full_text:
                        # Store relevant info in a dictionary
                        filtered_alerts.append({
                            "route_id": route,
                            "header_text": header,
                            "description_text": description
                        })

        # Save to JSON file
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(filtered_alerts, f, ensure_ascii=False, indent=4)

        if filtered_alerts:
            print(f"✅ {len(filtered_alerts)} delay alerts saved to '{filename}'")
        else:
            print(f"ℹ️ No current delay alerts for the {target_line} train. JSON file saved empty.")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")
