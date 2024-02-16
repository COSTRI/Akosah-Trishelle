current_users = ['ama', 'kofi', 'yaw', 'akua', 'yaa']
new_users = ['ama', 'charles', 'yaw', 'cynthia', 'nana']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
           print(f"The username '{user}' is not available. Please enter a new name ")
    else:
          print(f" the username '{user}' is available")



for num in range(1,101):
      if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz")
      elif num % 3 == 0:
            print("fizz")
      elif num % 5 == 0:
            print("buzz")
      else:
            print(num)