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
        SubElement(item, 'title').text = item_data.get('header_text', 'No Title')
        SubElement(item, 'description').text = item_data.get('description_text', 'No Description')
        SubElement(item, 'guid').text = item_data.get('roud_id', 'Unknown Route')
        SubElement(item, 'pubDate').text = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

        # Optional: include link if available in JSON
        if 'link' in item_data:
            SubElement(item, 'link').text = item_data['link']

    # Convert XML to text
    return tostring(rss, encoding='utf-8', xml_declaration=True).decode('utf-8')


# === Main Script ===

# Path to your JSON file
json_file_path = "DelayAlerts.json"

# Read the JSON input from file
with open(json_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert JSON to RSS
rss_output = json_to_rss(
    data,
    channel_title="NYC Subway Service Alerts",
    channel_link="https://www.mta.info/",
    channel_description="Live MTA subway service updates"
)

# Write RSS output to file
with open("SubwayRSSv2.xml", "w", encoding="utf-8") as f:
    f.write(rss_output)

print("✅ File 'SubwayRSS.xml' created successfully.")
