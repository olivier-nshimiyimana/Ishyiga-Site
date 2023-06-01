# from django.db import models
# from time import strftime, gmtime



# # Create your models here.



# def image_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'image/{0}/{1}'.format(strftime('%Y/%m/%d'), generate_file_name() + '.' + filename.split('.')[-1])


# class ImageThumbnail(models.Model):
#     title = models.CharField(max_length=100, verbose_name="image_name")
#     description = models.TextField()
#     image = models.FileField(upload_to=image_directory_path, max_length=500)
#     vote = models.IntegerField(default=0)
#     date = models.DateTimeField(auto_now_add=True)
#     status = models.TextField(default=0)

    
#     def __str__(self):
#         return self.title
    