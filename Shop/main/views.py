from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product  # Faqat models.py ichidan model import qilinadi
from .forms import CommentForm

class IndexView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    comments = product.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = CommentForm()

    return render(request, 'main/product_detail.html', {'product': product, 'comments': comments, 'form': form})





from .models import Product, Order, OrderProduct
from .forms import OrderForm

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            cart = request.session.get('cart', {})
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                OrderProduct.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.final_price()
                )

            request.session['cart'] = {}
            return redirect('order_success')
    else:
        form = OrderForm()

    return render(request, 'main/create_order.html', {'form': form})
