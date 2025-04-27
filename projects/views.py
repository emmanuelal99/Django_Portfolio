from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import ContactForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def index(request):
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        # Validate form fields with Django's built-in method
        if form.is_valid():
            name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                # Validate email manually just for an additional check (optional)
                validate_email(sender_email)
            except ValidationError:
                return HttpResponse('Invalid email address.', status=400)

            # Compose the email
            email_subject = f"New Contact Form Message from {name}"
            email_body = f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}"

            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=settings.EMAIL_HOST_USER,  # Admin email as the sender
                to=[settings.EMAIL_HOST_USER],  # Admin email to receive the message
                reply_to=[sender_email],  # User's email to reply to
            )

            try:
                email.send(fail_silently=False)
                messages.success(request, 'Your message has been successfully sent!')
                return redirect('index')  # Redirect to prevent form resubmission
            except Exception as e:
                messages.error(request, f"Error sending email: {str(e)}")
                return redirect('index')

        else:
            # Form is invalid, show error messages
            messages.error(request, "Make sure all fields are entered and valid.")

    return render(request, 'projects/project/index.html', {'projects': projects, 'form': form})

def details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project/details.html', {'project': project})

def resume_view(request):
    return render(request, 'projects/resume.html')












    




    
