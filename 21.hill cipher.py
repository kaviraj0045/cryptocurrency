import string

class HillCipher:
    key_string = string.ascii_uppercase + string.digits
    modulus = numpy.vectorize(lambda x: x % 36)
    to_int = numpy.vectorize(lambda x: round(x))

    def __init__(self, encrypt_key):
        self.encrypt_key = self.modulus(encrypt_key)
        self.check_determinant()
        self.decrypt_key = self.modulus(numpy.linalg.inv(self.encrypt_key))
        self.break_key = encrypt_key.shape[0]

    def replace_letters(self, letter):
        return self.key_string.index(letter.upper())

    def replace_digits(self, num):
        return self.key_string[round(num)]

    def check_determinant(self):
        det = round(numpy.linalg.det(self.encrypt_key))
        if det < 0:
            det = det % len(self.key_string)
        req_l = len(self.key_string)
        if math.gcd(det, req_l) != 1:
            raise ValueError(f"Try another key.")

    def process_text(self, text):
        chars = [char for char in text if char in self.key_string]
        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)
        return "".join(chars)

    def encrypt(self, text):
        text = self.process_text(text)
        encrypted = ""
        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i:i + self.break_key]
            batch_vec = [self.replace_letters(char) for char in batch]
            batch_vec = numpy.array([batch_vec]).T
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[0]
            encrypted_batch = "".join(self.replace_digits
