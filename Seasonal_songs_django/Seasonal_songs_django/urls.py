from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.twentythree, name='base'),
    path('winter/', main.views.twentythree_w, name='winter'),
    path('spring_modal/', main.views.spring_modal),
    path('winter_modal/', main.views.winter_modal),
    path('spring_hall_of_frame/', main.views.spring_hall_of_frame),
    path('winter_hall_of_frame/', main.views.winter_hall_of_frame),
    path('1/', main.views.base, name='index'),
    path('1/2/', main.views.exam, name='exam'),
    path('1/3/', main.views.exam2, name='exam2'),
    
    
    

    path('twelve/', main.views.twelve, name='twelve'),
    path('thirteen/', main.views.thirteen, name='thirteen'),
    path('fourteen/', main.views.fourteen, name='fourteen'),
    path('fifteen/', main.views.fifteen, name='fifteen'),
    path('sixteen/', main.views.sixteen, name='sixteen'),
    path('seventeen/', main.views.seventeen, name='seventeen'),
    path('eighteen/', main.views.eighteen, name='eighteen'),
    path('nineteen/', main.views.nineteen, name='nineteen'),
    path('twenty/', main.views.twenty, name='twenty'),
    path('twentyone/', main.views.twentyone, name='twentyone'),
    path('twentytwo/', main.views.twentytwo, name='twentytwo'),
    path('twentythree/', main.views.twentythree, name='twentythree'),

    path('twelve_w/', main.views.twelve_w, name='twelve_w'),
    path('thirteen_w/', main.views.thirteen_w, name='thirteen_w'),
    path('fourteen_w/', main.views.fourteen_w, name='fourteen_w'),
    path('fifteen_w/', main.views.fifteen_w, name='fifteen_w'),
    path('sixteen_w/', main.views.sixteen_w, name='sixteen_w'),
    path('seventeen_w/', main.views.seventeen_w, name='seventeen_w'),
    path('eighteen_w/', main.views.eighteen_w, name='eighteen_w'),
    path('nineteen_w/', main.views.nineteen_w, name='nineteen_w'),
    path('twenty_w/', main.views.twenty_w, name='twenty_w'),
    path('twentyone_w/', main.views.twentyone_w, name='twentyone_w'),
    path('twentytwo_w/', main.views.twentytwo_w, name='twentytwo_w'),
    path('twentythree_w/', main.views.twentythree_w, name='twentythree_w'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
