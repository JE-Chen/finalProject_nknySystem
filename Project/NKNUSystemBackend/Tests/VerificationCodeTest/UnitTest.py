import unittest

import JEVerificationCode


class GenerateVerification(unittest.TestCase):

    @staticmethod
    def testGenerateOnlyString():
        JEVerificationCode.GenerateVerificationCode().generate_code_only_string(5)

    @staticmethod
    def testGenerate():
        g = JEVerificationCode.GenerateVerificationCode().generate_base64_image(5, 40, True)
        print(g[0])
        print(g[1])


if __name__ == '__main__':
    suite = (unittest.TestLoader().loadTestsFromTestCase(GenerateVerification))
    unittest.TextTestRunner(verbosity=2).run(suite)
