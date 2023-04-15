from django.db import models


class DemoModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="demo_images")

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # CASCADE câu hỏi bị xóa câu trả lời củng bị xóa
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
