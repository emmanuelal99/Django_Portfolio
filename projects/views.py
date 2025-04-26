from django.shortcuts import render, get_object_or_404
from projects.models import Project
from projects.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError
# Create your views here.

def index(request):
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"Message from {name}"

            full_message = f"""
            You have received a new message from your portfolio website:

            Name: {name}
            Email: {sender}

            Message:
            {message}
            """

            try:
                send_mail(
                    subject,
                    full_message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                    headers={'Reply-To': sender}
                )
                messages.success(request, "Your message has been sent successfully!")
                form = ContactForm()  # Clear the form after successful send
            except BadHeaderError:
                messages.error(request, "Invalid header found.")
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")

    return render(request, 'projects/project/index.html', {'projects': projects, 'form': form})



def details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project/details.html', {'project': project})

def resume_view(request):
    return render(request, 'projects/resume.html')












    




   
