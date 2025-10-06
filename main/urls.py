from django.urls import path
from main.views import show_main, show_json, show_json_by_id, register, login_user, logout_user, show_myproducts
from main.views import show_xml, show_xml_by_id, create_product, show_product, show_catalogue, edit_product
from main.views import delete_product, add_product_entry_ajax
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/<str:id>/', show_xml_by_id),
    path('json/<str:id>/', show_json_by_id, name="show_json_by_id"),
    path('json/', show_json, name="show_json"),
    path('xml/', show_xml),
    path('add/', create_product, name="create_product"),
    path('productdetail/<str:id>', show_product, name="show_product"),
    path('browse/', show_catalogue, name="show_catalogue"),
    # path('employee/', show_employee, name="show_employee"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login_user"),
    path('logout/', logout_user, name="logout_user"),
    path('myproducts/', show_myproducts, name="show_myproducts"),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('create-product-ajax/', add_product_entry_ajax, name="add_product_entry_ajax"),
    ]