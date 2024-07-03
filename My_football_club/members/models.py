from django.db import models

# Create your models here.
class Member(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	phone = models.IntegerField(null=True)
	joined_date = models.DateField(null=True)
	
	# def __str__(self) -> str:
	# 	if self.phone is None:
	# 		self.phone = 'Chưa có'
	# 	elif self.joined_date is None:
	# 		self.joined_date = 'Chưa có'
	# 	return f"Tên: {self.firstname} Họ: {self.lastname}, Phone:  {self.phone}, Joined_date {self.joined_date}"

