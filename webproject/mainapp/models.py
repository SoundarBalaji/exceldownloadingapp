from django.db import models

class Quot(models.Model):
    category = models.CharField(max_length = 10,choices=[('A','A'),('B','B'),('C','C')])
    quantity = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True)
    def __int__(self):
        return self.pk