from django.shortcuts import render_to_response

from calvinball.forms import ComicSearchForm


def comics(request):
    form = ComicSearchForm(request.GET)
    comics = form.search()
    return render_to_response('templates/search/search.html', {'comics': comics})
