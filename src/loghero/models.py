from django.db import models
from enum import Enum


class Status(models.TextChoices):
    PENDING = 'pending', 'Pending'
    SUCCESS = 'success', 'Success'
    FAILED = 'failed', 'Failed'


class Severity(models.TextChoices):
    INFO = 'info', 'Info'
    WARNING = 'warning', 'Warning'
    ERROR = 'error', 'Error'
    CRITICAL = 'critical', 'Critical'


class LogQuerySet(models.QuerySet):
    def to_dict(self):
        return self.values(
            "actor",
            "action",
            "severity",
            "status",
            "target_type",
            "target",
            "created_at",
            "ip_address",
            "user_agent",
            "url",
            "location",
            "result_type",
            "result",
            "description",
            "extra_data",
        )

class Log(models.Model):
    actor = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    severity = models.CharField(max_length=50, choices=Severity.choices, default=Severity.INFO)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.PENDING)
    target_type = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    ip_address = models.CharField(max_length=255, null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    result_type = models.CharField(max_length=255,null=True,blank=True)
    result = models.CharField(max_length=255,null=True,blank=True)

    description = models.TextField(null=True,blank=True)
    extra_data = models.JSONField(null=True, blank=True)

    objects = LogQuerySet.as_manager()

    def __str__(self):
        return f"{self.created_at.isoformat()} [{self.severity}] Actor: '{self.actor}' execute '{self.action}' on/by {self.target}, status: {self.status}, from {self.location}"

