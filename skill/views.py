from django.shortcuts import render, redirect
from django.contrib import messages
from crud.models import crudUser
from django.urls import reverse


def home(request):
    return render(request, "index.html")


def saveuserdata(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if not name or not email or not password:
            messages.error(request, "☹️ Please Fill All fields!")
            return redirect('home')
        c = crudUser(name=name, email=email, password=password)
        c.save()
        messages.success(request, "🎉 Data saved successfully")
        return redirect('home')
    else:
        return redirect('home')

def delete(request, slug):
    c = crudUser.objects.get(slug=slug)
    c.delete()
    messages.success(request, '🎉 Record Deleted!')
    return redirect('home')
    
def reset(request):
    c = crudUser.objects.all().delete()
    messages.success(request, '🎉 All Records Deleted!')
    return redirect('home')



def edit(request, slug):
    user = crudUser.objects.get(slug=slug)
    response = render(request, 'index.html', {'editdata': user})
    user.delete()
    return response
