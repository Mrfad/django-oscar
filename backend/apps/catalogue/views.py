from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from oscar.apps.search.views import CatalogueView as CustomCatalogueView
from oscar.apps.search.views import ProductCategoryView as CustomProductCategoryView
from oscar.apps.partner.strategy import Selector  # To get the price strategy

class CatalogueView(CustomCatalogueView):
    template_name = 'oscar/catalogue/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # Add all products to the context
        products = Product.objects.all()
        context["products"] = products

        # Add price info using Oscar's pricing strategy
        strategy = Selector().strategy()
        for product in products:
            product.price = strategy.fetch_for_product(product).price

        return context


class ProductCategoryView(CustomProductCategoryView):
    template_name = 'oscar/catalogue/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get products in the selected category
        products = self.category.products.all()
        context["products"] = products

        # Add price info using Oscar's pricing strategy
        strategy = Selector().strategy()
        for product in products:
            product.price = strategy.fetch_for_product(product).price

        return context



# def home(request):
#     products = Product.objects.all()
#     context = {'products':products}
#     return render(request, 'oscar/catalogue/home.html', context)

# def store(request, category_slug=None):
#     categories = None
#     product = None
#     if category_slug != None:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = Product.objects.filter(categories=category, is_available=True)
#         product_count = products.count()
#     else:
#         products = Product.objects.filter(is_available=True)
#         product_count = products.count()
#     context ={
#         'products': products,
#         'product_count': product_count,  
#         }

#     return render(request, 'oscar/catalogue/store.html', context )
