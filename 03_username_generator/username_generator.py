#username_generator
full_name = input("Enter your full name: ")
city = input("Enter your city: ")
college_name = input("Enter your college name: ")
favorite_language = input("Enter your favourite programming language: ")
hobby = input("Enter your favourite hobby: ")
dob=int(input("Enter your date of birth (DDMMYYYY): "))

print("Personal Information:")
print("Full Name:", full_name.capitalize())
print("City:", city.capitalize())
print("College Name:", college_name.capitalize())
print("Favourite Programming Language:", favorite_language.capitalize())
print("Favourite Hobby:", hobby.capitalize())
print("Date of Birth:", dob)

print("\nGenerated Username:")
print("generating first username option:")
print("First name:", full_name.split()[0].capitalize())
print("Last name:", full_name.split()[-1].capitalize())
print("Option1:",full_name[0:-1:2].capitalize().replace(" ",""))
print("generating second username option:")
print("Option2:",full_name[0:2].capitalize().replace(" ","")+city[0:2].capitalize().replace(" ","")+college_name[0:2].capitalize().replace(" ","")+favorite_language[0:2].capitalize().replace(" ","")+hobby[0:2].capitalize().replace(" ",""))
print("generating third username option:")
print("Option3:",full_name.split()[0].capitalize()+"@"+str(dob)[-4:])

print("Check strength of generated Password:")
print("Note: A strong Password should be at least 8 characters long, contain a mix of uppercase and lowercase letters, numbers, and special characters.")

Password=(input("Enter your Password: "))
if len(Password) >= 8 and any(char.isupper() for char in Password) and any(char.islower() for char in Password) and any(char.isdigit() for char in Password) and any(not char.isalnum() for char in Password):
    print("Your Password is strong.")
else:
    print("Your Password is not strong.")

