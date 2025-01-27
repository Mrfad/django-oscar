# from django.shortcuts import render, get_object_or_404
# from oscar.apps.catalogue.models import Product
# from .models import CustomCategory, CustomProduct

# def home(request):
#     products = CustomProduct.objects.all()

#     context = {'products': products}
#     return render(request, 'product/home.html', context)

# def store(request, category_slug=None):
#     categories = None
#     products = None
#     if category_slug != None:
#         category = get_object_or_404(CustomCategory, slug=category_slug)
#         products = CustomProduct.objects.filter(category=category, is_available=True)
#         product_count = products.count()
#     else:
#         products = CustomProduct.objects.filter(is_available=True)
#         product_count = products.count()
     
#     context = {'products': products,
#                'product_count': product_count,}
#     return render(request, 'product/store.html', context)