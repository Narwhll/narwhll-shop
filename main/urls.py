from django.urls import path
from main.views import show_main, show_json, show_json_by_id, show_xml, show_xml_by_id, create_product, show_product, show_catalogue

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/<str:id>/', show_xml_by_id),
    path('json/<str:id>/', show_json_by_id),
    path('json/', show_json),
    path('xml/', show_xml),
    path('add/', create_product, name="create_product"),
    path('productdetail/<str:id>', show_product, name="show_product"),
    path('browse/', show_catalogue, name="show_catalogue"),
    # path('employee/', show_employee, name="show_employee"),
    ]