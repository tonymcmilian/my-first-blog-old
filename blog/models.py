from django.db import models
from django.utils import timezone


# Definizione del modello Post.
# models.Model significa che il Post è un modello Django,
# quindi Django sa che dovrebbe essere salvato nel database. 

class Post(models.Model):
    # Definiamo ora le proprieta della classe Post
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) 
    text = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)

    # Definiamo il metodo di pubblicazione del Posts
    def pulish(self):
        self.publisched_date = timezone.now()
        self.save

    def __str__(self):
        return self.title
    
