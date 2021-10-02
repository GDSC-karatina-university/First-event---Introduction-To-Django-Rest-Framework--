from django.conf.urls import url
from api.views.category.create import category
app_name = "api"

urlpatterns = [
    url(r"^category",category,name="Category")
]


