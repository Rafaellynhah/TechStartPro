from django.urls import path
from olist import views


urlpatterns = [
    path('', views.list, name="list"),
    path('forms', views.forms, name="forms"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('<int:id>/', views.forms,name='update'),
    path('import/csv/', views.import_csv, name='import_csv'),

]
