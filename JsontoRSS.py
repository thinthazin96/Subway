import json
from xml.etree.ElementTree import Element, SubElement, tostring

#Function to convert Json to RSS
def json_to_rss(json_data, routeID, headerText, description):
    rss = Element('rss', version='2.0')
    channel = SubElement(rss, 'channel')
    SubElement(channel, 'routeID').text = routeID
    SubElement(channel, 'headerText').text = headerText
    SubElement(channel, 'description').text = description

    #Loop each key and value in each array.
    for item_data in json_data:
        item = SubElement(channel, 'item')
        SubElement(item, 'routeID').text = item_data.get('routeID')
        SubElement(item, 'headerText').text = item_data.get('headerText')
        SubElement(item, 'description').text = item_data.get('description')
        # Add other RSS elements as needed (pubDate, guid, etc.)

    #Convert to readable format
    return tostring(rss, encoding='utf-8', xml_declaration=True).decode('utf-8')

# Sample JSON data
json_input = """
[
    {"routeID": "Q", "headerText": "No [B] service between Prospect Park and Brighton Beach.Extremely limited [Q] service between Prospect Park and Coney Island-Stillwell Av.", "description": "What's Happening?We're removing a fallen tree from the tracks at Sheepshead Bay."}
]
"""
#Load Json data
data = json.loads(json_input)

#Call json_to_rss function to convert the file
rss_output = json_to_rss(data, "My Awesome Feed", "https://example.com", "A feed of my articles")

with open("SubwayRSSv1.xml", "w") as f:
    f.write(rss_output)
print("File 'SubwayRSSv1.xml' created/overwritten.")

#print out the rss file
print(rss_output)