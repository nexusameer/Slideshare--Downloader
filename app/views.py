from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    person = Person.load()
    background = Background.objects.all()
    skills = Skills.objects.all()
    project = Projects.objects.all()
    languages = Languages.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = 'ameerk10fw@gmail.com'
        form_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        From: {}\n
        Subject: {}\n
        Message:\n\t\t{}\n
        '''.format(form_data['name'], form_data['subject'], form_data['message'])
        send_mail(form_data['subject'], message, '', [email])  # Using subject as email subject

    context = {
        'person': person,
        'background': background,
        'skills': skills,
        'project': project,
        'languages': languages,
    }
    return render(request, 'app/index.html', context)


def download_document(request, document_id):
    person = get_object_or_404(Person, pk=document_id)
    file_path = person.document.path
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(person.document.name)
        return response
