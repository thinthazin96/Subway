import json
from xml.etree.ElementTree import Element, SubElement, tostring

def json_to_rss(json_data, title, link, description):
    rss = Element('rss', version='2.0')
    channel = SubElement(rss, 'channel')
    SubElement(channel, 'title').text = title
    SubElement(channel, 'link').text = link
    SubElement(channel, 'description').text = description

    for item_data in json_data:
        item = SubElement(channel, 'item')
        SubElement(item, 'title').text = item_data.get('title')
        SubElement(item, 'link').text = item_data.get('link')
        SubElement(item, 'description').text = item_data.get('description')
        # Add other RSS elements as needed (pubDate, guid, etc.)

    return tostring(rss, encoding='utf-8', xml_declaration=True).decode('utf-8')

# Sample JSON data
json_input = """
[
    {"title": "Article 1", "link": "https://example.com/article1", "description": "Description for article 1"},
    {"title": "Article 2", "link": "https://example.com/article2", "description": "Description for article 2"}
]
"""

data = json.loads(json_input)
rss_output = json_to_rss(data, "My Awesome Feed", "https://example.com", "A feed of my articles")
print(rss_output)