from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
        
    }

    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    # 에러메시지에 request information 보고 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # DB에 저장하기
    post = Post()
    post.title = title # title에 들어온 값을 post.title 컬럼에 값을 채워넣는 역할
    post.content = content
    post.save() # 입력된 값들을 DB로 보내주는 역할

    return redirect(f'/posts/{post.id}/')

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/posts/')

def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    return render(request, 'edit.html', context)


def update(request, id):
# 기존 정보 가져오기
    post = Post.objects.get(id=id)

# 새로운 정보 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')

# 기존 정보를 새로운 정보로 덮어씌우기
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')