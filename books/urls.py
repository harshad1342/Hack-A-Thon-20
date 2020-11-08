from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name="index"),
                  path('about', views.about, name="about"),
                  path('<int:book_id>', views.book, name="book"),
                  path('donate', views.donate, name="donate"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
