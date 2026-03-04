from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


# from PIL import Image


def check_condition(value):
    if value < 0:
        raise ValidationError("Qabul qilinayotgan son manfiy bo'la olmaydi!")


def staff_photo_dimensions(photo):
    w, h = get_image_dimensions(photo)

    if not photo:
        raise ValidationError('Rasmni kiring!')

    else:
        if w / h != 0.75:
            raise ValidationError("Kiritilayotgan foto ning o'lchami nisbati 3x4 bo'lishi kerak")


class StaffModel(models.Model):  # DONE!
    main_title = models.CharField('Ismi ', max_length=64, help_text="Hodimning ismi")
    title = models.CharField('Vazifasi ', max_length=64, help_text="Hodimning vazifasi")
    photo = models.ImageField('Foto rasmi ', upload_to="Staff", validators=[staff_photo_dimensions],
                              help_text="Hodimning foto rasmi (o'lcahmi 3x4 nisbatda bo'lgan rasmni kiriting)")
    info = models.TextField("Ma'lumot", blank=True, null=True, help_text="Hodim haqida ma'lumot yoki habar")
    twitter = models.URLField('Twitter linki ', max_length=200, blank=True, null=True,
                              help_text="Hodimning twitterdagi profilidagi linki mavjud bo'lmasa bo'sh qoldiring")
    facebook = models.URLField('Facebook linki ', max_length=200, blank=True, null=True,
                               help_text="Hodimning facebookdagi profilidagi linki mavjud bo'lmasa bo'sh qoldiring")
    instagram = models.URLField('Instagram linki ', max_length=200, blank=True, null=True,
                                help_text="Hodimning instagramdagi profilidagi linki mavjud bo'lmasa bo'sh qoldiring")
    linkedin_box = models.URLField('linkedin-box linki ', max_length=200, blank=True, null=True,
                                   help_text="Hodimning linkedin_box profilidagi linki mavjud bo'lmasa bo'sh qoldiring")
    created_at = models.DateTimeField('Kiritilgan vaqti', auto_now_add=True, null=True)
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    # admin_object = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Hodimlar"
        verbose_name_plural = "Hodimlar"


class AboutChildrenModel(models.Model):  # DONE!
    name_of_first_table = models.CharField('Jadvalning nomini kiriting ', blank=True, null=True, max_length=24,
                                           default="Nimadir",
                                           help_text="Birinchi statistik ma'lumotning nomi")

    num_of_first_table = models.IntegerField('Jadvaldagi sonni kiriting ', default=0, blank=True, null=True,
                                             validators=[check_condition],
                                             help_text="Birinchi statistik ma'lumotning soni")

    name_of_second_table = models.CharField('Jadvalning nomini kiriting ', blank=True, null=True, max_length=24,
                                            default="Nimadir",
                                            help_text="Ikkinchi statistik ma'lumotning nomi")

    num_of_second_table = models.IntegerField('Jadvalning sonni kiriting ', default=0, blank=True, null=True,
                                              validators=[check_condition],
                                              help_text="Ikkinchi statistik ma'lumotning soni")

    name_of_third_table = models.CharField('Jadvalning nomini kiriting ', blank=True, null=True, max_length=24,
                                           default="Nimadir",
                                           help_text="Uchinchi statistik ma'lumotning nomi")

    num_of_third_table = models.IntegerField('Jadvalning sonni kiriting ', default=0, blank=True, null=True,
                                             validators=[check_condition],
                                             help_text="Uchinchi statistik ma'lumotning soni")

    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self): 
        return ""

    class Meta:
        verbose_name = "Statistik ma'lumotlar"
        verbose_name_plural = "Statistik ma'lumotlar"


class NewsModel(models.Model):  # DONE!
    image = models.ImageField('Yangilikning rasmi ', upload_to="Yangiliklar", help_text="Yangiliklardagi rasm")
    title = models.CharField('Yangilikning nomi ', max_length=45, help_text="Yangilikdagi mavzuning nomi")
    message = models.TextField('Yangilikdagi habar ', help_text="Yangilikdagi o'zgarishlardagi habarlar")

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
        return ""

    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"


class GalaryModel(models.Model):  # DONE 100%
    photo = models.ImageField('Gallereya rasmi ', upload_to="Gallereya",
                              help_text="Gallereyadagi rasm (Bolalar rasmi, Bog'chaning rasmi ...)")
    main_title = models.CharField('Gallereyadagi assosiy mavzu ', blank=False, max_length=32,
                                  help_text="Gallereyadagi assosiy mavzuning nomi")
    title = models.CharField('Gallereyadagi mavzu ', max_length=32, null=True, blank=True,
                             help_text="Gallereydagi ma'lumot (Gallereyadagi mavzu lekin assosiysi emas)")
    message = models.TextField('Gallereyadagi habar ', blank=True, null=True,
                               help_text="Gallereyadagi habarlar (Gallereyada ma'lumotni yozmasez, bo'sh qoldiring)")
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
        return ""

    class Meta:
        verbose_name = "Gallereya"
        verbose_name_plural = "Gallereya"


class ContactModel(models.Model):  # DONE! 100%
    location = models.TextField('Manzil ', help_text="Bog'chaning manzili")
    email = models.EmailField('Email manzilingiz ', help_text="Bog'chaning emaili")
    contact_num = models.CharField('Kontakt raqam ', max_length=32,
                                   help_text="Bog'chaning kontakt raqami (Aloqaga kirib bo'ladigan raqam)")
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontakt"


class BannerModel(models.Model):
    banner_main_title = models.CharField('Bannerning nomi ', max_length=48, null=True,
                                         help_text="Bannerdagi mavzu yoki uning nomi")  # APPROX 48
    banner_message_on_title = models.TextField("Bannerdagi ma'lumot", max_length=216, null=True, blank=True,
                                               help_text="Bannerdagi ma'lumot mavjud bo'lmasa bo'sh qoldiring")
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banner"


class Customer(models.Model):  # it is not ready yet totally but we can get answer!!
    name = models.CharField('Ismi ', max_length=120, help_text="Habar yuboruvchining ismi")
    phone_number = models.CharField('Telefon-raqami ', max_length=13, help_text="Habar yuboruvchining telefon raqami")
    message = models.TextField('Xabar ', max_length=1500, help_text="Habar yuboruvchining habari (yuborgan ma'lumoti)")
    created_at = models.DateTimeField('Kiritilgan vaqti', auto_now_add=True, null=True)
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Xabarlar"
        verbose_name_plural = "Xabarlar"

# ALL OF THEM AT THE ABOVE GET METHOD
