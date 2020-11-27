from blog_post import Blog_post
from blog import Blog


blog1 = Blog_post("John Doe" , "Lorem Ipsum" , "Lorem ipsum dolor sit amet.", "2000.05.04.")

blog2= Blog_post("Tim Urban","Wait but why", "A popular long-form, stick-figure-illustrated blog about almost everything.", "2010.10.10.")

blog3 = Blog_post("William Turton","One Engineer Is Trying to Get IBM to Reckon With Trump", "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.", "2017.03.28.")

blog = Blog()

blog.add(blog1)
blog.add(blog2)
blog.add(blog3)

print(len(blog.blog_posts))

blog.delete(2)

print(len(blog.blog_posts))
print(repr(blog.blog_posts))
