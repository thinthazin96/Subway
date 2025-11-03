import json
from xml.etree.ElementTree import Element, SubElement, tostring

#Function to convert Json to RSS
def json_to_rss(json_data, title, link, description):
    rss = Element('rss', version='2.0')
    channel = SubElement(rss, 'channel')
    SubElement(channel, 'title').text = title
    SubElement(channel, 'link').text = link
    SubElement(channel, 'description').text = description

    #Loop each key and value in each array.
    for item_data in json_data:
        item = SubElement(channel, 'item')
        SubElement(item, 'title').text = item_data.get('title')
        SubElement(item, 'link').text = item_data.get('link')
        SubElement(item, 'description').text = item_data.get('description')
        # Add other RSS elements as needed (pubDate, guid, etc.)

    #Convert to readable format
    return tostring(rss, encoding='utf-8', xml_declaration=True).decode('utf-8')

# Sample JSON data
json_input = """
[
    {"title": "Article 1", "link": "https://example.com/article1", "description": "Description for article 1"},
    {"title": "Article 2", "link": "https://example.com/article2", "description": "Description for article 2"}
]
"""
#Load Json data
data = json.loads(json_input)

#Call json_to_rss function to convert the file
rss_output = json_to_rss(data, "My Awesome Feed", "https://example.com", "A feed of my articles")

with open("SubwayRSS.xml", "w") as f:
    f.write(rss_output)
print("File 'SubwayRSS.xml' created/overwritten.")

#print out the rss file
print(rss_output)