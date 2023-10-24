# i don't feel like typing out the variable, pretty simple exercise
# This is a code snippet, it does not work

# try except if a key is called and it doesn't exist assign a default value to that key

facebook_posts = [{"key": "value"}]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post['likes']
    except KeyError:
        # Either pass or initalize a key for that nested list, i choose pass
        pass
print(total_likes)
