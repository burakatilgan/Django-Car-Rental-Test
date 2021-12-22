from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from car.models import Car, Category, Images, Comment
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage, UserProfile, FAQ


def index(request):
    setting = Setting.objects.get(pk=1)
    slider = Car.objects.all()[:4]
    category = Category.objects.all()
    daycars = Car.objects.all().order_by('?')[:3]
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'slider': slider,
               'daycars': daycars,
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'category': category, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslarimiz(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'category': category, 'page': 'referanslarimiz'}
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "mesajınız gönderildi")
            return HttpResponseRedirect('/iletisim')

    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'category': category, 'form': form}
    return render(request, 'iletisim.html', context)


def category_cars(request, id, slug):
    category = Category.objects.all()
    cars = Car.objects.filter(category_id=id)
    categorydata = Category.objects.get(pk=id)
    context = {'cars': cars,
               'category': category,
               'categorydata': categorydata,
               }
    return render(request, 'cars.html', context)


def car_detail(request, id, slug):
    category = Category.objects.all()
    car = Car.objects.get(pk=id)
    images = Images.objects.filter(car_id=id),
    comments = Comment.objects.filter(car_id=id, status='True')
    context = {
        'category': category,
        'car': car,
        'images': images,
        'comments': comments
    }
    return render(request, 'car_detail.html', context)


def content_detail(request, id, slug):
    category = Category.objects.all()
    car = Car.objects.filter(category_id=id)
    link = '/car/' + str(car[0].id) + '/' + car[0].slug
    return HttpResponse(link)


def car_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            cars = Car.objects.filter(title__icontains=query)
            context = {
                'cars': cars,
                'category': category,
            }
            return render(request, 'car_search.html', context)

    return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Girişiniz başarısız oldu")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "/images/users/user.png"
            data.save()
            messages.success(request, 'kullanıcı oluşturuldu')
            return HttpResponseRedirect("/")



    form = SignUpForm()
    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'signup.html', context)


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.all().order_by('id')
    context ={
        'category': category,
        'faq': faq
    }
    return render(request, 'faq.html', context)