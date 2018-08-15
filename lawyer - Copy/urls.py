from django.urls import path, include

from lawyer.views import lawyer_list, lawyer_detail, Home
 
app_name = 'lawyer'
 
urlpatterns = [
	path('lawyer', Home, name='homee'),
    path('', lawyer_list, name='lawyer_list'),
    path('<slug:category_slug>/', lawyer_list, name='lawyer_list_by_category'),
    path('<int:id>/<slug:name_slug>/', lawyer_detail, name='lawyer_detail'),
]