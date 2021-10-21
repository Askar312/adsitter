from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Название поста',
        db_index=True
    )
    image = models.ImageField(
        upload_to='images/%Y/%m/%d',
        verbose_name='Фото'
    )
    likes = models.PositiveIntegerField(
        verbose_name='Лайки '
    )
    views = models.PositiveIntegerField(
        verbose_name='Просмотры'
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    update_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    draft = models.BooleanField(
        default=False,
        verbose_name='Черновик'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-create_at']

    def __str__(self):
        return f"{self.title}"
