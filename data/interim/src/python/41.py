from django.core.paginator import Paginator
from django.shortcuts import render

def get_more_movies(request):
    page_number = int(request.GET.get("page", 1))
    movies_per_page = NUMBER_MOVIES_PER_PAGE

    movies = Movie.objects.all()
    paginator = Paginator(movies, movies_per_page)

    page = paginator.get_page(page_number)
    movies = page.object_list

    context = {
        'movies': movies,
        'next_page': page_number + 1 if page.has_next() else None,
    }
    return render(request, 'movies/_movies.html', context)
