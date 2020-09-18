from django.shortcuts import render

from django.http import HttpResponse

import random
# Create your views here.

def home(requset):
 return  render(requset,'generator/html/home.html')

def password(requset):
 pas=''
 Ch=list('abcdefghijklmnopqrstvwxyz')
 if requset.GET.get('uppercase'):
     Ch.extend(list('ABCDEFGHIJKLMNOPQRSTVWXYZ'))
 if requset.GET.get('number'):
     Ch.extend(list('0123456789'))
 if requset.GET.get('Special'):
     Ch.extend(list('+*/-.!@#$%^&*()_|\?'))
 length=int(requset.GET.get('length',12))
 for i in range(length):
     pas+=random.choice(Ch)
 return render(requset,'generator/html/password.html',{'password':pas})