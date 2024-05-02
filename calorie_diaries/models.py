from django.db import models


# Create your models here.
class Diary(models.Model):
    date = models.DateField()
    label = models.CharField(max_length=100)

    def total_calorie(self):
        return sum(diary_entry.calorie for diary_entry in self.diaryentry_set.all())

    def eaten(self):
        return sum(
            diary_entry.calorie for diary_entry in self.diaryentry_set.all() if not diary_entry.is_burning_calorie)

    def burned(self):
        return sum(diary_entry.calorie for diary_entry in self.diaryentry_set.all() if diary_entry.is_burning_calorie)


class DiaryEntry(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calorie = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_burning_calorie = models.BooleanField()

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.is_burning_calorie:
            self.calorie = -self.calorie
        super().save(force_insert, force_update, using, update_fields)
