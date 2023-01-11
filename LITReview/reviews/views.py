from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def cover_upload(request):
    form = forms.PhotoForm()
    if request.method =='POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        cover = form.save(commit=False)
        cover.uploader = request.user
        cover.save()
        return redirect('home')
    return render(request, 'reviews/cover_upload.html', context={'form': form})


@login_required
def home(request):
    covers = models.Photo.objects.all()
    return render(request, 'reviews/home.html', context={'covers': covers})


@login_required
def home(request):
    # return HttpResponse('<h1>Bienvenue chez LITReview</h1>')
    return render(request, 'reviews/home.html')


def sign_up_page(request):
    return HttpResponse('<h1>Créer votre compte</h1>')


def flow_page(request):
    return HttpResponse('<h1>Flux</h1>')


def subscriptions_page(request):
    return HttpResponse('<h1>Souscriptions</h1>')


def tickets_page(request):
    return HttpResponse('<h1>Tickets</h1>')


def critic_create(request):
    return HttpResponse('<h1>Création critique</h1>')


def critic_response(request):
    return HttpResponse('<h1>Création critique en réponse</h1>')


def view_own_post(request):
    return HttpResponse('<h1>Voir vos posts</h1>')


def critic_modify(request):
    return HttpResponse('<h1>Modifier votre propre critique</h1>')


def ticket_modify(request):
    return HttpResponse('<h1>Modifier votre propre ticket</h1>')





