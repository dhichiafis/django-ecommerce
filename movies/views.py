from django.shortcuts import render,redirect
from .utils import calculate_cart_total
# Create your views here.
from .models import Movie,Item,Order


def movies_list(request):
    search_term=request.GET.get('search')
    if search_term:
        movies=Movie.objects.filter(title__icontains=search_term)
    else:
        movies=Movie.objects.all()
        
        
    context={'movies':movies}
    return render(request,'movies/movies_list.html',context)


def movie_detail(request,id):
    movie=Movie.objects.get(id=id)
    context={'movie':movie}
    return render(request,'movies/movie_detail.html',context)

def add_to_cart(request,id):
    movie=Movie.objects.get(id=id)
    cart=request.session.get('cart',{})
    cart[id]=request.POST['quantity']
    request.session['cart']=cart
    return redirect('movies_list')

def cart_detail(request):
    cart_total=0
    movies_in_cart=[]
    cart=request.session.get('cart',{})
    movie_ids=list(cart.keys())
    if(movie_ids!=[]):
        movies_in_cart=Movie.objects.filter(id__in=movie_ids)
        cart_total=calculate_cart_total(cart,movies_in_cart=movies_in_cart)
        
    context={'cart_total':cart_total,'movies_in_cart':movies_in_cart}
    return render(request,'movies/cart_detail.html',context)


def clear_cart(request):
    request.session['cart']={}
    return redirect('movies_list')


def purchase(request):
    cart=request.session.get('cart',{})
    movies_in_cart=[]
    cart_total=0
    movies_id=list(cart.keys())
    if(movies_id==[]):
        return redirect('cart_detail')
    
    movies_in_cart=Movie.objects.filter(id__in=movies_id)
    cart_total=calculate_cart_total(cart,movies_in_cart=movies_in_cart)
    order=Order()
    order.total=cart_total
    order.save()
    for movies in movies_in_cart:
        item=Item()
        item.movie=movies 
        item.price=movies.price
        item.order=order
        item.save()
    request.session['cart']={}
    return render(request,'movies/purchase_complete.html')