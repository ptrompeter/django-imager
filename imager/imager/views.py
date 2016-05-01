# _*_ coding: utf-8 _*_
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

#NOTES FROM CLASS:

# def home_page(request, *args, **kwargs):
#     kwargstring = argstring = ""
#     if args:
#         argstring = "args: {}".format(", ".join(args))
#     if kwargs:
#         kwargstring = "kwargs: \n".format(
#             "\t{}: {}\n".format(key, val) for key, val in kwargs.items()
#             )
#     body = """
# home page view was called with:
#     {}
#     {}
#     """.format(argstring, kwargstring)
#     return HttpResponse(body)

# def home_page(request, *args, **kwargs):
#     template = loader.get_template('home.html')
#     foo = 'garbanzo beans'
#     body = template.render({'foo': foo})
#     return HttpResponse(body)

# def home_page(request, *args, **kwargs):
#     foo = 'garbanzo beans'
#     return render(request, 'home.html', context={foo})

class ClassView(TemplateView):
    template_name = 'home.html'

    # def get_context_data(self, id=1):
    #     foo = 'garbanzo beans'
    #     return {'foo': foo}

    def get_context_data(self):
        """Pass image to the homepage"""
        try:
            img = Photo.objects.all().order_by("?")[0]
            # maybe Photo.objects.filter(published = 'pub')[:200].order_by("?")[0]
        except IndexError:
            img = None
        return {'img': img}

def logout_view(request):
    logout(request)
    return redirect('homepage')

def home_page(request):
    request

