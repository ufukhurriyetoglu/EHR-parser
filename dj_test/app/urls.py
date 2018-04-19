from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recruiter/', views.RecruiterView.as_view(), name='recruiter'),
    path('candidate/', views.CandidateView.as_view(), name='candidate'),
    path('candidate/submit/', views.submit_cv, name='submit_cv'),
    path('recruiter/signup/', views.signup, name="signup"),
    path('recruiter/login/', auth_views.LoginView.as_view(template_name='app/login.html', redirect_field_name='recruiter/'), name="signin"),
    path('recruiter/logout/', views.logout_view),

    path('recruiter/job_offer/', views.JobOfferView.as_view(), name='Job offer'),
    path('recruiter/view_offer/', views.OfferListView.as_view(), name='View offers'),
    path('recruiter/view_offer/<int:offer_id>/', views.OfferFormView.as_view()),
    path('recruiter/view_offer/<int:offer_id>/match/', views.MatchView.as_view()),
    path('recruiter/view_offer/<int:offer_id>/match/<int:cand_id>/', views.CandidateMatchView.as_view()),
    path('recruiter/view_offer/<int:offer_id>/match/<int:cand_id>/contact/', views.CandidateContactView.as_view()),
    path('recruiter/parse_cvs/', views.ParserView.as_view(), name='Batch parser'),

    path('recruiter/job_offer/submit/', views.submit_jo, name='submit_jo'),
]
