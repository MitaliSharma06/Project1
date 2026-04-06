from urllib.request import Request, urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
import socket

# timeout set
socket.setdefaulttimeout(10)

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    self.links.append(attr[1])

def open_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        req = Request(url, headers=headers)
        return urlopen(req)
    except Exception as e:
        print("Error:", e)
        return None

def get_links(url):
    response = open_url(url)
    if not response:
        return []

    html = response.read().decode("utf-8", errors="ignore")

    parser = LinkParser()
    parser.feed(html)

    return [urljoin(url, link) for link in parser.links]

def main():
    target = input("Enter URL: ")

    print("\n[+] Getting links...")
    links = get_links(target)

    print(f"[+] Found {len(links)} links")

    print("\n[✔] Scan Complete")

if __name__ == "__main__":
    main()
