from django.shortcuts import render
from .models import Post

def post_list(request):
    hosts = Post.objects.all()
    context = {'posts': hosts}

    return render(request,'post_list.html', context)



