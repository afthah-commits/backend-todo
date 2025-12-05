from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Root URL response
def home(request):
    return JsonResponse({"message": "Backend running successfully"})

urlpatterns = [
    path('', home, name='home'),              # Root URL
    path('admin/', admin.site.urls),          # Admin panel
    path('api/', include('api.urls')),        # API routes (very important)
]
