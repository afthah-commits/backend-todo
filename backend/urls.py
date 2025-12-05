from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


# Optional root route response
def home(request):
    return JsonResponse({"message": "Backend running successfully"})


urlpatterns = [
    path('', home),                   # optional root path
    path('admin/', admin.site.urls),  # admin panel
    path('api/', include('api.urls')),  # include API app routes

]
