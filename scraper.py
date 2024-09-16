import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote
from email_sender import send_email



def get_google_news(keyword, num_stories=3):
    base_url = "https://news.google.com/rss/search?"
    params = f"q={quote(keyword)}+when:7d&hl=en-US&gl=US&ceid=US:en&lr=lang_en"
    url = base_url + params
    
    print(f"Fetching RSS feed: {url}")  # Debug print
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return []

    root = ET.fromstring(response.content)
    
    unique_stories = []
    for item in root.findall('.//item'):
        title = item.find('title').text
        link = item.find('link').text
        
        if not any(story['title'] == title for story in unique_stories):
            unique_stories.append({'keyword': keyword, 'title': title, 'link': link})
            print(f"Added story: {title[:30]}...")  # Debug print
            
            if len(unique_stories) == num_stories:
                break
    
    print(f"Collected {len(unique_stories)} unique stories for '{keyword}'")  # Debug print
    return unique_stories