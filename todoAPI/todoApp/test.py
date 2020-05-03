import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MY_DIR = os.path.join(os.path.dirname(BASE_DIR), "venv", "lib", "python3.6","site-packages","drf_yasg","static")
print(BASE_DIR)
print(MY_DIR)
