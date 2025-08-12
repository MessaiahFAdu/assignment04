correctPassword = "secret"
userAttempt = ""
attemptsLeft = 3
while attemptsLeft > 0 and userAttempt != correctPassword:
    userAttempt = input(f"Enter password (Attempts left: {attemptsLeft})")
    attemptsLeft -= 1
    if userAttempt != correctPassword and attemptsLeft > 0:
        print("Incorrect password, Try again")
if userAttempt == correctPassword:
    print("Access Granted!")
else:
    print("Access Denied!")