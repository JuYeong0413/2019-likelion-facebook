from django.db import models
from imagekit.models import ImageSpecField #썸네일만드는거
from imagekit.processors import ResizeToFill #크기조정 추가


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(upload_to='image', blank=True)
    comment_count = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 여기에서 Post의 key 를 갖고있는 comments 들을 불러오는 메서드를 만들거에요
    # 이렇게 하면 item.comments 하면 Post의 comments 들을 다 불러올 수 있어요
    # 이제 이걸 newsfeed.html 에서 바로 쓰면 돼요! 
    def comments(self):
        return Comment.objects.filter(post=self)

    
    # def add_comment(self):
    #     num = Post.objects.values('comment_count')
    #     num = num + 1
    #     return self.update(comment_count=num)
        


class Comment(models.Model):
    writer = models.CharField(max_length=200)
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete="CASCADE")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)