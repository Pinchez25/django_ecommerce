from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField


# Create your models here.
class Category(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',
                                 verbose_name=_('category'))
    title = models.CharField(_('Product Name'), max_length=100)
    slug = AutoSlugField(populate_from='title')
    image = ImageField(_('Image'), default='default.png', upload_to='products')
    description = models.TextField(_('description'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))
    available = models.BooleanField(default=True, verbose_name=_('available'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # get the url of the sorl thumbnail image
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return ''

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created', ]
        verbose_name = _("Product")
        verbose_name_plural = _('Products')
