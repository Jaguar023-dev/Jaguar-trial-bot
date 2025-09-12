```
AI Chat Program
Function to handle user input
def get_user_input():
  return input("You: ")
Function to generate response
def generate_response(user_input):
  responses = {
    "hello": "Hello, how are you?",
    "how are you": "I'm great, thanks for asking!",
    "what is your name": "My name is Jaguar."
  }
  return responses.get(user_input.lower(), "I didn't understand.")
Main program loop
while True:
  user_input = get_user_input()
  response = generate_response(user_input)
  print("Jaguar:", response)
```
