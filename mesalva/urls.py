"""mesalva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from . import consultations

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios-inativos', views.inactive_users, name='inactive-users'),
    path('conteudos-mais-comentados', views.top_commented_contents, name='top-commented-contents'),
    path('conteudos-melhor-avaliados', views.top_rated_content, name='top-rated-contents')
    ,
    path('atividade-usuarios', consultations.users_activity, name='users-activity'),
    path('avaliacao-redacao', consultations.evaluation_essay, name='evaluation-essay'),
    path('media-redacao', consultations.avg_essay, name='avg-essay'),
    path('usuario-sem-avaliacao', consultations.users_without_evaluation, name='users-without-evaluation'),
    path('exercicios', consultations.exercises, name='exercises'),
    path('exercicios-n-respondidos', consultations.not_answered_exercises, name='not-answered-exercises'),
    path('exercicio-gabarito', consultations.exercises_correct_answer, name='exercises-correct-answer'),
    path('usuario-taxa-acerto', consultations.user_hit_rate , name='user_hit_rate'),
    path('conteudo-atividade', consultations.content_activity , name='content-activity'),
    path('conteudo-gratuito', consultations.free_content, name='free-content'),
    path('comentarios', consultations.comments, name='comments'),
    path('pedidos', consultations.orders, name='orders')
]
