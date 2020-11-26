try:
    from django.urls import path
    from . import views
except Exception as e:
    error = f"Importation error has occored: {e}"
    print(error)

urlpatterns = [
    path('', views.index),
    path('new/', views.new_products)
]
