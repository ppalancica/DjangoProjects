from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post
from marketing.models import Signup

def index(request):
    # queryset = Post.objects.filter(featured=True)
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list': featured,
        'latest': latest
    }
    return render(request, 'index.html', context)

def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        # If it's an empty page, return the last page
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        # 'post_list': post_list,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'blog.html', context)

def post(request):
    return render(request, 'post.html', {})
