from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError
from django.http import HttpResponse

def index(request):
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        # Retrieve form fields
        name = request.POST.get("name", "")
        message = request.POST.get("message", "")
        from_email = request.POST.get("from_email", "")

        if name and message and from_email:  # Check if all required fields are present
            try:
                # Send email
                send_mail(name, message, from_email, ["admin@example.com"])
                messages.success(request, 'Your message has been successfully sent!')
                return redirect('index')  # Redirect to index page after sending email
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
        else:
            return HttpResponse("Make sure all fields are entered and valid.")
    
    return render(request, 'projects/project/index.html', {'projects': projects, 'form': form})

def details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project/details.html', {'project': project})

def resume_view(request):
    return render(request, 'projects/resume.html')












    




    
