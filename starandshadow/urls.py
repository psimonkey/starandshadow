from django.conf.urls import patterns, url, include
from programming.feeds import listPeriodFeed, listTodayFeed, listWeekFeed, listNextWeekFeed, listMonthFeed, listNextMonthFeed
from tastypie.api import Api
from api.handlers import *
from registration.signals import user_activated
from django.dispatch import receiver
from programming.models import Programmer
import os
from django.conf import settings
from django.db import IntegrityError

from django.contrib import admin

admin.autodiscover()


@receiver(user_activated)
def create_programmer(sender, user, request, **kwargs):
    p = Programmer(name=user.username, email=user.email, user=user)
    try:
        p.save()
    except IntegrityError:
        pass


api_v1 = Api(api_name='1')
api_v1.register(PageResource())
api_v1.register(SeasonResource())
api_v1.register(FilmResource())
api_v1.register(GigResource())
api_v1.register(EventResource())
api_v1.register(FestivalResource())
api_v1.register(MeetingResource())
api_v1.register(MinutesResource())
api_v1.register(DocumentResource())
api_v1.register(SelectSeasonResource())
api_v1.register(SelectProgrammerResource())
api_v1.register(SelectMeetingResource())
api_v1.register(SelectRatingResource())
api_v1.register(SelectCertificateResource())
api_v1.register(SelectFilmFormatResource())
api_v1.register(SelectPictureResource())
api_v1.register(SelectApprovalResource())
api_v1.register(SelectMenuResource())

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include(api_v1.urls)),
    (r'^upload/', include('fileupload.urls')),
    url(r'^accounts/login/?$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/?$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': os.path.join(settings.PROJECT_ROOT, 'static')}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': os.path.join(settings.PROJECT_ROOT, 'static')}),
)
urlpatterns += patterns(
    'programming.views',
    (r'^on/today/?$', 'listToday'),
    (r'^on/thisweek/?$', 'listWeek'),
    (r'^on/nextweek/?$', 'listNextWeek'),
    (r'^on/thismonth/?$', 'listMonth'),
    (r'^on/nextmonth/?$', 'listNextMonth'),

    url(r'^on/(?P<year>\d{4})(/w(?P<week>\d{1,2})|/(?P<month>\d{1,2})(/(?P<day>\d{1,2})|)|/?)/?$',
        'listPeriod', name='listPeriod'),

    (r'^on/today/feed/?$', listTodayFeed()),
    (r'^on/thisweek/feed/?$', listWeekFeed()),
    (r'^on/nextweek/feed/?$', listNextWeekFeed()),
    (r'^on/thismonth/feed/?$', listMonthFeed()),
    (r'^on/nextmonth/feed/?$', listNextMonthFeed()),
    (r'^on/(?P<year>\d{4})(/w(?P<week>\d{1,2})|/(?P<month>\d{1,2})(/(?P<day>\d{1,2})|)|/?)/feed/?$',
     listPeriodFeed()),

    url(r'^on/season/(?P<id>\d+)/?$', 'season', name='show-season'),
    url(r'^on/film/(?P<id>\d+)/?$', 'film', name='show-film'),
    url(r'^on/gig/(?P<id>\d+)/?$', 'gig', name='show-gig'),
    url(r'^on/event/(?P<id>\d+)/?$', 'event', name='show-event'),
    url(r'^on/festival/(?P<id>\d+)/?$', 'festival', name='show-festival'),
    url(r'^on/meeting/(?P<id>\d+)/?$', 'meeting', name='show-meeting'),
)
urlpatterns += patterns(
    'organisation.views',

    url(r'^org/on/(?P<year>\d{4})/(?P<month>\d{1,2})/text/?$', 'monthReportText',
        name='month-report-text'),
    url(r'^org/on/(?P<year>\d{4})/(?P<month>\d{1,2})/?$', 'monthReport', name='month-report'),

    url(r'^org/on/?$', 'reportIndex', name='report-index'),

    url(r'^org/returns/(?P<year>\d{4})/(?P<month>\d{1,2})/?$', 'returnReport',
        name='return-report'),
    url(r'^org/returns/forfilm/(?P<filmId>\d+/?)?$', 'returnEdit', name='return-addforfilm'),
    url(r'^org/returns/(?P<id>\d+/?)$', 'returnEdit', name='return-film'),
    url(r'^org/returns/?$', 'returnReportIndex', name='return-index'),

    url(r'^org/changelog/?$', 'changeLog', name='change-log'),

    url(r'^org/meetings/(?P<year>\d{4})?/?$', 'meetingsReport', name='meetings-report'),

    url(r'^org/minutes/add/(?P<forMeeting>\d+)/?$', 'minutesAdd', name='add-minutes'),
    url(r'^org/minutes/(?P<minutesId>\d+/?)$', 'minutesView', name='view-minutes'),

    url(r'^org/who/(?P<volunteerId>\d+)/?$', 'volunteerProfile', name='volunteerProfile'),
    url(r'^org/who/me/?$', 'volunteerMe', name='volunteerMe'),
    url(r'^org/who/?$', 'volunteerIndex', name='volunteerIndex'),
)
urlpatterns += patterns(
    'content.views',
    url(r'^work/review/?$', 'documentList', name='list-document'),
    url(r'^work/review/add/?$', 'documentAdd', name='add-document'),
    url(r'^work/review/(?P<documentId>\d+)/?$', 'documentView', name='view-document'),
    (r'^signup/?$', 'pageSignup'),
    (r'^(?P<linkText>[\w\/-]+)/?$', 'page'),
    (r'^/?$', 'page'),
)
