# encoding=utf8
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views import generic
from sysApp.models import MyUser, Product, Material
from sysApp.forms import UserForm, ProductForm, MaterialForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def my_view(request):
    if request.user.is_authenticated():
        output = "welcome back "
        output += str(request.user.username)
    else:
        output = "welcome"
    
    return HttpResponse(output)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        content = {}
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/test')
            else:
                content['info'] = u"帐号或密码错误"
                content['form'] = AuthenticationForm()
                return render(request, 'login.html', content)
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form}, RequestContext(request))


def logout_view(request):
    logout(request)
    return redirect('/')


def create_user_view(request):
    if request.method == 'POST':
        data = request.POST
        form = UserForm(data)
        if form.is_valid():
            form.clean_username()
            form.clean()
            form.save()
            return HttpResponseRedirect('login')
        else:
            return render(request, 'user_create.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'user_create.html', {'form': form})


class ProductIndexView(generic.ListView):
    model = Product
    template_name = "product_index.html"
    context_object_name = "product_list"


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def create_product_view(request):
    if request.user.has_perm('sysApp.add_product'):
        if request.method == 'POST':
            data = request.POST
            form = ProductForm(data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('product')
            else:
                return render(request, 'product_create.html', {'form':form})
        else:
            form = ProductForm()
            content = {
                "form": form
            }
            return render(request, 'product_create.html', content)
    else:
        return redirect('login')


# TODO: 做材料商的CRUD， 参考product