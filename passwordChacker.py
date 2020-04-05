userName = input("user name: ")
password = input("password: ")

print(f"""
Hello {userName}, 
your {'*' * len(password)} is {len(password)} characters long
""")