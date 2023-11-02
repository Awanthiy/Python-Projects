#  user's inputs
Hobby= input("Enter your hobby: ")
name = input("Enter your name: ")
age = input("Enter your age: ")
Uni = input("Enter your university: ")

# Create a story template
story = "My name is {name} . I'm {age} years old.My University is {Uni}.I like {Hobby}."

# Substitute the user's inputs into the story template
story = story.format(Hobby=Hobby,name=name,age=age,Uni=Uni)

# Print the story
print(story)
