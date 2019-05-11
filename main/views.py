from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Lists, Tasks
from django.urls import reverse_lazy


class IndexPageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = Lists.objects.all()
        counts = []
        priority = []
        for l in context['lists']:
            counts.append(Tasks.objects.filter(lists=l.id).count())
            priority.append(Tasks.objects.filter(
                lists=l.id, priority=1).count())
        context['counts'] = counts
        context['priority'] = priority
        return context


class ListCreateView(CreateView):
    model = Lists
    fields = ['title', 'description']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListDetailView(DetailView):
    model = Lists

    def get_context_data(self, *args, **kwargs):
        context = super(ListDetailView, self).get_context_data(*args, **kwargs)
        list_id = context['object'].id
        context['tasks'] = Tasks.objects.filter(
            lists_id=list_id).order_by('priority')
        return context


class ListUpdateView(UpdateView):
    model = Lists
    fields = ['title', 'description']
    success_url = reverse_lazy('index')
    template_name_suffix = '_update_form'


class ListDeleteView(DeleteView):
    model = Lists
    success_url = reverse_lazy('index')


class TaskCreateView(CreateView):
    model = Tasks
    fields = ['title', 'description', 'priority']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.lists = Lists.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Tasks


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'


class TaskUpdateView(UpdateView):
    model = Tasks
    fields = ['title', 'description', 'priority']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('index')


class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = reverse_lazy('index')
