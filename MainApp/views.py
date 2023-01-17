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
    res = f"""<a href="/countries-list">К списку стран</a>
        <h1>{elem}</h1>
        <ul>"""
    for item in items:
        if item["country"][0] == elem:
            res += f"<li>{item['country']}</li>"
    res += "</ul>"
    return HttpResponse(res)

def languages_list(request):
    lang_list = []
    for item in items:
        for lang in item["languages"]:
            if lang not in lang_list:
                lang_list.append(lang)
    res = f"""<a href="/">На главную</a>
        <h1>Список языков мира</h1>
        <ol>"""
    for i in sorted(lang_list):
        res += f"<a href=/lang-use/{i}><li>{i}</li></a>"
    res += "</ol>"
    return HttpResponse(res)

def lang_use(request, lang):
    res = f"""<a href=/languages-list>К списку языков</a>
        <h1>Страны говорящие на {lang}</h1>
        <ul>
        """
    for item in items:
        if lang in item["languages"]:
            res += f"<li>{item['country']}</li>"
    res += "</ul>"
    return HttpResponse(res)