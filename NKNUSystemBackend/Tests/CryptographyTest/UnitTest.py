import unittest

import JECryptography


class Cryptography(unittest.TestCase):

    @staticmethod
    def testCryptography():
        Hash = JECryptography.Hash()
        Hash.hash_md5("12345123451234512345")
        Hash.hash_sha1("12345123451234512345")
        Hash.hash_sha224("12345123451234512345")
        Hash.hash_sha256("12345123451234512345")
        Hash.hash_sha384("12345123451234512345")
        Hash.hash_sha512("12345123451234512345")


if __name__ == '__main__':
    suite = (unittest.TestLoader().loadTestsFromTestCase(Cryptography))
    unittest.TextTestRunner(verbosity=2).run(suite)
