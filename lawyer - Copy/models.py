from django.db import models
from django.urls import reverse
from accounts.models import Profile
CATEGORY_CHOICES = (
    ('CRIMINAL', 'Criminal'),
    ('EMPLOYMENT', 'Employment'),
    ('CORPORATE', 'Corporate'),)
# Create your models here.


class Category(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=10, db_index=True,choices=CATEGORY_CHOICES)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    city = models.CharField(max_length=20)
#   types = models.CharField(max_length=20)
#   updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('category_name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('lawyer:lawyer_list_by_category', args=[self.slug])
    # @property
    # def get_lawyer(self):
    #     return Category.objects.filter(categories__category_name=self.category_name)


class Lawyer(models.Model):
    category = models.ForeignKey(Category, related_name='lawyer', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name='profiles', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    #city = models.CharField(max_length=200)
    #image = models.ImageField(upload_to='lawyerdp/%Y/%m/%d', blank=True)
    #types = models.CharField(max_length=20)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    #categ = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lawyer:lawyer_detail', args=[self.id, self.slug])
