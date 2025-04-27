from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                f'New Contact from {name}',  # Subject line
                message,                     # Message body
                email,                       # From email
                [settings.ADMIN_EMAIL],      # To (Admin's email)
                fail_silently=False,
            )

            messages.success(request, 'Your message has been successfully sent!')
            return redirect('index')  # prevent form re-submission

    return render(request, 'projects/project/index.html', {'projects': projects, 'form': form})



def details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project/details.html', {'project': project})

def resume_view(request):
    return render(request, 'projects/resume.html')












    




    
