from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(url):
    """
    Converte uma URL normal do YouTube em uma URL embutida para <iframe>.
    """
    regex = r"youtu(?:\.be|be\.com)/(?:.*v(?:/|=)|(?:.*/)?)([\w'-]+)"
    match = re.search(regex, url)
    if match:
        video_id = match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"
    return url  
