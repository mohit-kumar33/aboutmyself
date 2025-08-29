import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
print("This is the first project of our team.\n So this AI is very limited.\nlike (calculator,greetings,writing articals)")

# First user intraction keywords
first_user_greeting = ["hello","hlo","hloo","hi","how are you","what's up?","what's up","hey there","hello there","heyyy",
                       "hey"]

# Timing based greetings keywords
first_user_greeting_timiming = ["good morning","good afternoon","good evening","good night"]

#  Answers for first user intraction 
first_user_greeting_answer = ["Hello\nHow are you?\nHow can i help you?","Hlo\nHow are you?\nHow can i help you?","Hloo\nHow are you?\nHow can i help you?","Hello\nHow are you?\nHow can i help you?","I am fine.\n and you?\nHow can i help you?","what's up.\nHow can i help you today?",
                              "what's up.\n and you?\nHow can i help you?","Hello there\nHow are you?\nHow can i help you?","Hello there\nHow are you?\nHow can i help you?","Hello\nHow are you?\nHow can i help you?","Hello\nHow are you?\nHow can i help you?",]

# Answers for first user intraction based on timing
first_user_greeting_timiming_answer = ["Good Morning\nHow can i help you today?","Good Afternoon\nHow can i help you today?","Good Evening\nHow can i help you today?","Good Night!\nSee you soon."]

# For performing calculations
calculator_list = ["calculate","add","multiply","divide"]
def calculator(first,second,operator):
    if operator == "*":
        print(first*second)
    elif operator == "/" and second!= 0:
        print(first/second)
    elif operator == "/" and second == 0:
        print("Not Defined!")
    elif operator == "+":
        print(first + second)
    elif operator == "-":
        print(first-second)

# For greeting answers
def greetings():
    if user_input in first_user_greeting:
        print(first_user_greeting_answer[first_user_greeting.index(user_input)])

# For artical writing
wiki_key = ["write","print","article","assay"]
def wiki_article(topic):
    try:
        # Set language to English (change to 'hi' for Hindi)
        wikipedia.set_lang("en")
        
        # Get full page content
        page = wikipedia.page(topic)
        content = page.content

        # Trim to approx 500 words
        words = content.split()
        trimmed = " ".join(words[:500])

        # Format output
        article = f"**Article on: {page.title}**\n\n{trimmed}\n\n Source: {page.url}"
        print(article)

    except DisambiguationError as e:
        print(f"Ambiguous topic. Did you mean one of these?\n{', '.join(e.options[:5])}")

    except PageError:
        print("Page not found. Try a different topic.")

    except Exception as e:
        print(f"Unexpected error: {str(e)}")

while True:
    user_input = input("How can i help you sir: ").lower()
    user_input_list = user_input.split()
    if user_input=="exit":
        break
    else:
        for i in user_input_list:
            if i in first_user_greeting:
                greetings()
                continue
            elif i in calculator_list:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                opr = input("Enter the operator:")
                calculator(num1,num2,opr)
                continue
            elif i in wiki_key:
                name = input("Enter the topic name : ")
                wiki_article(name)
                
