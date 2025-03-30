import dotenv
import os


dotenv.load_dotenv()
if os.name == "nt":
    os.system("glance.exe")
else:
    os.system("glance")
