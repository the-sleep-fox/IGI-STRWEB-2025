from django.shortcuts import render

#getting a response
def index(request):
    data = {
        'title': "Main Page!",
        'values': ['some', 'hello', '123']
    }
    return render(request, 'main/index.html', data)
def about(request):
    return render(request, 'main/about.html')