from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),

    # /polls/numero_pergunta/
    path('<int:question_id>/', views.detail, name='detail'),

    # /polls/numero_pergunta/resultado/
    path('<int:question_id>/results/', views.results, name='results'),

    # /polls/numero_pergunta/voto/
    path('<int:question_id>/vote/', views.vote, name='vote',),
]
