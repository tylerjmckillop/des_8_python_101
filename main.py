from dotenv import load_dotenv

#import os to interact with operating system 

import os

# importing the package into our script
# install in terminal first for this to run
# importing the ability to work with the .env file with our secret keys + passwords

# activates ability to go find .env file

load_dotenv()

print(os.getenv('secret'))