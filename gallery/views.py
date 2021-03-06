from django.shortcuts import render, get_object_or_404
from .models import Category, Art_Product
from cart.forms import CartAddProductForm

# Create your views here.
def art_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Art_Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'gallery/art/index.html', {'category': category, 'categories': categories, 'products': products})

def art_detail(request, id, slug):
    product = get_object_or_404(Art_Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'gallery/art/product.html', {'product': product, 'cart_product_form': cart_product_form})
