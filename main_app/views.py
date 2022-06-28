from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import MyProject
from .forms import PostForm
from telegram import Bot



class SenderMessages:

    TELEGRAM_TOKEN = '5320918569:AAHjUUYGCpY7P6cZ8iDvtKJu7b8_lC0OJn8'
    CHAT_ID = '1053634002'
    bot = Bot(token=TELEGRAM_TOKEN)

    def sended_message(message):
        send = SenderMessages
        send.bot.send_message(chat_id=send.CHAT_ID, text=message)


def index(request):

    SenderMessages.sended_message('кто-то открыл страницу')
    form = PostForm()

    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            form.save()
            SenderMessages.sended_message(text)
            ok = True
            return render(request, 'index.html', {'ok':ok})

    
    ok = False
    return render(request, "index.html", {'form': form, 'ok': ok})



