import JECryptography

Hash = JECryptography.Hash()

if __name__ == "__main__":
    Hash.hash_md5("12345123451234512345")
    Hash.hash_sha1("12345123451234512345")
    Hash.hash_sha224("12345123451234512345")
    Hash.hash_sha256("12345123451234512345")
    Hash.hash_sha384("12345123451234512345")
    Hash.hash_sha512("12345123451234512345")
