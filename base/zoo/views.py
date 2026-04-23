from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Animals

def index(request):
    animals = Animals.objects.all()
    return render(request, 'animals.html', {'animals': animals})

def get_animal(request, animal_id):
    try:
        animal = Animals.objects.get(pk=animal_id)
    except Animals.DoesNotExist:
        raise Http404("Обьект не найден")
    return render(request, 'single_animal.html', {'animal': animal})


def get_animals_with_good_and_excellent_health(request):
    animals = Animals.objects.all().filter(health__in=['Хорошее', 'Отличное'])
    return render(request, 'animals.html', {'animals': animals})