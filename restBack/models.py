from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Создаем класс менеджера пользователей
class MyUserManager(BaseUserManager):
    # Создаём метод для создания пользователя
    def _create_user(self, email, username, password, **extra_fields):
        # Проверяем есть ли Email
        if not email:
            # Выводим сообщение в консоль
            raise ValueError("Вы не ввели Email")
        # Проверяем есть ли логин
        if not username:
            # Выводим сообщение в консоль
            raise ValueError("Вы не ввели Логин")
        # Делаем пользователя
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем всё остальное
        user.save(using=self._db)
        # Возвращаем пользователя
        return user

    # Делаем метод для создание обычного пользователя
    def create_user(self, email, username, password):
        # Возвращаем нового созданного пользователя
        return self._create_user(email, username, password)

    # Делаем метод для создание админа сайта
    def create_superuser(self, email, username, password):
        # Возвращаем нового созданного админа
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)  # Идентификатор
    username = models.CharField(max_length=50, unique=True)  # Логин
    email = models.EmailField(max_length=100, unique=True)  # Email
    exponent = models.ForeignKey("Exponent", blank=True, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)  # Статус активации
    is_staff = models.BooleanField(default=False)  # Статус админа

    USERNAME_FIELD = 'email'  # Идентификатор для обращения
    REQUIRED_FIELDS = ['username']  # Список имён полей для Superuser

    objects = MyUserManager()  # Добавляем методы класса MyUserManager

    # Метод для отображения в админ панели
    def __str__(self):
        return self.email


class Exponent(models.Model):
    name = models.CharField(max_length=180, blank=True, null=False, default='Нет имени',
                            verbose_name='Наименование экспонента')
    description = models.CharField(max_length=255, blank=True, null=False, default='Нет описания',
                                   verbose_name='Описание экспонента')
    title = models.CharField(max_length=255, blank=False, null=False, default='Test', verbose_name='Meta title')
    meta_keywords = models.CharField(max_length=255, blank=False, null=False, default='Нет мета-ключевых слов',
                                     verbose_name='Meta ключевые слова')
    meta_description = models.CharField(max_length=255, blank=False, null=False, default='Нет мета-описания',
                                        verbose_name='Meta описание')
    about_company = models.CharField(max_length=355, blank=True, null=False, default='Нет истории компании',
                                     verbose_name='О компании')
    logo = models.ImageField(upload_to='logo_exp/%Y/%m/%d/', blank=True, null=True, verbose_name='Логотип компании')
    main_picture = models.ImageField(upload_to='main_picture_exp/%Y/%m/%d/', blank=True, null=True,
                                     default='Нет картинки',
                                     verbose_name='Главное изображение')
    category = models.ForeignKey("Category", on_delete=models.PROTECT, blank=True, null=True, default=None,
                                 verbose_name='Категория')
    fio_contact = models.CharField(max_length=255, blank=True, null=False, default='Нет контактного лица',
                                   verbose_name='ФИО контактного лица')
    inn_exponent = models.BigIntegerField(blank=True, null=False, default=0, verbose_name='ИНН экспонента')
    urid_address = models.CharField(max_length=255, blank=True, null=False, default='Нет адреса',
                                    verbose_name='Юридический адрес')
    prod_address = models.CharField(max_length=255, blank=True, null=False, default='Нет адреса',
                                    verbose_name='Адрес производства')
    locations = models.ForeignKey("Location", on_delete=models.PROTECT, blank=True, null=True, default=None,
                                  verbose_name='Локации')
    partners = models.ForeignKey("Partner", on_delete=models.PROTECT, blank=True, null=True, default=None,
                                 verbose_name='Партнеры/клиенты компании')
    review = models.ForeignKey("Review", on_delete=models.PROTECT, blank=True, null=True, default=None,
                               verbose_name='Отзывы партнеров')
    catalog = models.ForeignKey("Catalog", on_delete=models.PROTECT, blank=True, null=True, default=None,
                                verbose_name='Каталог компании')
    portfolio = models.ForeignKey("Case", on_delete=models.PROTECT, blank=True, null=True, default=None,
                                  verbose_name='Портфолио')
    import_substitution = models.BooleanField(blank=True, null=False, default=True, verbose_name='Импортозамещение')
    publications = models.ForeignKey("Publication", on_delete=models.PROTECT, blank=True, null=True, default=None,
                                     verbose_name='Публикации')


class Publication(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False, default='Нет имени', verbose_name='Наименование')
    type = models.CharField(max_length=255, blank=True, null=False, default='Без типа', verbose_name='Тип')
    is_published = models.CharField(max_length=255, blank=True, null=False, default='Нет', verbose_name='Публикация')
    date_of_create = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    comment = models.CharField(max_length=255, blank=True, null=False, default='Без комментария',
                               verbose_name='Комментарий от модератора')


class Catalog(models.Model):
    category = models.ForeignKey("Category", on_delete=models.PROTECT, blank=True, null=True, default=None,
                                 verbose_name='Категория')
    product = models.ManyToManyField("Product")
    publish_price = models.CharField(max_length=255, blank=True, null=False, default='Отображать произвольный текст',
                                     verbose_name='Отображение цен на сайте')


class Location(models.Model):
    address = models.CharField(max_length=255, blank=True, null=False, default='Адреса нет', verbose_name='Адрес')
    gps_coordination = models.CharField(max_length=255, blank=True, null=False, default='Нет координат',
                                        verbose_name='GPS координаты')
    name = models.CharField(max_length=255, blank=True, null=False, default='Нет имени', verbose_name='Наименование')
    type_of_cooperation = models.CharField(max_length=255, blank=True, null=False, default='Нет типа сотрудничества',
                                           verbose_name='Тип сотрудничества')
    url = models.URLField(max_length=256, blank=True, null=False, default='Нет ссылки',
                          verbose_name='Ссылка на сайт партнера')
    status = models.BooleanField(blank=True, null=False, default=False, verbose_name='Статус')


class Partner(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False, default='Нет имени', verbose_name='Наименование')
    logo = models.ImageField(upload_to='logo_partner/%Y/%m/%d/', blank=True, null=True, verbose_name='Логотип партнера')
    display_order = models.IntegerField(blank=True, null=False, default=0, verbose_name='Порядок отображения')
    is_published = models.CharField(max_length=255, blank=True, null=False, default='Нет', verbose_name='Публикация')


class Review(models.Model):
    date_of_create = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    text = models.TextField(max_length=400, blank=True, null=False, default='Нет текста', verbose_name='Текст отзыва')
    grade = models.IntegerField(blank=True, null=False, default=0, verbose_name='Оценка')
    author = models.CharField(max_length=255, blank=True, null=False, default='Без автора',
                              verbose_name='ФИО и компания автора')
    picture = models.ImageField(upload_to='pic_review/%Y/%m/%d/', blank=True, null=True,
                                verbose_name='Картинка в отзыве')
    is_published = models.CharField(max_length=255, blank=True, null=False, default='Нет', verbose_name='Публикация')


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False, default='Нет имени', verbose_name='Наименование')
    date_of_create = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    is_published = models.CharField(max_length=255, blank=True, null=False, default='Нет', verbose_name='Публикация')


class ProductPhoto(models.Model):
    image = models.ImageField(upload_to='pic_review/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото товара')


class Product(models.Model):
    type = models.CharField(max_length=255, blank=True, null=False, default='Без типа', verbose_name='Тип')
    manufacturer = models.CharField(max_length=255, blank=True, null=False, default='Нет производителя',
                                    verbose_name='Производитель')
    brand = models.CharField(max_length=255, blank=True, null=False, default='Нет бренда',
                             verbose_name='Бренд/торговая марка')
    name = models.CharField(max_length=255, blank=True, null=False, default='Нет имени', verbose_name='Наименование')
    picture = models.ForeignKey("ProductPhoto", on_delete=models.PROTECT, blank=True, null=True, default=None,
                                verbose_name='Фото товара')

    video = models.FileField(upload_to='video_product/%Y/%m/%d/', null=True, blank=True, verbose_name='Видео продукта')
    description = models.CharField(max_length=255, blank=True, null=False, default='Нет описания',
                                   verbose_name='Описание товара')
    price = models.IntegerField(blank=True, null=False, default=0, verbose_name='Цена')
    tags = models.CharField(max_length=255, null=True, blank=False, default='Нет тегов', verbose_name='Мета теги')
    category = models.ForeignKey("Category", on_delete=models.PROTECT, blank=True, null=True, default=None,
                                 verbose_name='Категория')
    type_of_purchase = models.CharField(max_length=255, null=True, blank=False, default='Розница',
                                        verbose_name='Возможность приобретения')
    lot = models.CharField(max_length=255, null=True, blank=False, default='1шт',
                           verbose_name='Минимальная партия')
    payment_method = models.CharField(max_length=255, null=True, blank=False, default='Карта',
                                      verbose_name='Метод оплаты')
    standart = models.CharField(max_length=255, null=True, blank=False, default='ГОСТ',
                                verbose_name='Соответствие стандартам')
    analog = models.CharField(max_length=255, null=True, blank=False, default='УНИКАЛЕЕЕЕЕЕЕЕЕЕЕН',
                              verbose_name='Аналоги')
    is_published = models.CharField(max_length=255, blank=True, null=False, default='Нет', verbose_name='Публикация')
    import_substitution = models.BooleanField(blank=True, null=False, default=True, verbose_name='Импортозамещение')


class Case(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False, default='Нет имени', verbose_name='Наименование')
    url = models.URLField(max_length=256, blank=True, null=False, default='Нет ссылки',
                          verbose_name='Ссылка на сайт партнера/заказчика')
    type = models.CharField(max_length=255, blank=True, null=False, default='Без типа', verbose_name='Тип')
    html = models.CharField(max_length=255, blank=True, null=False, default='-', verbose_name='HTML контент')
    url_video = models.URLField(max_length=256, blank=True, null=False, default='Нет ссылки',
                                verbose_name='Ссылка на видео')
    is_published = models.CharField(max_length=255, blank=True, null=False, default='Нет', verbose_name='Публикация')
    import_substitution = models.BooleanField(blank=True, null=False, default=True, verbose_name='Импортозамещение')
