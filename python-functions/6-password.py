def validate_password(password):
    SpecialSym =['$', '@', '#', '%']
    if len(password)<8:
        print(False)
        if not any(char.isdigit()for char in password):
            print(False)
            if not any(char.isupper() for char in password):
                print(False)
                if not any(char in SpecialSym for char in password):
                    print(False)

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))