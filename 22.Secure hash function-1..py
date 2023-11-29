import hashlib

def hash_string(string, algorithm):
  result = hashlib.new(algorithm, string.encode())
  return result.hexdigest()

algorithms = ["sha256", "sha384", "sha224", "sha512", "sha1"]

for algorithm in algorithms:
  hashed_string = hash_string("Hello everyone", algorithm)
  print(f"The hexadecimal equivalent of {algorithm} is : {hashed_string}")
