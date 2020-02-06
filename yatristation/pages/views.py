from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def about(request):
	return render(request, 'pages/about.html')


def destination(request):
	return render(request, 'pages/destination.html')


def destination_details(request):
	return render(request, 'pages/destination_details.html')


def blog(request):
	return render(request, 'pages/blog.html')


def contacts(request):
	return render(request, 'pages/contacts.html')


def single_blog(request):
	return render(request, 'pages/single_blog.html')