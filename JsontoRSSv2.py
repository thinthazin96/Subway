import json
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring

def json_to_rss(json_data, channel_title, channel_link, channel_description):
    # Create root RSS element
    rss = Element('rss', version='2.0')
    channel = SubElement(rss, 'channel')

    # Required channel metadata for RSS 2.0
    SubElement(channel, 'title').text = channel_title
    SubElement(channel, 'link').text = channel_link
    SubElement(channel, 'description').text = channel_description
    SubElement(channel, 'language').text = 'en-us'
    SubElement(channel, 'lastBuildDate').text = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

    # Loop through each JSON entry and create an <item>
    for item_data in json_data:
        item = SubElement(channel, 'item')
        SubElement(item, 'title').text = item_data.get('headerText', 'No Title')
        SubElement(item, 'description').text = item_data.get('description', 'No Description')
        SubElement(item, 'guid').text = item_data.get('routeID', 'Unknown Route')
        SubElement(item, 'pubDate').text = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        # Optional: add a link for each item (if applicable)
        if 'link' in item_data:
            SubElement(item, 'link').text = item_data['link']

    # Convert to string with XML declaration
    return tostring(rss, encoding='utf-8', xml_declaration=True).decode('utf-8')

# Sample JSON input
json_input = """
[
    {
        "routeID": "Q",
        "headerText": "No [B] service between Prospect Park and Brighton Beach. Extremely limited [Q] service between Prospect Park and Coney Island-Stillwell Av.",
        "description": "We're removing a fallen tree from the tracks at Sheepshead Bay."
    }
]
"""

# Load JSON
data = json.loads(json_input)

# Convert JSON to RSS
rss_output = json_to_rss(data, "NYC Subway Service Alerts", "https://example.com/subway-alerts", "Live MTA subway service updates")

# Write to file
with open("SubwayRSS.xml", "w", encoding="utf-8") as f:
    f.write(rss_output)

print("✅ File 'SubwayRSS.xml' created successfully.")
print(rss_output)
