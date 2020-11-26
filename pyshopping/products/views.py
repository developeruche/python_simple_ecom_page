try:
    from django.http import HttpResponse
    from django.shortcuts import render
    from .models import Product
except Exception as e:
    error = f"Importation error has occored: {e}"
    print(error)


# View function


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {
        "products": products
    })


def new_products(request):
    return HttpResponse("This is the new product page")
