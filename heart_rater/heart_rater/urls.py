from django.contrib import admin
from django.urls import path, include

from heart_rater.views import AddPressureRecordView, OkView, AddEventRecordView, \
    PressureListView, EventListView

urlpatterns = [
    path('', AddPressureRecordView.as_view(), name="pressure_add"),
    path('event/add', AddEventRecordView.as_view(), name="event_add"),
    path('ok', OkView.as_view(), name="ok"),
    path('pressure/log', PressureListView.as_view(), name="pressure_log"),
    path('event/log', EventListView.as_view(), name="event_log"),
    path('admin/', admin.site.urls, name="admin"),
    path('accounts/', include('django.contrib.auth.urls'))
]
