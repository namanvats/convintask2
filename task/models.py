from django.db import models

# Create your models here.


class Task(models.Model):
    TYPE1 = 1
    TYPE2 = 2
    TYPE3 = 3
    TYPE4 = 4
    TYPE5 = 5
    TASK_TYPE = [
        (TYPE1, 1),
        (TYPE2, 2),
        (TYPE3, 3),
        (TYPE4, 4),
        (TYPE5, 5),
    ]
    task_type = models.IntegerField(
        choices=TASK_TYPE,
        default=TYPE1,
    )
    task_desc = models.TextField(max_length=255)

    def __str__(self):
        return self.task_desc


class TaskTracker(models.Model):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    UPDATE_TYPE = [
        (DAILY, 'Daily, Every day at 5PM'),
        (WEEKLY, 'Weekly, Every Monday'),
        (MONTHLY, 'Monthly, First day of Month'),
    ]
    update_type = models.CharField(
        max_length=32,
        choices=UPDATE_TYPE,
        default=DAILY,
    )
    task = models.ForeignKey(Task, related_name='trackers', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
