"""
Heart rate logger: main views
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from heart_rater.models import PressureRecord, EventRecord


class CreateWithUserView(CreateView):
    """
    View class: CreateView adding .user field
    """
    def form_valid(self, form):
        # Save session user
        form.instance.user = self.request.user
        return CreateView.form_valid(self, form)


class AddPressureRecordView(CreateWithUserView, LoginRequiredMixin):
    """
    Add pressure record view
    """
    model = PressureRecord
    template_name = "add_form.html"
    fields = ('sys', 'dia', 'hr', 'comment', 'time')

    success_url = '/ok?rec=Pressure&ret='

    def get_form(self, form_class=None):
        # Make comment non-required
        form = CreateView.get_form(self, form_class)
        form.fields["comment"].required = False
        return form


class PressureListView(ListView):
    """
    Pressure list view
    """
    model = PressureRecord
    paginate_by = 100
    template_name = "list_pressure.html"


class EventListView(ListView):
    """
    Pressure list view
    """
    model = EventRecord
    paginate_by = 100
    template_name = "list_event.html"


class AddEventRecordView(CreateWithUserView, LoginRequiredMixin):
    """
    Add event record view
    """
    model = EventRecord
    template_name = "add_form.html"
    fields = ('event', 'time')
    success_url = '/ok?rec=Event&ret=event'


class OkView(TemplateView):
    template_name = "ok.html"


class ConstructionView(TemplateView):
    template_name = "construction.html"
