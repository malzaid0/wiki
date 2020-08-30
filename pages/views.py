from django.shortcuts import render
from .models import Page

def List(request):
    context = {
        "pages": Page.objects.all()
    }
    return render(request, "list.html", context)


def Detail(request, page_id):
    context = {
        "page": Page.objects.get(id=page_id)
    }
    return render(request, "detail.html", context)