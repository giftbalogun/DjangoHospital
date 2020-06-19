from django.shortcuts import render, get_object_or_404, redirect, reverse, redirect

from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

from care.models import Blog
from doctor.models import Doctor
from fact.models import Fact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q

from emailing.forms import EmailSignupForm
from emailing.models import Emailing

from .forms import CommentForm
from django.http import HttpResponse


form = EmailSignupForm()


def handler404(request, exception=None):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'includes/404.html', data)


def handler400(request, exception=None):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'includes/400.html', data)


def handler403(request, exception=None):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'includes/403.html', data)


def handler500(request, exception=None):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'includes/500.html', data)


def search(request):
    query = request.GET.get('q')

    queryset = Blog.objects.filter(
        Q(title__icontains=query))

    context = {
        'queryset': queryset
    }
    return render(request, 'includes/search_results.html', context)


def get_category_count():
    queryset = Blog \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


class SendBookingEmail(View):

    form = EmailSignupForm()

    def post(self, request, *args, **kwargs):
        email = request.POST.get("semail")
        new_signup = Emailing()
        new_signup.email = email
        new_signup.save()
        messages.success(request, "Successfully subscribed")
        return redirect("index")

    def get(self, request):
        # Get the form data
        name = request.GET.get('name', None)
        phone = request.GET.get('phone', None)
        email = request.GET.get('email', None)
        scheldule = request.GET.get('scheldule', None)
        message = request.GET.get('message', None)

        send_mail(
            'Appointment for: ' + name,
            'Message: ' + message + ',\n' +
            'Phone: ' + phone + ',\n' +
            'Schedule: ' + scheldule,
            'balogunigift@aol.com',  # Admin
            [
                email, 'blgnbalogun53@gmail.com',
            ]
        )

        # Redirect to same page after form submit
        messages.success(request, ('Your Booking Has Been Made.'))
        return redirect('index')


def index(request):
    latest = Blog.objects.order_by('-timestamp')[0:3]
    doctor = Doctor.objects.order_by('-name')
    fact = Fact.objects.order_by('-name')

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Emailing()
        new_signup.email = email
        new_signup.save()
        messages.success(request, "Successfully subscribed")

    context = {
        'latest': latest,
        'doctor': doctor,
        'fact': fact,
        'form': form
    }

    return render(request, 'index.html', context)


def blog_list(request):
    category_count = get_category_count()
    most_recent = Blog.objects.order_by('-timestamp')[:3]
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Emailing()
        new_signup.email = email
        new_signup.save()
        messages.success(request, "Successfully subscribed")

    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'category_count': category_count,
        'form': form
    }
    return render(request, 'blog.html', context)


def blog_detail(request, id):
    category_count = get_category_count()
    most_recent = Blog.objects.order_by('-timestamp')[:3]
    blog = get_object_or_404(Blog, id=id)

    comments = blog.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blog = blog
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'blog': blog,
        'most_recent': most_recent,
        'category_count': category_count,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form

    }
    return render(request, 'blog-details.html', context)


class SendContactEmail(View):

    def get(self, request):
        # Get the form data
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        send_mail(
            'Contact Message from: ' + name,
            'Message: ' + message + ',\n',
            'balogunigift@aol.com',  # Admin
            [
                email, 'blgnbalogun53@gmail.com'
            ]
        )
        # Redirect to same page after form submit
        messages.success(request, ('Your Message Has Been Sent.'))
        return redirect('contact')


def contact(request):

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Emailing()
        new_signup.email = email
        new_signup.save()
        messages.success(request, "Successfully subscribed")

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)


def about(request):
    doctor = Doctor.objects.order_by('-name')
    fact = Fact.objects.order_by('-name')

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Emailing()
        new_signup.email = email
        new_signup.save()
        messages.success(request, "Successfully subscribed")

    context = {
        'doctor': doctor,
        'fact': fact,
        'form': form
    }

    return render(request, 'about.html', context)
