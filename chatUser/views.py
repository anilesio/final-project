from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from accounts.decorators import *
from .models import *
from .forms import *
from django.db.models import Q
from django.db.models import Sum
from estudante.models import *
from professor.models import *

# Create your views here.
@login_required(login_url='accounts:user_login')
def chatUser(request):
    # estadoMensagem = Chat.objects.all().filter(estadoVisto=False).count()
    objecto = Chat.objects.all()
    form = ChatForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            f1 = form.save(commit=False)
            f1.transmissor = request.user
            f1.receptor = User.objects.get(username = 'admin')
            f1.save()
            return HttpResponseRedirect(reverse('chatUser:chat-user'))

    estudante = Estudante.objects.get(user = request.user)
    mensagens = Chat.objects.all()
    mensagens.update(estadoVisto=True)
    args = {
        'mensagens':mensagens,
        'estudante':estudante,
        'form':form,
        'objecto':objecto
    }
    return render(request, 'chat/chat.html', args)