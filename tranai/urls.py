from tranai.models import Sentence
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
    path('documents/search', views.search_documents, name='search-documents'),

    # Translation
    path('all_translations', views.index_all_translations, name='index-all-translations'),
    # path('documents/<document_id>/translations/', views.show_document_translations, name='show-document-translations'),

    path('documents/<document_id>/translations/', views.index_document_translations, name='index-document-translations'),
    path('documents/<document_id>/translations/<translation_id>/', views.show_document_translation, name='show-document-translation'),
    path('documents/<document_id>/translations/new', views.create_document_translation, name='create-document-translation'),
    path('documents/<document_id>/translations/<translation_id>/edit', views.update_document_translation, name='update-document-translation'),
    path('documents/<document_id>/translations/<translation_id>/delete', views.delete_document_translation, name='delete-document-translation'),

    path('lookup_link/documents/<document_id>/translations/<translation_id>', views.import_lookup, name='import-lookup'),
    path('lookup_delete_link/documents/<document_id>/translations/<translation_id>', views.delete_lookup, name='delete-lookup'),

    # Sentence
    # path('translations/<translation_id>/sentences/', views.index_translation_sentences, name='index-translation-sentences'),
    path('translations/<translation_id>/sentences/<sentence_id>/', views.show_translation_sentence, name='show-translation-sentence'),
    path('translations/<translation_id>/sentences/new', views.create_translation_sentence, name='create-translation-sentence'),
    path('translations/<translation_id>/sentences/<sentence_id>/edit', views.update_translation_sentence, name='update-translation-sentence'),
    path('translations/<translation_id>/sentences/<sentence_id>/delete', views.delete_translation_sentence, name='delete-translation-sentence'),

    # # Change #add AFTER import_content
    # # path('sentences/<sentence_id>/changes/', views.index_sentence_changes, name='index-sentence-changes'),
    # path('sentences/<sentence_id>/changes/<change_id>/', views.show_sentence_change, name='show-sentence-change'),
    # path('sentences/<sentence_id>/changes/new', views.create_sentence_change, name='create-sentence-change'),
    # path('sentences/<sentence_id>/changes/<change_id>/edit', views.update_sentence_change, name='update-sentence-change'),
    # path('sentences/<sentence_id>/changes/<change_id>/delete', views.delete_sentence_change, name='delete-sentence-change'),

    # Task
    path('tasks/', views.index_tasks, name='index-tasks'),
    path('tasks/<task_id>/', views.show_task, name='show-task'),
    path('tasks/new', views.create_task, name='create-task'),
    path('tasks/<task_id>/edit', views.update_task, name='update-task'),
    path('delete_task/<task_id>', views.delete_task, name='delete-task'),

    path('import_content_for_validation/tasks/<task_id>/', views.import_content_for_validation, name='import-content-for-validation'),
    path('import_content/tasks/<task_id>/', views.import_content, name='import-content'),

    # User
    path('users/', views.index_users, name='index-users'),
    # path('switch_current_task/translations/<translation_id>/sentences/<sentence_id>/', views.switch_current_task, name='switch-current-task'),
    path('switch_current_task/tasks/<task_id>/', views.switch_current_task, name='switch-current-task'),


]