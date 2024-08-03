import password_cracker
from unittest import main

print("\n--------- SHA-1 Password Cracker ---------")


cracked_password1 = password_cracker.crack_password(
    "b305921a3723cd5d70a375cd21a61e60aabb84ec")
print(cracked_password1)
cracked_password2 = password_cracker.crack_password(
    "c7ab388a5ebefbf4d550652f1eb4d833e5316e3e")
print(cracked_password2)
cracked_password3 = password_cracker.crack_password(
    "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")
print(cracked_password3)

# using salts
'''
cracked_password4 = password_cracker.crack_password(
    "53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True) == "superman"
print(cracked_password4)

cracked_password4 = password_cracker.crack_password(
    "da5a4e8cf89539e66097acd2f8af128acae2f8ae", use_salts=True) == "q1w2e3r4t5"
print(cracked_password4)

cracked_password4 = password_cracker.crack_password(
    "ea3f62d498e3b98557f9f9cd0d905028b3b019e1", use_salts=True) == "bubbles1"
print(cracked_password4)
'''

def user_input_password_cracker():
    """Allow user to input hash and optionally use salts."""
    hashed_password = raw_input("Enter the SHA-1 hashed password: ")
    use_salts = raw_input("Use salts? (yes/no): ").strip().lower() == 'yes'
    cracked_password = password_cracker.crack_password(hashed_password, use_salts)
    print "Cracked password for hash '{}' with salts={}: {}".format(hashed_password, use_salts, cracked_password)

if __name__ == "__main__":
    # Run the pre-defined tests
    #test_passwords()
    
    # Allow user to input a password hash and crack it
    user_input_password_cracker()
    
    # Run unittests
    main(module='test_module', exit=False)


