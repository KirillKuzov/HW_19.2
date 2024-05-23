from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта', **NULLABLE)
    picture = models.ImageField(upload_to='products/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="version",
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Продукт",
    )
    version_number = models.PositiveIntegerField(
        verbose_name="Номер версии",
        help_text="Введите номер версии продукта",
    )
    version_title = models.CharField(
        max_length=150,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    version_is_active = models.BooleanField(
        default=False, verbose_name="Признак текущей версии"
    )

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"

    def __str__(self):
        return f"{self.version_title}"
