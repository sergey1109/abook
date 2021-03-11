from django.shortcuts import render, redirect

from .forms import UserForm
from .models import Users


# Create your views here.

def index(request):
    all_users = Users.objects.all()
    search_input = request.GET.get('search_area')
    if search_input:
        all_users = Users.objects.filter(name__icontains=search_input, surname__icontains=search_input)
    else:
        all_users = Users.objects.all()
        search_input = ""

    return render(request, 'index.html', {'all_users': all_users, 'search_input': search_input})


def AddContact(request):
    user_form = {}
    user_form['form'] = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'new.html', user_form)

    elif request.method == 'GET':
        return render(request, 'new.html', user_form)


def ContactProfile(request, pk):
    contact = Users.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': contact})


def EditContact(request, pk):
    contact = Users.objects.get(id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            contact.name = request.POST['name']
            contact.surname = request.POST['surname']
            contact.address_country = request.POST['address_country']
            contact.address_sity = request.POST['address_sity']
            contact.address_street = request.POST['address_street']
            contact.url = request.POST['url']
            contact.phone_number = request.POST['phone_number']
            contact.img_user = request.POST['img_user']
            contact.save()
        return redirect('/profile/' + str(contact.id))
    return render(request, 'edit.html', {'contact': contact})


def DeleteContact(request, pk):
    contact = Users.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})
