from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Idea, Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging
from .forms import IdeaForm, CommentForm
from django.shortcuts import get_object_or_404


def idea(request):
    ideas = Idea.objects.all()
    return render(request, 'home.html', {'myideas': ideas})


logger = logging.getLogger(__name__)


@login_required
def make_post(request):
    form = IdeaForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            logger.info("Formularz poprawny, tworzenie posta")
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            messages.success(request, "Post został pomyślnie utworzony!")
            return redirect('idea')
        else:
            logger.warning("Formularz nie przeszedł walidacji")
            messages.error(request, "Nie udało się stworzyć posta. Popraw błędy.")

    return render(request, 'create_idea.html', {'form': form, 'title': 'Create New Post'})


def chat_room(request, room_name):
    return render(request, 'chat_room.html', {'room_name': room_name})


def detail(request, idea_id):
    details = get_object_or_404(Idea, id=idea_id)
    return render(request, 'detail_view.html', {'idea': details})


def detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    comments = Comments.objects.filter(idea=idea)
    return render(request, 'detail_view.html', {'idea': idea, 'comments': comments})


@login_required
def make_comment(request):
    form = CommentForm(request.POST or None)
    context = {
        'form': form,
        'title': 'Create New Comment',
    }
    if request.method == "POST":
        if form.is_valid():
            logger.info("Formularz poprawny, dodawanie komentarza")
            new_comm = form.save(commit=False)
            new_comm.user = request.user
            new_comm.save()
            messages.success(request, "Komentarz został dodany")
            return redirect('idea')
        else:
            logger.warning("Formularz nie przeszedł walidacji")
            messages.error(request, "Nie udało się stworzyć komeentarza. Popraw błędy.")

    return render(request, 'create_idea.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Konto zostało utworzone! Możesz się teraz zalogować.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('idea')
