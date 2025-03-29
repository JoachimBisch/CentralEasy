from django.db import models

class Service(models.Model):
    image_path = models.CharField(max_length=200, default="img/no-image-available.jpg")  # Chemin vers l'image
    category = models.CharField(max_length=100, default="Autre")
    title = models.CharField(max_length=100)
    stars = models.IntegerField(default=0)  # Peut-être changer en FloatField si vous utilisez un système d'évaluation par étoiles
    short_description = models.CharField(max_length=400)
    long_description = models.TextField()
    service_url = models.URLField(max_length=200, blank=True, null=True)  # Champ URL
    order = models.IntegerField(default=0)  # Champ pour spécifier l'ordre des services
    category_order = models.IntegerField(default=0)  # Champ pour spécifier l'ordre des catégories


    def get_stars_html(self):
        full_stars = self.stars // 1
        half_star = self.stars % 1 > 0
        empty_stars = 5 - full_stars - half_star

        stars_html = '<div class="stars">'
        for _ in range(full_stars):
            stars_html += '<span class="fas fa-star"></span>'
        if half_star:
            stars_html += '<span class="fas fa-star-half-alt"></span>'
        for _ in range(empty_stars):
            stars_html += '<span class="far fa-star"></span>'
        stars_html += '</div>'

        return stars_html

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        return '/static/' + self.image_path