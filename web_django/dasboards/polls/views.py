#http://localhost:8000/polls/
#Username:alpha
#Paword: admin
#Email address : alphadiop@gmail.com
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Upload
from django.shortcuts import get_object_or_404, render,redirect
from .forms import UploadFileForm
import os
from django.conf import settings
import csv
from io import StringIO
from django.core.files.storage import FileSystemStorage


def home(request):
    documents = Upload.objects.all()
    return render(request, 'polls/home.html', { 'documents': documents })

#https://tutorial.djangogirls.org/fr/django_forms/



def success(request):
    upload = Upload.objects.order_by('name')
    return render(request, "polls/success.html", {"upload": upload})


def file_upload(request):
    save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
    path = default_storage.save(save_path, request.FILES['file'])
    return default_storage.path(path)
#---------------------------------------------------------------------------------


    
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'polls/simple_upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'polls/upload.html')
    
    
#-----------------------------------------------------------------------
def create_data(data):
    Upload.objects.bulk_create(generator())


def generator(data):
    for row in data:
        yield Upload(field1=data['field1'])


#-----televersement de fichiers liés à un modèle---------------------------------
#pour enregistrer un fichier dans un Model contenant un chap FileField
#l'emploi d'un formulaire ModelForm simplifie le processus.
#form.is_valid() : permet de vérifier que le formulaire a été rempli correctement
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/success/')
            return redirect('/polls')
    else:
        form = UploadFileForm()
    return render(request, 'polls/entry.html', {'form': form})

#form = UploadFileForm(request.POST, request.FILES)
#post = form.save(commit=False)
#post.name = request.name
#post.file = request.file
#post.save()



#https://docs.djangoproject.com/fr/4.0/topics/http/file-uploads/
#les données du fichier aboutissent dans "request.FILES" pour une méthode POST
#Chaque vue est responsable de renvoyer un objet HttpResponse.
#objets HttpRequest et HttpResponse, qui sont définis dans le module django.http.

#les données sont accessibles dans request.FILES['file'].
def upload_filexx(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request,'polls/upload.html', {'form': form})

#construrcteur du formulaire : UploadFileForm
#transmettre request.FILES au constructeur du formulaire : 
#UploadFileForm(request.POST, request.FILES)

def handle_uploaded_file(upload):
    contents = file.read().decode('ascii')# if Python 3
    my_model = Upload(some_other_field='something')
    my_model.field = contents
    my_model.save()

#gérer un fichier téléversé 
def handle_uploaded_filexx(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)







#--------------------------------------------------------------------
def indexxxxx(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))

def indexx(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

#----------------------------------------------------------------------



#----------------------------------------------------------------------

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def detail_(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



