
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .service import get_ai_response
from .models import ChatMessage
from .forms import RegisterForm


@api_view(['POST'])
@login_required(login_url='/chatbot/login/')
def chat_with_ai(request):

    user_message = request.data.get('message')

    if not isinstance(user_message, str):

        return Response(
            {
                "error": "Message must be text."
            },
            status=400
        )

    user_message = user_message.strip()

    if not user_message:

        return Response(
            {
                "error": "Message cannot be empty."
            },
            status=400
        )

    if len(user_message) > 5000:

        return Response(
            {
                "error": "Message is too long. Please keep it under 5000 characters."
            },
            status=400
        )

    ai_reply = get_ai_response(user_message)

    ChatMessage.objects.create(
        user=request.user,
        user_message=user_message,
        ai_response=ai_reply
    )

    return Response(
        {
            "user_message": user_message,
            "ai_response": ai_reply
        }
    )


@login_required(login_url='/chatbot/login/')
def chat_page(request):

    return render(
        request,
        'chatbot/data.html'
    )


@login_required(login_url='/chatbot/login/')
def chat_history(request):

    conversations = ChatMessage.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'chatbot/history.html',
        {
            'conversations': conversations
        }
    )


@require_POST
@login_required(login_url='/chatbot/login/')
def clear_history(request):

    ChatMessage.objects.filter(
        user=request.user
    ).delete()

    return redirect('chat_history')


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

            login(request, user)

            return redirect('chat_page')

    else:

        form = RegisterForm()

    return render(
        request,
        'chatbot/register.html',
        {
            'form': form
        }
    )


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('chat_page')

        else:

            return render(
                request,
                'chatbot/login.html',
                {
                    'error': 'Invalid username or password.'
                }
            )

    return render(
        request,
        'chatbot/login.html'
    )


def logout_view(request):

    logout(request)

    return redirect('login')