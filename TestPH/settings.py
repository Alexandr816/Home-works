import os
from dotenv import load_dotenv

load_dotenv()

e_mail = os.getenv('e_mail')
pass_word = os.getenv('pass_word')
false_email = os.getenv('false_email')
false_password = os.getenv('false_password')