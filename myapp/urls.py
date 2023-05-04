
from django_distill import distill_path
from .views import my_view

urlpatterns = [
distill_path('myapp/', my_view, name='my_static_page'),
]