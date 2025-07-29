
from django.http import JsonResponse
from django.shortcuts import render
from .backend import build_ancestor_tree

def index(request):
    return render(request, "mathgen/index.html")

def get_tree(request):
    mathgen_id = request.GET.get("id")
    depth = int(request.GET.get("depth", 1))
    tree = build_ancestor_tree(mathgen_id, depth)
    return JsonResponse(tree)
