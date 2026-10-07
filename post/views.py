from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment

def index(request):
    return render(request, 'index.html')

def index(request):
    comments = Comment.objects.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            text_content = request.POST.get('comment_text')
            if text_content and text_content.strip():
                Comment.objects.create(
                    user=request.user,
                    text=text_content.strip()
                )
                return redirect('/post/')
        else: return redirect('/accounts/login/')

    return render(request, 'index.html', {'comments': comments})