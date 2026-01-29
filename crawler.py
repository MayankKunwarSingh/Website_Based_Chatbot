import requests
from bs4 import BeautifulSoup

def crawl_web(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; WebsiteChatbot/1.0)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise ValueError("Invalid or unreachable URL")

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["header", "footer", "nav", "aside", "script", "style"]):
        tag.decompose()

    title = soup.title.string.strip() if soup.title else ""

    texts = []
    for tag in soup.find_all(["p", "li", "h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if len(text) > 40:
            texts.append(text)

    if not texts:
        raise ValueError("No meaningful HTML content found")

    unique_text = "\n".join(dict.fromkeys(texts))
    return title, unique_text
