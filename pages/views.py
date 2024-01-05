from django.shortcuts import render, redirect

from pages.forms import ContactModelForm
from pages.models import HomeModel, AboutModel, ProductsModel


def home_page_view(request):
    home = HomeModel.objects.all()
    about = AboutModel.objects.all()
    product = ProductsModel.objects.all()
    context = {
        "home": home,
        "product": product,
        "about": about,
    }
    return render(request, template_name='home.html', context=context)


def contact_page_view(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pages:contact")
    else:
        return render(request, template_name="home.html")

