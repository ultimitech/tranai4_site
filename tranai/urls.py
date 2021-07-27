from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('documents/', views.index_documents, name='index-documents'),
    path('documents/<document_id>', views.show_document, name='show-document'),

    # Translation
    path('documents/<document_id>/translations/<translation_id>/', views.show_document_translation, name='show-document-translation'),

]