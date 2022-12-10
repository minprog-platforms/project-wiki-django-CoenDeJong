from django.shortcuts import render
import markdown2
from django import forms
from random import choice

from . import util

class Searchform(forms.Form):
    query = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Search Wiki"}))

class NewPage(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput({'placeholder': "Title"}))

def index(request):
    searchform = Searchform()

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "searchform": searchform
    })

def entry(request, title):
    """ Redirect to title page if it exists """
    searchform = Searchform()

    if util.get_entry(title) == None:
        return render(request, "encyclopedia/not_found.html", {
            "searchform" : Searchform()
        })

    return render(request, "encyclopedia/entry.html", {
        "content": markdown2.markdown(util.get_entry(title)),
        "title": title,
        "searchform" : searchform
    })

def search(request):
    """ Loads a page for what is searched """
    searchform = Searchform()
    searchlist = []

    if request.method == "POST":
        searchform = Searchform(request.POST)

    if searchform.is_valid():
        query = searchform.cleaned_data["query"]

        if util.get_entry(query):
            return render(request, "encyclopedia/entry.html", {
                "content": markdown2.markdown(util.get_entry(query)),
                "title": query,
                "searchform" : searchform
            })

        for entry in util.list_entries():
            if query.lower() in entry.lower():
                searchlist.append(entry)

        return render(request, "encyclopedia/searchresults.html", {
            "searchlist": searchlist,
            "query": query,
            "searchform": searchform
            })

def create(request):
    """ Allows the user to create a wiki page """
    searchform = Searchform()
    createform = NewPage()

    if request.method == "POST":
        createform = NewPage(request.POST)
        content = request.POST["content"]

        if createform.is_valid():
            title = createform.cleaned_data['title']

            if title in util.list_entries():
                return render(request, "encyclopedia/exists.html", {
                    "searchform": searchform
                    })

            util.save_entry(title, content)
            return entry(request, title)
    else:
        form = NewPage()
        return render(request, "encyclopedia/create.html", {
            "searchform": searchform,
            "createform": createform
            })

def random(request):
    """ Brings user to a random wiki page """
    titles = util.list_entries()
    title = choice(titles)
    return entry(request, title)
