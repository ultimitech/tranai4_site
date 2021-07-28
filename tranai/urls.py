from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),

    # Document
    path('documents/new', views.create_document, name='create-document'),
    path('documents/', views.index_documents, name='index-documents'),
    path('documents/<document_id>/', views.show_document, name='show-document'),
    path('documents/<document_id>/edit', views.update_document, name='update-document'),
    path('documents/<document_id>/delete', views.delete_document, name='delete-document'),

    # Translation
    path('all_translations', views.index_all_translations, name='index-all-translations'),
    # path('documents/<document_id>/translations/', views.show_document_translations, name='show-document-translations'),
    path('documents/<document_id>/translations/', views.index_document_translations, name='index-document-translations'),
    path('documents/<document_id>/translations/<translation_id>/', views.show_document_translation, name='show-document-translation'),
    path('documents/<document_id>/translations/new', views.create_document_translation, name='create-document-translation'),
    path('documents/<document_id>/translations/<translation_id>/edit', views.update_document_translation, name='update-document-translation'),
    path('documents/<document_id>/translations/<translation_id>/delete', views.delete_document_translation, name='delete-document-translation'),

    # Task
    path('tasks/', views.index_tasks, name='index-tasks'),
    path('tasks/<task_id>/', views.show_task, name='show-task'),
    path('tasks/new', views.create_task, name='create-task'),


]