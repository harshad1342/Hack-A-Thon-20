from django.shortcuts import render
from .models import Book
from django.http import Http404


# Create your views here.
def index(request):
    Book_dets = Book.objects.all()
    return render(request, "index.html", {'Book_dets': Book_dets})


def about(request):
    return render(request, "about.html")


def book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book not found")
    context = {
        "Book_det": book
    }
    return render(request, "books.html", context)

def donate(request):
    return render(request, "donate.html")