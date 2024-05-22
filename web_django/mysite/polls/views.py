# Create your views here.
#https://github.com/raszidzie/Django-Import-Export/tree/master/reports
#diop
#Ibrahima1
# print(python --version)
# print(python -m django --version)
#home
# import django
# print(django.VERSION)

from django.http import HttpResponse,HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from tablib import Dataset
from django.urls import reverse,NoReverseMatch
from django.views import generic
from django.utils import timezone

#vote
###---------------------------------------
##polls/index.html

#from django.test.utils import setup_test_environment
#setup_test_environment()
def people(request):
    istekler = hotel.objects.all()
    return render(request, 'list.html', locals())


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
        # """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # def get_queryset(self):
        # """
        # Excludes any questions that aren't published yet.
        # """
        # return Question.objects.filter(pub_date__lte=timezone.now())
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html',{'question': question,'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


##################################################################################

def resultsTT(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

from django.shortcuts import get_object_or_404, render
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def results_tgg(request, question_id):
    question_obj = get_object_or_404(Question, pk=question_id)
    question = get_list_or_404(question, to=question_obj)
    return render(request, 'polls/results.html', {'question': question})


################################################################################################
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def voteII(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


from .models import Choice, Question
# ...

##reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)	



#Exemple : return render(request, 'auth_lifecycle/user_profile.html',context_instance=RequestContext(request))
###############################################################################


from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question

def index_(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))
##---------------------------------------------------
def indexss(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
##------------------------------

def indexBB(request):
    return HttpResponse("You are at the polls index")
	
def indexTT(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
	
def indexDD(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def indexUU(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
	
# # Leave the rest of the views (detail, results, vote) unchanged
# from .models import Question

def indexsss(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


###-------------------------------------------------------------------------------
##Detail
from django.http import Http404
from django.shortcuts import render
from .models import Question

def detailRR(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
	
	
def detailYY(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})	
# def index(request):

# # ...
def detailMM(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def detailYY(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def detailTT(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        #raise Http404("Question does not exist")
        return HttpResponseNotFound("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

#HttpResponseRedirect(reverse('detail', kwargs={"pk": job.pk}))
##reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# from django.http import Http404
# from django.shortcuts import render
# from polls.models import Poll

# def detailTest(request, poll_id):
    # try:
        # p = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
        # raise Http404("Poll does not exist")
    # return render(request, 'polls/detail.html', {'poll': p})
	

# # pour appeler cette vue, il faut l'associer à une URL, et pour cela nous avons besoin d'un uRLconf
# # Pour créer un URLconf dans le repertoire polls, créez un fichier nommé urls_taxi.py.

########################################################################################

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


##################################################################
from django.http import HttpResponseRedirect
from django.urls import reverse
from .resources import EmployeeResource
from .models import Employee

def home_view(request):
    return render(request, 'polls/base.html')

def import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        employee_resource = EmployeeResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
            result = employee_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='json')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            employee_resource.import_data(dataset, dry_run=False)
    return render(request, 'import.html')    

def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        employee_resource = EmployeeResource()
        dataset = employee_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   
    return render(request, 'export.html')


def people(request):
    istekler = hotel.objects.all()
    return render(request, 'list.html', locals())


def post_treasure(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        treasure = Treasure(name = form.cleaned_data['name'],
                        value = form.cleaned_data['value'],
                        material = form.cleaned_data['material'],
                        location = form.cleaned_data['location'],
                        img_url = form.cleaned_data['img_url'])
        treasure.save()
    return HttpResponseRedirect('/numbers/')


# class RegisterView(View):
# def post(self, request):
    # form = UserCreateForm(request.POST)

    # if form.is_valid():
        # form.save()
        # return redirect(reverse(home))
    # return render(request, 'accounts/register.html', {'form': form})

# def get(self, request):
    # form = UserCreateForm()
    # return render(request, 'accounts/register.html', {'form': form})`