import hashlib

def crack_sha1_hash(hash, use_salts=False):
  top_passwords = get_top_passwords()
  if use_salts:
      salts = get_salts()
  
  for password in top_passwords:
      if use_salts:
          for salt in salts:
              hash_pass = hashlib.sha1((password + salt).encode('utf-8')).hexdigest()
              if hash_pass == hash:
                  return password
              hash_pass = hashlib.sha1((salt + password).encode('utf-8')).hexdigest()
              if hash_pass == hash:
                  return password
      else:
        hash_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
        if hash_pass == hash:
            return password

  return 'PASSWORD NOT IN DATABASE'



def get_salts():
    salts = []
    with open('known-salts.txt', 'r') as fp:
        line = fp.readline()
        while line:
            salts.append(line.strip())
            line = fp.readline()
    return salts

def get_top_passwords():
    passwords = []
    with open('top-10000-passwords.txt', 'r') as fp:
        line = fp.readline()
        while line:
            passwords.append(line.strip())
            line = fp.readline()
    return passwords
