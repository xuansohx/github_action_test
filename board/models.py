from django.db import models

# Serverless (Python 함수를 Github이 실행해 줌)
class GithubLottery(models.Model):
    no = models.PositiveIntegerField()
    win_amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

# Async task queue (별도의 프로세스에서 특정 작업을 수행)
class CeleryArticle(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
