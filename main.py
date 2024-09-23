from scraper import get_google_news, get_article_content
from email_sender import send_email
from llama_sentiment import llama_summary
import time

keywords = [] #Input string keywords
top_stories = []

for keyword in keywords:
    stories = get_google_news(keyword)
    top_stories.extend(stories)
    print(f"After processing '{keyword}', top_stories has {len(top_stories)} items")

for story in top_stories:
    print(f"Keyword: {story['keyword']}")
    print(f"Title: {story['title']}")
    print(f"Link: {story['link']}")
    

email_content = "<html><body>"
for story in top_stories:
    email_content += f"<h2>{story['keyword']}</h2>"
    email_content += f"<h3><a href='{story['link']}'>{story['title']}</a></h3>"
    email_content += f"<div class='article-content'>{llama_summary(text=get_article_content(story['link']))}</div>"
    email_content += "</body></html>"
    time.sleep(3)

sender = "sender@gmail.com"  # Replace with your Gmail address
to = "recipient@gmail.com"  # Replace with recipient's email address
subject = "Today's Top News Stories"
send_email(sender, to, subject, email_content)
