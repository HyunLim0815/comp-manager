from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import sys 
sys.path.append("..") 
from team.views import *
from student.views import *
from judge.views import *
from login.views import *
from organizer.views import *

urlpatterns = [
    path('<str:pk>/login-api-detail/', view = login_api_detail),
    path('login-api-list/', view = login_api_list),
    path('<str:pk>/judge-detail/', view = judge_detail),
    path('judge-list/', view = judgerlist),
    path('<str:pk>/org-info-detail/', view = Org_info_detail.as_view()),
    path('org-info-list/', view = Org_info_list.as_view()),
    path('<str:pk>/com-judge-detail/', view = com_judge_deatil.as_view()),
    path('com_judge_list/com-judge-list/', view = com_judge_list.as_view()),
    path('<str:pk>/com-organizer-detail/', view = com_organizer_detail.as_view()),
    path('com-organizer-list/', view = com_organizer_list.as_view()),
    path('<str:pk>/com-score-detail/', view = com_scroe_detail.as_view()),
    path('com-score-list/', view = com_scroe_list.as_view()),
    path('<str:pk>/com-team-detail/', view = com_team_detail.as_view()),
    path('com-team-list/', view = com_team_list.as_view()),
    path('<str:pk>/team-detail/', view = TeamDeatil.as_view()),
    path('team-list/', view = TeamList.as_view()),
    path('<str:pk>/stu-detail', view = StudentDeatil.as_view()),
    path('stu-list/', view = StudentList.as_view()),
    path('<str:pk>/user-info-detail', view = user_info_detail),
    path('user-info-list', view = user_info_list.as_view())
]