from django.shortcuts import render
from django.http import JsonResponse
import requests
import os
import certifi
from bs4 import BeautifulSoup
import time

os.environ['SSL_CERT_FILE'] = certifi.where()

BASE_URL = "https://www.genealogy.math.ndsu.nodak.edu/id.php?id={}"

def get_advisors(mathgen_id):
    url = BASE_URL.format(mathgen_id)
    try:
        response = requests.get(url, verify=False)
    except requests.exceptions.SSLError:
        return []

    if response.status_code != 200:
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
    return advisors

def build_ancestor_tree(mathgen_id, depth):
    if depth == 0:
        return {}

    advisors = get_advisors(mathgen_id)
    if not advisors:
        return {}

    tree = {}
    for advisor_id, advisor_name in advisors:
        subtree = build_ancestor_tree(advisor_id, depth - 1)
        tree[advisor_name + f" [ID {advisor_id}]"] = subtree
        time.sleep(0.2)
    return tree

def index(request):
    return render(request, 'index.html')

def get_tree(request):
    mathgen_id = request.GET.get('id')
    depth = int(request.GET.get('depth', 1))
    tree = build_ancestor_tree(mathgen_id, depth)
    return JsonResponse({'tree': tree})