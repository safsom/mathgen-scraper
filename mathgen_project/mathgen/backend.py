
import requests
import os
import certifi
from bs4 import BeautifulSoup
import urllib3
import threading

os.environ['SSL_CERT_FILE'] = certifi.where()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://www.genealogy.math.ndsu.nodak.edu/id.php?id={}"
cache = {}
cache_lock = threading.Lock()

def get_advisors(mathgen_id):
    with cache_lock:
        if mathgen_id in cache:
            return cache[mathgen_id]

    url = BASE_URL.format(mathgen_id)
    try:
        response = requests.get(url, verify=False)
    except requests.exceptions.SSLError:
        return []

    if response.status_code != 200:
        with cache_lock:
            cache[mathgen_id] = []
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    advisor_tags = soup.select("p[style*='line-height'] a[href*='id.php?id=']")

    advisors = []
    for a_tag in advisor_tags:
        name = a_tag.text.strip()
        href = a_tag['href']
        if "id=" in href:
            advisor_id = href.split("id=")[-1]
            advisors.append((advisor_id, name))

    with cache_lock:
        cache[mathgen_id] = advisors
    return advisors

def build_ancestor_tree(mathgen_id, depth, current_depth=1):
    if depth == 0:
        return {}

    advisors = get_advisors(mathgen_id)
    if not advisors:
        return {}

    tree = {}
    for advisor_id, advisor_name in advisors:
        subtree = build_ancestor_tree(advisor_id, depth - 1, current_depth + 1)
        tree[advisor_name + f" [ID {advisor_id}]"] = subtree
    return tree
