from django.shortcuts import render, redirect
from .models import User, UserManager, Quote
from django.contrib import messages
import re
import bcrypt


# Create your views here.
def index(request):
    return render(request, 'log_reg_app/log_reg.html')


def register(request):
    errors = User.objects.register(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        the_user = User.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email'],
            password=pw)
        request.session['user_id'] = the_user.id
        return redirect('/home')


def login(request):
    errors = User.objects.login(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        current_user = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(),
                          current_user.password.encode()):
            pass
        else:
            return redirect('/')
        request.session['user_id'] = current_user.id
        return redirect('/home')

def home(request):
    context = {
        'all_quotes': Quote.objects.all(),
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'log_reg_app/index.html', context)

def add_quote(request):
    errors = Quote.objects.add_quote(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/home')
    else:
        current_user = User.objects.get(id=request.session['user_id'])
        Quote.objects.create(author=request.POST['author'], quote=request.POST['quote'], users=current_user)
    return redirect('/home')

def like(request):
    current_quote = Quote.objects.get(id=request.POST['quote_id'])
    current_user = User.objects.get(id=request.session['user_id'])
    print('jell')
    if current_quote.user_liked.filter(id=current_user.id):
        return redirect('/home')
    else:
        current_quote.likes += 1
        current_quote.user_liked.add(current_user)
        current_quote.save()
    return redirect('/home')

def delete(request):
    this_quote = Quote.objects.get(id=request.POST['quote_id'])
    this_quote.delete()
    return redirect('/home')

def edit(request):
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        'current_user': current_user
    }
    return render(request, 'log_reg_app/edit.html', context)

def update(request):
    current_user = User.objects.get(id=request.session['user_id'])
    errors = User.objects.update(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit')
    else:
        current_user.first_name = request.POST['fname']
        current_user.last_name = request.POST['lname']
        current_user.email = request.POST['email']
        current_user.save()
        return redirect('/home')
    return redirect('/home')

def user(request):
    this_user   = User.objects.get(id=request.POST['this_id'])
    user_quotes = Quote.objects.filter(users=this_user)
    print(user_quotes)
    context = {
        'user': this_user,
        'user_quotes': user_quotes
    }
    return render(request, 'log_reg_app/user_page.html', context)

def logout(request):
    del request.session['user_id']
    return redirect('/')