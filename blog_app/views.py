from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post
from django.core.paginator import Paginator,EmptyPage


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm


def frontpage(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,5)
    try:
        if request.GET.get('page'):
            posts = paginator.page(request.GET.get('page'))
        else:
            posts = paginator.page(5)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog_frontend/frontpage.html', {'posts': posts})



def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content
            })

            send_mail('The contact form subject', 'This is the message', 'noreply@codewithstein.com', ['codewithtestein@gmail.com'], html_message=html)

            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {
        'form': form
    })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', post=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog_frontend/post_details.html', {'post': post, 'form': form})