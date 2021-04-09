from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

# Welcome page
def welcome(request):
	return render(request, 'allotment/home.html')

# Show Hostel Info
def show_hostel_info(request):
	return render(request, 'allotment/hostel_info.html')