import secrets, hmac, hashlib, string

STATES = ["ROCK", "PAPER", "SCISSORS", "SPOCK", "LIZARD"]
#STATES = ["ROCK", "PAPER", "SCISSORS"]

print(' '.join(STATES))
print("Rules:")
print("The computer makes a move and encrypts it.")
print("The computer sends you a verification code and you make your move.")
print("After this happens, you are informed of the result and the key for verification")
print("LET'S GO")
print()

computerChoice = ''.join(secrets.choice(STATES))
digits = string.ascii_letters + string.digits
key = str.encode(''.join(secrets.choice(digits) for i in range(16)))
hash = hmac.new(key, str.encode(computerChoice), hashlib.sha1).hexdigest()

print("hash: " + hash)
print()
print("Choose your destiny(one from this):")
print(' '.join(STATES))
userChoice = input("Your choice: ")

print(computerChoice + "(PC) VS (YOU)" + str.upper(userChoice))
computerChoice = STATES.index(computerChoice)
userChoice = STATES.index(str.upper(userChoice))
answer = (len(STATES) + computerChoice - userChoice) % len(STATES)
if answer == 0:
    print("Draw!")
elif (answer % 2) == 1:
    print("You lose!")
elif (answer % 2) == 0:
    print("You win!")

print()
print("Key for check: " + key.decode("utf-8"))
