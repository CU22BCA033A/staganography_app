import os

class Config:
    SECRET_KEY = 'your_secret_key_here'  # Change this to a secure key
    UPLOAD_FOLDER = 'uploads/'          # Folder for uploaded files
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Allowed file extensions