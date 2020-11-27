from blog_post import Blog_post

class Blog:
    def __init__(self):
        self.blog_posts = []

    def add(self, blog_post):
        self.blog_posts.append(blog_post)
        return blog_post

    def delete(self, num):
        for i, v in enumerate(self.blog_posts): 
            if (i+1) == num:
                self.blog_posts.remove(v)
                
    def update(self, num, BlogPost):
        for i, v in enumerate(self.blog_posts): 
            if (i+1) == num:
                self.blog_posts[i] = BlogPost

    def get_blog(self):
        return self.blog_posts



