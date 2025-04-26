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
            cleaned_data = form.cleaned_data
            print(cleaned_data)  # Temporary for debugging

            name = cleaned_data.get('name', 'No Name')
            email = cleaned_data.get('email', 'noemail@example.com')
            subject = cleaned_data.get('subject', 'No Subject')
            message = cleaned_data.get('message', '')

            # Send email
            send_mail(
                f'From {name}, Subject: {subject}',
                f'Message: {message}',
                email,  # From email
                [settings.ADMIN_EMAIL],  # Admin email
                fail_silently=False,
            )

            messages.success(request, 'Your message has been successfully sent!')

            return redirect('index')

    return render(request, 'projects/project/index.html', {'projects': projects, 'form': form})



def details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project/details.html', {'project': project})

def resume_view(request):
    return render(request, 'projects/resume.html')












    




    
