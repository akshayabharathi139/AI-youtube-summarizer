import re

def clean_description(desc):
    desc = re.sub(r'\n+', ' ', desc)
    return desc.strip()[:1000]  # Limit to 1000 chars
