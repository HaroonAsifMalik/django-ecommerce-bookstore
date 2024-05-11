# this is the file for the data which is avaliable on all the pages
from .models import Category


def categories(request):
    return {
        'categories' : Category.objects.all()
    }
