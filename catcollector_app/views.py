from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat

# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]
# Create your views here.

def home(request):
    return render(request, 'cats/home.html')

def about(request):
    return render(request, 'cats/about.html')

def cats_index(request):
  cats = Cat.objects.all()
  # We pass data to a template very much like we did in Express!
  return render(request, 'cats/index.html', {
    'cats': cats
  })

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat })

class CatCreate(CreateView):
  model = Cat
  fields = '__all__'

class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'

  



