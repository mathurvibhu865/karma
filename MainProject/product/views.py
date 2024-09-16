from django.shortcuts import render
from.models import Product,Category

# Create your views here.
def products(request):
    data=Product.objects.all()
    cat=Category.objects.all()
    context={
        'products':data
    }
    return render(request, 'product/products_list.html', context)


