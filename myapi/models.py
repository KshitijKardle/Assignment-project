from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username or str(self.telegram_id)

