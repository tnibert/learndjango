# to use: ./manage.py shell < createdbdata.py
from polls.models import Question, Choice
from django.utils import timezone
q = Question(question_text="What's good?", pub_date=timezone.now())
q.save()
q2 = Question(question_text="What's up?", pub_date=timezone.now())
q2.save()
