from rest_framework import serializers
from task import models


class TaskTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'update_type',
            'task',
            'email',
        )
        model = models.TaskTracker
