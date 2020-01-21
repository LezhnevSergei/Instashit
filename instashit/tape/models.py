from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.
class User(models.Model):
    name = models.CharField("Имя", max_length=50)
    avatar = models.ImageField("Аватар", upload_to="static/img/avatars", max_length=256, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"    

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name= "Автор", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="static/img/posts",default="", max_length=256, blank=False, null=False)
    comment = models.CharField("Комментарий", max_length=2000, blank=True, default="")
    like_count = models.PositiveIntegerField("Количество лайков", null=True)
    pub_date = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)


    def do_like(is_liked, self, request):
        if is_liked:
            self.like_count += 1
        else:
            self.like_count -= 1


    def __str__(self):
        return f'{self.author}:{self.id}'
    
