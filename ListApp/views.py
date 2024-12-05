from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import ListTask
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def miand(request ):
    return render(request, 'main.html', {} )

def showList(request):
    tasks = ListTask.objects.all()
    return render(request, 'showList.html', {'tasks':tasks})

class Taskview(LoginRequiredMixin, ListView):
    model = ListTask
    context_object_name = 'tasks'
    template_name = 'lsitView.html'
    def get_context_data(self, **kwargs):
        cont = super().get_context_data(**kwargs)
        cont['tasks'] = cont['tasks'].filter(user = self.request.user)
        cont['count'] = cont['tasks'].filter(complet = False).count()

        serch_input = self.request.GET.get('serch')
        if serch_input:
            cont['tasks'] = cont['tasks'].filter(title__icontains = serch_input) or ""  #or search via startswith
        cont['ddd'] = serch_input

        return cont
class TaskDetil(LoginRequiredMixin, DetailView):
    model= ListTask
    template_name= 'task_detail.html'
    context_object_name = 'tas'

class creatTask(LoginRequiredMixin, CreateView):
    model = ListTask
    fields = ['title', 'desc', 'complet']
    template_name= 'creat_form.html'
    success_url = reverse_lazy('Taskview')
    context_object_name = 'form'
    def form_valid(self, form) :
        form.instance.user = self.request.user
        return super(creatTask, self).form_valid(form)

class updateTask(UpdateView):
    model = ListTask
    fields = fields = ['title', 'desc', 'complet']
    success_url = reverse_lazy('Taskview')
    template_name = 'update.html'
    

class DelteTask(LoginRequiredMixin, DeleteView):
    model = ListTask
    success_url = reverse_lazy('Taskview')
    template_name = 'delete.html'
    context_object_name = 'task'

class Loginn(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url (self):
        return reverse_lazy('Taskview')
    
class Regeister(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('Taskview')
    def form_valid(self, form) :
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Regeister, self).form_valid(form)
    
    def get (self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect ('Taskview')
        return super(Regeister, self).get(*args, **kwargs)
    
    