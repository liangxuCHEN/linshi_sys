from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from sysApp.models import MyUser, Product, Material
from sysApp.forms import UserForm, ProductForm, MaterialForm

#django defaut listView
def my_view(request):
    if request.user.is_authenticated():
        output = "welcome back"
        output += str(request.user.id)
    else:
        output = "welcome"
    
    return HttpResponse(output)


def LoginView(request):
    """
    Log in view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        content = {}
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('test')
                else:
                    content = {}
                    form = TargetUserForm()
                    content['form'] = form
                    content['user'] = user
                    return render(request, 'target_user_create.html', content)
            else:
                content['info'] = "can not login in"
                return render(request, 'login.html', content)
    else:
        form = AuthenticationForm()
    return render_to_response('login.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def LogoutView(request):
    logout(request)
    return redirect('/')

def CreateUserView(request):
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

def productDetailView(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

#create the product
# has_perm(perm, obj=None):
#Returns True if the user has# the named permission. If obj is provided, the permission needs to be checked against a specific object instance.

#has_module_perms(app_label):
def createproductView(request):
    if request.user.is_authenticated():
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
            return render(request, 'product_create.html', content)
    else:
        return redirect('login')
