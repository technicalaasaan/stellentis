from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=10, choices=(
        ('BE', 'Bacholor of Engineering'), ('BA', 'Bachelor of Arts'), ('BSc', 'Bachelor of Science'), ('Others', 'Others')
    ), null=False, default='Others')
    address = models.TextField(null=False)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.first_name
