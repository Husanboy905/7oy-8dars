from  django.views.generic import ListView
from .models import Product


class IndexView(ListView):
    model = Product
    template_name = "index.html"



def home(request):
    products = Product.objects.all()  # 🔹
    return render(request, 'index.html', {'products': products})




from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import CommentForm

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

    return render(request, 'mein/product_detail.html', {'product': product, 'comments': comments, 'form': form})
