import wikipedia 

# Syntax : wikipedia.summary(title, sentences)
result = wikipedia.summary("India", sentences = 2) 
print(result) 

# Syntax : wikipedia.search(title, results)
result = wikipedia.search("Geek", results = 5)
print(result)

# Syntax : wikipedia.page(title)
page_object = wikipedia.page("india")
print(page_object.html) # printing html of page_object
print(page_object.original_title) # printing title
print(page_object.links[0:10]) # printing links on that page object

# Syntax : wikipedia.set_lang(language)
wikipedia.set_lang("hi") # setting language to hindi
print(wikipedia.summary("India"))
