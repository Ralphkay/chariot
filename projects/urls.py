from django.urls import path

from projects.views import projects, create_project, edit_project, delete_project, project_monetary_contributions, \
    create_project_monetary_contribution, edit_project_monetary_contribution, delete_project_monetary_contribution, \
    project_item_contributions, create_project_item_contribution, edit_project_item_contribution, \
    delete_project_item_contribution, project_expenses, create_project_expense, edit_project_expense, \
    delete_project_expense, project_documents, create_project_document, edit_project_document, delete_project_document

urlpatterns = [
    path('', projects, name="projects"),
    path('create-project/', create_project, name="create-project"),
    path('edit-project/<int:pk>', edit_project, name="edit-project"),
    path('delete-project/<int:pk>', delete_project, name="delete-project"),

    path('<int:project_pk>/monetary-contributions', project_monetary_contributions, name="project-monetary-contributions"),
    path('<int:project_pk>/create-project-monetary-contribution/', create_project_monetary_contribution, name="create-project-monetary-contribution"),
    path('<int:project_pk>/edit-project-monetary-contribution/<int:pmc_pk>', edit_project_monetary_contribution, name="edit-project-monetary-contribution"),
    path('<int:project_pk>/delete-project-monetary-contribution/<int:pmc_pk>', delete_project_monetary_contribution, name="delete-project-monetary-contribution"),


    path('<int:project_pk>/item-contributions', project_item_contributions, name="project-item-contributions"),
    path('<int:project_pk>/create-project-item-contribution/', create_project_item_contribution,
         name="create-project-item-contribution"),
    path('<int:project_pk>/edit-project-item-contribution/<int:pmc_pk>', edit_project_item_contribution,
         name="edit-project-item-contribution"),
    path('<int:project_pk>/delete-project-item-contribution/<int:pmc_pk>', delete_project_item_contribution,
         name="delete-project-item-contribution"),

    path('<int:project_pk>/expenses', project_expenses, name="project-expenses"),
    path('<int:project_pk>/create-project-expense/', create_project_expense, name="create-project-expense"),
    path('<int:project_pk>/edit-project-expense/<int:pmc_pk>', edit_project_expense, name="edit-project-expense"),
    path('<int:project_pk>/delete-project-expense/<int:pmc_pk>', delete_project_expense, name="delete-project-expense"),

    path('<int:project_pk>/documents', project_documents, name="project-documents"),
    path('<int:project_pk>/create-project-document/', create_project_document, name="create-project-document"),
    path('<int:project_pk>/edit-project-document/<int:pmc_pk>', edit_project_document, name="edit-project-document"),
    path('<int:project_pk>/delete-project-document/<int:pmc_pk>', delete_project_document, name="delete-project-document"),

]