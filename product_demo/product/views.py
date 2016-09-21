# coding: utf-8
from django.shortcuts import render,redirect
from product.models import Category,Keyword,Product
from django.core.paginator import Paginator
# Create your views here.

def add(request):
    if request.method == 'POST':
        post = request.POST
        product = Product.objects.create(
            name = post.get('product_name'),
            spec = post.get('product_spec'),
            cate_id = post.get('product_category'),
            stock = post.get('product_stock'),
            price = post.get('product_price'),
            desc = post.get('product_desc'))

        keylist = post.getlist('product_key')
        for key_id in keylist:
                product.key.add(key_id)
        return redirect('list')

    categorys = Category.objects.all()
    keywords = Keyword.objects.all()
    return render(request,'product/add.html',{'categorys':categorys,'keywords':keywords})

def update(request,id):

    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        post = request.POST
        product.name = post.get('product_name')
        product.spec = post.get('product_spec')
        product.cate_id = post.get('product_category')
        product.stock = post.get('product_stock')
        product.price = post.get('product_price')
        product.desc = post.get('product_desc')
        keylist = post.getlist('product_key')
        for key_id in keylist:
            key = Keyword.objects.get(pk=key_id)
            if key not in product.key.all():
                product.key.add(key_id)
        for key in product.key.all():
            if str(key.id) not in keylist:
                product.key.remove(key)
        product.save()

        return redirect('list')
    product = Product.objects.get(pk=id)
    categorys = Category.objects.all()
    keywords = Keyword.objects.all()
    return render(request, 'product/update.html', locals())

def delete(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('list')

def list(request):
    products = Product.objects.order_by('-id')
    paginator = Paginator(products,3)
    try:
        page = int(request.GET.get('page'))
        products = paginator.page(page)
    except:
        products = paginator.page(1)
    return render(request,'product/list.html',locals())