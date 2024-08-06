from django.db import models


class Sign_up(models.Model):
    First_Name = models.CharField(max_length=250)
    Last_name = models.CharField(max_length=250)
    Email = models.EmailField(unique=True)
    Username = models.CharField(max_length=250, unique=True)
    Password = models.CharField(max_length=250)

    # def get_absolute_url(self):
    #     return reverse('myapp:Index', kwargs={'pk': self.pk})

    # def _str_(self):
    #     return self.First_Name + '-' + self.Last_name + '-' + self.Email + '-' + self.Username + '-' + self.Password
