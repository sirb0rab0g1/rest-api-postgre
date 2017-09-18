from django.db import models


class Information(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.CharField(max_length=140)
    creation_date = models.DateTimeField('date created', auto_now_add=True)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.first_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'creation_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
