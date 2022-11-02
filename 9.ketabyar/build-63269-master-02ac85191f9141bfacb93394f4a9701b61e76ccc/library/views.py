from django.http import HttpResponse

from .models import Book
from .render import render_to_readable_output


def book_list(request):
    min_price = request.GET.get('min_price') or 0 #ya get('min_price', 0)
    max_price = request.GET.get('max_price') or 100000
    author = request.GET.get('author', [])
    name = request.GET.get('name', [])

    all_books = Book.objects.filter(
    price__lte=max_price,
    price__gte=min_price,    
    )
    if author:
        all_books = Book.objects.filter(author__icontains=author)
    if name:
        all_books = Book.objects.filter(name__icontains=name)
    #ya
    #    all_books = Book.objects.filter(name__icontains = name, author__icontains = author, price__gte = min_price, price__lte = max_price)

    rendered_string = render_to_readable_output(all_books)
    return HttpResponse(rendered_string)
