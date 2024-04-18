from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name='index'),
    path('winter/', main.views.winter, name='winter'),
    path('spring_modal/', main.views.spring_modal),
    path('winter_modal/', main.views.winter_modal),
    path('spring_hall_of_frame/', main.views.spring_hall_of_frame),
    path('winter_hall_of_frame/', main.views.winter_hall_of_frame),

    path('twenty/', main.views.twenty, name='twenty'),
    path('twentyone/', main.views.twentyone, name='twentyone'),
    path('twentytwo/', main.views.twentytwo, name='twentytwo'),
    path('twentythree/', main.views.twentythree, name='twentythree'),

    path('twenty_w/', main.views.twenty_w, name='twenty_w'),
    path('twentyone_w/', main.views.twentyone_w, name='twentyone_w'),
    path('twentytwo_w/', main.views.twentytwo_w, name='twentytwo_w'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
