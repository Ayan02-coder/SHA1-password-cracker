import password_cracker

def test_password_cracker():
    # Test without salts
    assert password_cracker.password_cracker('b305921a3723cd5d70a375cd21a61e60aabb84ec') == "sammy123"
    assert password_cracker.password_cracker('c7ab388a5ebefbf4d550652f1eb4d833e5316e3e') == "abacab"
    assert password_cracker.password_cracker('5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8') == "password"

    # Test with salts
    assert password_cracker.password_cracker('53d8b3dc9d39f0184144674e310185e41a87ffd5', use_salts=True) == "superman"
    assert password_cracker.password_cracker('da5a4e8cf89539e66097acd2f8af128acae2f8ae', use_salts=True) == "q1w2e3r4t5"
    assert password_cracker.password_cracker('ea3f62d498e3b98557f9f9cd0d905028b3b019e1', use_salts=True) == "bubbles1"

   print("All tests passed!")

if __name__ == "__main__":
    test_password_cracker()
