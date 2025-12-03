def password_validator(password:str) -> str:
  length=len(password) >=8
  digit=any(c.isdigit() for c in password)
  upper=any(c.isupper() for c in password)
  lower=any(c.islower() for c in password)
  special=any(not c.isalpnum() for c in password)
  score=sum([length, digit, upper, lower, special])
  return["Critical", "Low", "Moderate", "High", "Very High"][score-1]

if__name__=="__main__":
  user_password=input("Please enter a password for strength analysis: ")
  print("Password Strength: ", password_validator(user_password))
