from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    # path('', views.index, name='index'),
    path("", views.IndexView.as_view(), name="index"),

    # /polls/numero_pergunta/
    # path('<int:question_id>/', views.detail, name='detail'),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # /polls/numero_pergunta/resultado/
    # path('<int:question_id>/results/', views.results, name='results'),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # /polls/numero_pergunta/voto/
    path('<int:question_id>/vote/', views.vote, name='vote'),


]
