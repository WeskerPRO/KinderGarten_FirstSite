from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


# from PIL import Image


def check_condition(value):
    if value < 0:
        raise ValidationError('Kirityotgan raqamingiz manfiy bo"la olmaydi!')


def staff_photo_dimensions(photo):
    w, h = get_image_dimensions(photo)
    condition_x = 600
    condition_y = 600

    if not photo:
        raise ValidationError('Fotoni kiring!')

    else:
        if w != condition_x:
            raise ValidationError('Kiritilayotgan foto ning o"lchami %i piksel bo"lishi kerak' % condition_x)

        if h != condition_y:
            raise ValidationError('Kiritilayotgan foto ning o"lchami %i piksel bo"lishi kerak' % condition_y)


def news_photo_dimensions(photo):
    w, h = get_image_dimensions(photo)
    condition_x = 300
    condition_y = 400

    if not photo:
        raise ValidationError('Fotoni kiring!')
    else:
        if w > condition_x:
            raise ValidationError('Kiritilayotgan foto ning o"lchami %i piksel bo"lishi kerak' % condition_x)

        if h > condition_y:
            raise ValidationError('Kiritilayotgan foto ning o"lchami %i piksel bo"lishi kerak' % condition_y)


def galary_photo_dimensions(photo):
    w, h = get_image_dimensions(photo)
    condition_x = 600
    condition_y = 600

    if not photo:
        raise ValidationError('Fotoni kiring!')
    else:
        if w > condition_x:
            raise ValidationError('Kiritilayotgan foto ning o"lchami %i piksel bo"lishi kerak' % condition_x)

        if h > condition_y:
            raise ValidationError('Kiritilayotgan foto ning o"lchami %i piksel bo"lishi kerak' % condition_y)


class MakeSingleModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(MakeSingleModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class StaffModel(models.Model):  # DONE!
    main_title = models.CharField('Ismi ', max_length=64)
    title = models.CharField('Vazifasi ', max_length=64)
    photo = models.ImageField('Foto rasmi ', upload_to="Staff", validators=[staff_photo_dimensions],
                              help_text="O'lcahmi 3x4 bo'lgan rasmni kiriting!")
    info = models.TextField('Ma"lumot ', blank=True, null=True)
    twitter = models.CharField('Twitter linki (shart emas) ', max_length=200, blank=True, null=True)
    facebook = models.CharField('Facebook linki (shart emas) ', max_length=200, blank=True, null=True)
    instagram = models.CharField('Instagram linki (shart emas) ', max_length=200, blank=True, null=True)
    linkedin_box = models.CharField('linkedin-box linki (shart emas) ', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField('Kiritilgan vaqti', auto_now_add=True, null=True)
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    # admin_object = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = "Adminlar ma'lumoti"
        verbose_name_plural = "Adminlar ma'lumoti"


class AboutChildrenModel(MakeSingleModel):  # DONE!
    name_of_first_table = models.CharField('Birinchi jadvalning nomini kiriting ', blank=True, null=True, max_length=24,
                                           default="Nimadir")
    num_of_first_table = models.IntegerField('Birinchi jadvaldagi sonni kiriting ', default=0, blank=True, null=True,
                                             validators=[check_condition])
    name_of_second_table = models.CharField('Ikkinchi jadvalning nomini kiriting ', blank=True, null=True,
                                            max_length=24,
                                            default="Nimadir")
    num_of_second_table = models.IntegerField('Ikkinchi jadvalning sonni kiriting ', default=0, blank=True, null=True,
                                              validators=[check_condition])
    name_of_third_table = models.CharField('Uchinchi jadvalning nomini kiriting ', blank=True, null=True, max_length=24,
                                           default="Nimadir")
    num_of_third_table = models.IntegerField('Uchinchi jadvalning sonni kiriting ', default=0, blank=True, null=True,
                                             validators=[check_condition])

    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return "Shaxsiy ma'lumot"

    class Meta:
        verbose_name = "Shaxsiy ma'lumot"
        verbose_name_plural = "Shaxsiy ma'lumot"


class NewsModel(models.Model):  # DONE!
    image = models.ImageField('Foto rasmi ', upload_to="Yangiliklar", validators=[news_photo_dimensions],
                              help_text="Rasmni 300x400 darajasida joylashtiring")
    title = models.CharField('Jadvalning nomi ', max_length=45)
    message = models.TextField('Jadvaldagi habar ')

    '''
    InputChoice = [
        ("bx-news", "news"), ("bx-alarm", "alarm"), ("bx-award", "award"), ("bx-broadcast", "broadcast"),
        ("bx-bi-hand-index", "hand_index"), ("bx-gift", "gift"), ("bxs-hourglass-top", "hour_glass_top"),
        ("bxs-hourglass-bottom", "hour_glass_bottom"), ("bi-question-circle", "question"),
        ("bi-telephone-fill", "telephone"), ("bi-telegram", "telegram")
    ]
    

    choice = models.CharField('Type of news ', choices=InputChoice, default="bx-news", max_length=64, blank=False,
                              null=True)
    '''

    created_at = models.DateTimeField('Kiritilgan vaqti', auto_now_add=True, null=True)
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"


class GalaryModel(models.Model):  # DONE 100%
    photo = models.ImageField('Jadvalning rasmi ', upload_to="Gallereya", validators=[galary_photo_dimensions])
    main_title = models.CharField('Jadvalning nomi ', blank=False, max_length=32)
    title = models.CharField("Jadvaldagi ma'lumot ", max_length=32, null=True, blank=True)
    message = models.TextField('Jadvaldagi habar ', blank=True, null=True)
    created_at = models.DateTimeField('Kiritilgan vaqti', auto_now_add=True, null=True)
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    '''
    RealCharChoices = [
        ("web", "all photos"),
        ("app", "main-list"),
        ("card", "garden-list")
    ]
    '''

    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = "Surat"
        verbose_name_plural = "Suratlar"


class ContactModel(MakeSingleModel):  # DONE! 100%
    location = models.TextField('Manzil ')
    email = models.EmailField('Email manzilingiz ')
    contact_num = models.CharField('Kontakt raqam ', max_length=32)
    '''
    twitter = models.CharField('Twitter link (if exists) ', max_length=200, blank=True, null=True)
    facebook = models.CharField('Facebook link (if exists) ', max_length=200, blank=True, null=True)
    instagram = models.CharField('Instagram link (if exists) ', max_length=200, blank=True, null=True)
    skype = models.CharField('Skype link (if exists) ', max_length=200, blank=True, null=True)
    linkedin_box = models.CharField('linkedin-box link (if exists) ', max_length=200, blank=True, null=True)
    '''
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return "Contact"

    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontakt"


class BannerModel(MakeSingleModel):
    banner_main_title = models.CharField('Jadvalning nomi ', max_length=48, null=True)  # APPROX 48
    banner_message_on_title = models.TextField("Jadvaldagi ma'lumot", max_length=216, null=True, blank=True)
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banner"


class Customer(models.Model):  # it is not ready yet totally but we can get answer!!
    name = models.CharField('Ismi ', max_length=120)
    phone_number = models.CharField('Telefon-raqami ', max_length=13)
    message = models.TextField('Xabar ', max_length=1500)  # models.CharField('Message ', max_length=1500)
    created_at = models.DateTimeField('Kiritilgan vaqti', auto_now_add=True, null=True)
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Xabarlar"
        verbose_name_plural = "Xabarlar"

# ALL OF THEM AT THE ABOVE GET METHOD
