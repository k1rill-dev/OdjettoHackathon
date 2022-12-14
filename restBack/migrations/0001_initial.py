# Generated by Django 4.1.2 on 2022-10-22 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_price', models.CharField(blank=True, default='Отображать произвольный текст', max_length=255, verbose_name='Отображение цен на сайте')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Нет имени', max_length=255, verbose_name='Наименование')),
                ('date_of_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('is_published', models.CharField(blank=True, default='Нет', max_length=255, verbose_name='Публикация')),
                ('moderation_passed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прошло ли модерацию')),
                ('moder_comment', models.CharField(blank=True, default='Комментарий отсутствует', max_length=255, null=True, verbose_name='Комментарий от модератора')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Exponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Нет имени', max_length=180, verbose_name='Наименование экспонента')),
                ('description', models.CharField(blank=True, default='Нет описания', max_length=255, verbose_name='Описание экспонента')),
                ('title', models.CharField(default='Test', max_length=255, verbose_name='Meta title')),
                ('meta_keywords', models.CharField(default='Нет мета-ключевых слов', max_length=255, verbose_name='Meta ключевые слова')),
                ('meta_description', models.CharField(default='Нет мета-описания', max_length=255, verbose_name='Meta описание')),
                ('about_company', models.CharField(blank=True, default='Нет истории компании', max_length=355, verbose_name='О компании')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_exp/%Y/%m/%d/', verbose_name='Логотип компании')),
                ('main_picture', models.ImageField(blank=True, default='Нет картинки', null=True, upload_to='main_picture_exp/%Y/%m/%d/', verbose_name='Главное изображение')),
                ('fio_contact', models.CharField(blank=True, default='Нет контактного лица', max_length=255, verbose_name='ФИО контактного лица')),
                ('inn_exponent', models.BigIntegerField(blank=True, unique=True, verbose_name='ИНН экспонента')),
                ('urid_address', models.CharField(blank=True, default='Нет адреса', max_length=255, verbose_name='Юридический адрес')),
                ('prod_address', models.CharField(blank=True, default='Нет адреса', max_length=255, verbose_name='Адрес производства')),
                ('import_substitution', models.BooleanField(blank=True, default=True, verbose_name='Импортозамещение')),
                ('moderation_passed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прошло ли модерацию')),
                ('moder_comment', models.CharField(blank=True, default='Комментарий отсутствует', max_length=255, null=True, verbose_name='Комментарий от модератора')),
                ('catalog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='restBack.catalog', verbose_name='Каталог компании')),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='restBack.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Экспонент',
                'verbose_name_plural': 'Экспоненты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, default='Без типа', max_length=255, verbose_name='Тип(товар/услуга)')),
                ('manufacturer', models.CharField(blank=True, default='Нет производителя', max_length=255, verbose_name='Производитель')),
                ('brand', models.CharField(blank=True, default='Нет бренда', max_length=255, verbose_name='Бренд/торговая марка')),
                ('name', models.CharField(blank=True, default='Нет имени', max_length=255, verbose_name='Наименование')),
                ('video', models.FileField(blank=True, null=True, upload_to='video_product/%Y/%m/%d/', verbose_name='Видео продукта')),
                ('description', models.CharField(blank=True, default='Нет описания', max_length=255, verbose_name='Описание товара')),
                ('price', models.IntegerField(blank=True, default=0, verbose_name='Цена')),
                ('tags', models.CharField(default='Нет тегов', max_length=255, null=True, verbose_name='Мета теги')),
                ('type_of_purchase', models.CharField(default='Розница', max_length=255, null=True, verbose_name='Возможность приобретения')),
                ('lot', models.CharField(default='1шт', max_length=255, null=True, verbose_name='Минимальная партия')),
                ('payment_method', models.CharField(default='Карта', max_length=255, null=True, verbose_name='Метод оплаты')),
                ('standart', models.CharField(default='ГОСТ', max_length=255, null=True, verbose_name='Соответствие стандартам')),
                ('analog', models.CharField(default='УНИКАЛЕЕЕЕЕЕЕЕЕЕЕН', max_length=255, null=True, verbose_name='Аналоги')),
                ('is_published', models.CharField(blank=True, default='Нет', max_length=255, verbose_name='Публикация')),
                ('import_substitution', models.BooleanField(blank=True, default=True, verbose_name='Импортозамещение')),
                ('moderation_passed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прошло ли модерацию')),
                ('moder_comment', models.CharField(blank=True, default='Комментарий отсутствует', max_length=255, null=True, verbose_name='Комментарий от модератора')),
                ('catalog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='restBack.catalog', verbose_name='Каталог')),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='restBack.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('text', models.TextField(blank=True, default='Нет текста', max_length=400, verbose_name='Текст отзыва')),
                ('grade', models.IntegerField(blank=True, default=0, verbose_name='Оценка')),
                ('author', models.CharField(blank=True, default='Без автора', max_length=255, verbose_name='ФИО и компания автора')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pic_review/%Y/%m/%d/', verbose_name='Картинка в отзыве')),
                ('is_published', models.CharField(blank=True, default='Нет', max_length=255, verbose_name='Публикация')),
                ('moderation_passed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прошло ли модерацию')),
                ('moder_comment', models.CharField(blank=True, default='Комментарий отсутствует', max_length=255, null=True, verbose_name='Комментарий от модератора')),
                ('exponent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='restBack.exponent', verbose_name='Экспонент')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Нет имени', max_length=255, verbose_name='Наименование')),
                ('type', models.CharField(blank=True, default='Без типа', max_length=255, verbose_name='Тип')),
                ('is_published', models.CharField(blank=True, default='Нет', max_length=255, verbose_name='Публикация')),
                ('date_of_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('moderation_passed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прошло ли модерацию')),
                ('moder_comment', models.CharField(blank=True, default='Комментарий отсутствует', max_length=255, null=True, verbose_name='Комментарий от модератора')),
                ('exponent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='restBack.exponent', verbose_name='Экспонент')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pic_review/%Y/%m/%d/', verbose_name='Фото товара')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='restBack.product', verbose_name='Сам товар')),
            ],
            options={
                'verbose_name': 'Фото продукта',
                'verbose_name_plural': 'Фото продукта',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Нет имени', max_length=255, verbose_name='Наименование')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_partner/%Y/%m/%d/', verbose_name='Логотип партнера')),
                ('display_order', models.IntegerField(blank=True, default=0, verbose_name='Порядок отображения')),
                ('is_published', models.CharField(blank=True, default='Нет', max_length=255, verbose_name='Публикация')),
                ('exponent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='restBack.exponent', verbose_name='Экспонент')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='Адреса нет', max_length=255, verbose_name='Адрес')),
                ('gps_coordination', models.CharField(blank=True, default='Нет координат', max_length=255, verbose_name='GPS координаты')),
                ('name', models.CharField(blank=True, default='Нет имени', max_length=255, verbose_name='Наименование')),
                ('type_of_cooperation', models.CharField(blank=True, default='Нет типа сотрудничества', max_length=255, verbose_name='Тип сотрудничества')),
                ('url', models.URLField(blank=True, default='Нет ссылки', max_length=256, verbose_name='Ссылка на сайт партнера')),
                ('status', models.BooleanField(blank=True, default=False, verbose_name='Статус')),
                ('moderation_passed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прошло ли модерацию')),
                ('moder_comment', models.CharField(blank=True, default='Комментарий отсутствует', max_length=255, null=True, verbose_name='Комментарий от модератора')),
                ('exponent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='restBack.exponent', verbose_name='Экспонент')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
        ),
        migrations.AddField(
            model_name='catalog',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='restBack.category', verbose_name='Категория'),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Нет имени', max_length=255, verbose_name='Наименование')),
                ('url', models.URLField(blank=True, default='Нет ссылки', max_length=256, verbose_name='Ссылка на сайт партнера/заказчика')),
                ('type', models.CharField(blank=True, default='Без типа', max_length=255, verbose_name='Тип')),
                ('html', models.CharField(blank=True, default='-', max_length=255, verbose_name='HTML контент')),
                ('url_video', models.URLField(blank=True, default='Нет ссылки', max_length=256, verbose_name='Ссылка на видео')),
                ('is_published', models.CharField(blank=True, default='Нет', max_length=255, verbose_name='Публикация')),
                ('import_substitution', models.BooleanField(blank=True, default=True, verbose_name='Импортозамещение')),
                ('moderation_passed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прошло ли модерацию')),
                ('moder_comment', models.CharField(blank=True, default='Комментарий отсутствует', max_length=255, null=True, verbose_name='Комментарий от модератора')),
                ('exponent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='restBack.exponent', verbose_name='Экспонент')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('exponent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restBack.exponent')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
