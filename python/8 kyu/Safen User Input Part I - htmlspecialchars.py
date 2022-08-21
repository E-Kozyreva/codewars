# You are a(n) novice/average/experienced/professional/world-famous Web Developer (choose one) 
# who owns a(n) simple/clean/slick/beautiful/complicated/professional/business website 
# (choose one or more) which contains form fields so visitors can send emails or leave a comment on your website with ease. 

# Your mission is to implement a function that converts the following potentially harmful characters:
# < --> &lt;
# > --> &gt;
# " --> &quot;
# & --> &amp;

def html_special_chars(data): 
    characters = {"<": "&lt;", ">": "&gt;",
                  '"': "&quot;", "&": "&amp;", }
    new_data = ""
    for char in data:
        if char in characters.keys():
            new_data += characters[char]
        else:
            new_data += char
    return new_data
