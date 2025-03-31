import dotenv
import os


dotenv.load_dotenv()

os.system("glance diagnose")
os.system("glance config:validate")
# os.system("glance config:print")
os.system("glance")
