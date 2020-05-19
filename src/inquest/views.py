from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from blog.models import BlogPost


def home_page(request):
    qs = BlogPost.objects.recent()[:4]
    context = {'latest': qs}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {'title': "About Page"})


def contact_page(request):
    return render(request, "contact.html", {'title': "Contact Page"})


def example_page(request):
    # This is a more standard way
    context = {'title': 'Example Page'}
    template_name = 'example.html'  # This can be any file type
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
