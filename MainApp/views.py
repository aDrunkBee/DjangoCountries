from django.shortcuts import render
from django.http import HttpResponse
from countries import items as items

# Create your views here.

def home(request):
    context = {}
    return render(request, "index.html", context)

def countries_list(request):
    context = {"items": items}
    return render(request, "countries_list.html", context)

def country_item(request, country):
    for item in items:
        if item["country"] == country:
            context = {"item": item}
            return render(request, "country_item.html", context)

def country_alpha(request, elem):
    cnt_list=[]
    for item in items:
        if item["country"][0] == elem:
            cnt_list.append(item)
    context = {"items": cnt_list}
    return render(request, "country_alpha.html", context)


def languages_list(request):
    lang_list = []
    for item in items:
        for lang in item["languages"]:
            if lang not in lang_list:
                lang_list.append(lang)
    context = {"items": lang_list}
    return render(request, "language_list.html", context)

def lang_use(request, lang):
    cnt_list=[]
    for item in items:
        if lang in item["languages"]:
            cnt_list.append(item)
    context = {"items": cnt_list}
    return render(request, "lang_use.html", context)