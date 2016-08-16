from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from .forms import MessageForm


def Index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
    form = MessageForm()
    latest_message = Message.objects.order_by('-create_time')[:5]
    return render(request, 'msgbd/index.html', {'latest_message': latest_message, 'form': form})
