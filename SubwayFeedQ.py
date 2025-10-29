from google.transit import gtfs_realtime_pb2
import requests
import time

# Real-time feed for NQRW lines
url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get(url)
feed.ParseFromString(response.content)

target_stop = "D37N"  # Example: Times Sq southbound platform

now = time.time()
arrivals = []

for entity in feed.entity:
    if not entity.HasField("trip_update"):
        continue

    trip = entity.trip_update.trip
    if trip.route_id != "Q":
        continue

    for stu in entity.trip_update.stop_time_update:
        if stu.stop_id == target_stop and stu.HasField("arrival"):
            arrival_time = stu.arrival.time
            minutes = (arrival_time - now) / 60
            arrivals.append(round(minutes, 1))

arrivals.sort()

print(f"Upcoming Q trains at {target_stop}:")
for m in arrivals[:5]:
    print(f"→ in {m} minutes")
