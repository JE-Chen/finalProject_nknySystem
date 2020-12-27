import JEVerificationCode

g = JEVerificationCode.GenerateVerificationCode()
Code = g.generate_base64_image(5, 40, True)
print(Code[0])
print(Code[1])

print(g.generate_code_only_string(5))
