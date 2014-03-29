
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from DemoApp.models import Cuisine,Recipe

from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):

    # Cuisine.objects.filter(id=2).delete()
    # cuisines = Cuisine.objects.all()
    # cuisines= Cuisine.book_set.all().order_by('-pub_date')[:5]
    cuisines=Cuisine.objects.all().order_by('-id')[:6]

    return render_to_response(
        'index.html',
        {'documents':cuisines},
        context_instance=RequestContext(request)
    )





def search(request):
    context = RequestContext(request)

    if request.method == 'POST':
        keyword = request.POST.get('searchtext')
        documents = Cuisine.objects.filter(name__contains=keyword)


    return render_to_response('food_list.html', {'documents': documents}, context)


# def food_list(request):
#     food =Food.objects.all()
#     return render_to_response('food_list.html', {'object_list': food}, context_instance = RequestContext(request))

def list(request):


    documents = Cuisine.objects.all()

    return render_to_response(
        'food_list.html',
        {'documents': documents},
        context_instance=RequestContext(request)

    )

def recipeDetails(request, num=0):

    documents = Recipe.objects.filter(cuisines=1)

    cuisinedetails=Cuisine.objects.get(id=num)

    ctx = RequestContext(request, {
        'documents': documents,
        'cuisinedetails': cuisinedetails,

    })
    return render_to_response('food_detail.html', context_instance=ctx)

def sign_up(request):
    return render_to_response(
        'register.html',
        context_instance=RequestContext(request)
    )

def login1(request):
    return render_to_response(
        'login.html',
        context_instance = RequestContext(request)
    )

def loginview(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_and_login(request, onsuccess='/', onfail='/account/login/'):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True


def sign_up_in(request):
    post = request.POST
    if not user_exists(post['email']):
        user = create_user(username=post['email'], email=post['email'], password=post['password'])
    	return auth_and_login(request)
    else:
    	return redirect("/account/login/")

@login_required(login_url='/account/login/')
def secured(request):
    return render_to_response("secure.html")

