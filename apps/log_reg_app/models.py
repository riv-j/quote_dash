from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = 'First name must be at least 2 characters long'
        if len(postData['lname']) < 2:
            errors['lname'] = 'Last name must be at least 2 characters long'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be in the correct format"
        if len(postData['password']) < 8:
            errors['password'] = 'Password must contain at least 1 uppercase letter, 1 lowecase, at least 1 digit, 1 special character, and a minimum of 8 characters'
        if postData['password'] != postData['cpassword']:
            errors['match'] = 'Passwords do not match'
        user_with_email = User.objects.filter(email=postData['email'])
        if len(user_with_email) > 0:
            errors['email'] = 'Email is already taken'
        return errors

    def login(self, postData):
        errors = {}
        if len(postData['email']) == 0:
            errors['email'] = 'Please enter an email'
        if len(postData['password']) == 0:
            errors['password'] = 'Please enter a password'
        user_with_email = User.objects.filter(email=postData['email'])
        if len(user_with_email) <= 0:
            errors['email'] = 'Email does not exist'
        return errors

    def update(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = 'First name must be at least 2 characters long'
        if len(postData['fname']) == 0:
            errors['fname'] = 'You must enter a first name'
        if len(postData['lname']) < 2:
            errors['lname'] = 'Last name must be at least 2 characters long'
        if len(postData['lname']) == 0:
            errors['lname'] = 'You must enter a last name'
        if len(postData['email']) == 0:
            errors['email'] = 'Please enter an email'
        user_with_email = User.objects.filter(email=postData['email'])
        if len(user_with_email) > 0:
            errors['email'] = 'Email is already taken'
        return errors


class User(models.Model):
    first_name      = models.CharField(max_length=45)
    last_name       = models.CharField(max_length=45)
    email           = models.CharField(max_length=45)
    password        = models.CharField(max_length=255)
    updated_at      = models.DateTimeField(auto_now=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    objects         = UserManager()

class QuoteManager(models.Manager):
    def add_quote(self, postData):
        errors = {}
        if len(postData['author']) < 3:
            errors['author'] = 'Author name must be at least 3 characters long'
        if len(postData['quote']) < 10:
            errors['quote'] = 'Quote must be at least 10 characters long'
        return errors

class Quote(models.Model):
    author          = models.CharField(max_length=55)
    quote           = models.TextField()
    likes           = models.IntegerField(default=0)
    user_liked      = models.ManyToManyField(User, related_name='num_likes')
    users           = models.ForeignKey(User, related_name='quotes')
    updated_at      = models.DateTimeField(auto_now=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    objects         = QuoteManager()