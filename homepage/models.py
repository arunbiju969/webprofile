from django.db import models
from django.utils.translation import gettext_lazy as _

class SiteTitle(models.Model):
    title = models.CharField(_("NavBar-Title"), max_length=50)
    page_title = models.CharField(_("Page-Title"), max_length=50)
    

    class Meta:
        verbose_name = _("Site Title")
        verbose_name_plural = _("1. Site Title")

    def __str__(self):
        return self.page_title


class About(models.Model):
    title = models.CharField(_("About Page Title"), max_length=50)
    details = models.TextField(_("Profile Details"))
    profle_photo = models.ImageField(upload_to='about_page')

    class Meta:
        verbose_name_plural = '2. About'

    def __str__(self):
        return f'{self.title}'

class Projects(models.Model):
    title = models.CharField(_("Projects Page Title"), max_length=50)
    details = models.TextField(_("Projects Details"))
    cat_one_heading = models.CharField(_("Category One Heading"), max_length=50)
    cat_two_heading = models.CharField(_("Category Two Heading"), max_length=50)
    cat_three_heading = models.CharField(_("Category Three Heading"), max_length=50)
    
    class Meta:
        verbose_name = _("Projects")
        verbose_name_plural = _("3. Projects")

    def __str__(self):
        return self.title

class CatOneCards(models.Model):
    card_title = models.CharField(_("Card Title"), max_length=50)
    card_image = models.ImageField(_("Card Image"), upload_to='projects_page')
    excerpt = models.CharField(_("Card Exerpt"), max_length=50)
    button_one_name = models.CharField(_("Button One"), max_length=50, default='Button 1')
    button_two_name = models.CharField(_("Button two"), max_length=50, default='Button 2')
    link_1 = models.TextField(_("Link one"),default='#')
    link_2 = models.TextField(_("Link two"),default='#')
    

    class Meta:
        verbose_name = _("Category One Card")
        verbose_name_plural = _("3.1 Category One Cards")

    def __str__(self):
        return self.card_title

class CatTwoCards(models.Model):
    card_title = models.CharField(_("Card Title"), max_length=50)
    card_image = models.ImageField(_("Card Image"), upload_to='projects_page')
    excerpt = models.CharField(_("Card Exerpt"), max_length=50)
    button_one_name = models.CharField(_("Button One"), max_length=50,default='Button 1')
    button_two_name = models.CharField(_("Button two"), max_length=50,default='Button 2')
    link_1 = models.TextField(_("Link one"),default='#')
    link_2 = models.TextField(_("Link two"),default='#')

    class Meta:
        verbose_name = _("Category Two Card")
        verbose_name_plural = _("3.2 Category Two Cards")

    def __str__(self):
        return self.card_title

class CatThreeCards(models.Model):
    card_title = models.CharField(_("Card Title"), max_length=50)
    card_image = models.ImageField(_("Card Image"), upload_to='projects_page')
    excerpt = models.CharField(_("Card Exerpt"), max_length=50)
    button_one_name = models.CharField(_("Button One"), max_length=50,default='Button 1')
    button_two_name = models.CharField(_("Button two"), max_length=50,default='Button 2')
    link_1 = models.TextField(_("Link one"),default='#')
    link_2 = models.TextField(_("Link two"),default='#')
    

    class Meta:
        verbose_name = _("Category Three Card")
        verbose_name_plural = _("3.3 Category Three Cards")

    def __str__(self):
        return self.card_title

class Certificates(models.Model):
    title = models.CharField(_("Certificate Title"), max_length=50)
    image = models.ImageField(_("Certififcate Image"), upload_to='certificate_page')
    link = models.TextField(_("Verification Link"))

    
    class Meta:
        verbose_name = _("Certificates")
        verbose_name_plural = _("4. Certificates")

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    icon = models.ImageField(_("Icon"), upload_to='contact_page')
    dark_icon = models.ImageField(_("Dark_Icon"), upload_to='contact_page')
    link = models.TextField(_("Social Link"))
    

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("5. Contacts")

    def __str__(self):
        return self.title
