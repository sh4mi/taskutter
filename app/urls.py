from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from main.views import IndexPageView, ChangeLanguageView, ListDetailView, ListCreateView, ListUpdateView, ListDeleteView
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index'),
    path('list/new', ListCreateView.as_view(), name='list_create'),
    path('list/<int:pk>', ListDetailView.as_view(), name='list_detail'),
    path('list/update/<int:pk>', ListUpdateView.as_view(), name='list_update'),
    path('list/delete/<int:pk>', ListDeleteView.as_view(), name='list_delete'),

    # tasks
    path('task/new/<int:pk>', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
