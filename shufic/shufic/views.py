from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth

def index(request):
    return render(request, "index.html")