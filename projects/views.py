from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse

def index(request):
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        # Validate the form
        if form.is_valid():
            # Retrieve form fields
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            
            try:
                # Send email
                send_mail(f'Message from {name}', message, from_email, ["admin@example.com"])
                messages.success(request, 'Your message has been successfully sent!')
                return redirect('index')  # Redirect to prevent form resubmission
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
        else:
            messages.error(request, "Make sure all fields are entered and valid.")

    return render(request, 'projects/project/index.html', {'projects': projects, 'form': form})

def details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project/details.html', {'project': project})

def resume_view(request):
    return render(request, 'projects/resume.html')












    




    
