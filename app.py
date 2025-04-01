from flask import Flask, render_template, request, send_from_directory, send_file, flash, redirect, url_for
from stegano import lsb
import os
from config import Config
from PIL import Image

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your_secret_key_here'  # Required for flashing messages

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_to_png(image_path):
    """Convert an image to PNG format."""
    try:
        img = Image.open(image_path)
        png_path = os.path.splitext(image_path)[0] + '.png'
        img.save(png_path, 'PNG')
        return png_path
    except Exception as e:
        raise Exception(f"Error converting image to PNG: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        # Check if the file is uploaded
        if 'image' not in request.files:
            flash('No file uploaded!', 'error')
            return redirect(request.url)

        image = request.files['image']
        message = request.form['message']
        secret_key = request.form['secret_key']

        # Check if the file is allowed
        if image.filename == '':
            flash('No file selected!', 'error')
            return redirect(request.url)

        if not allowed_file(image.filename):
            flash('Invalid file format. Only PNG, JPG, and JPEG are allowed.', 'error')
            return redirect(request.url)

        # Save the image temporarily
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)

        # Convert JPG/JPEG to PNG
        if image.filename.lower().endswith(('.jpg', '.jpeg')):
            try:
                image_path = convert_to_png(image_path)
            except Exception as e:
                flash(f'Error converting image: {str(e)}', 'error')
                return redirect(request.url)

        # Combine the secret key with the message
        combined_message = f"{secret_key}:{message}"
        print(f"Combined Message: {combined_message}")  # Debug statement

        # Encode the combined message into the image
        try:
            secret_image = lsb.hide(image_path, combined_message)
            encoded_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'encoded_' + os.path.basename(image_path))
            secret_image.save(encoded_image_path)

            flash('Message encoded successfully!', 'success')
            return render_template('encode.html', encoded_image=encoded_image_path)
        except Exception as e:
            flash(f'Error encoding the image: {str(e)}', 'error')
            return redirect(request.url)

    return render_template('encode.html')

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        # Check if the file is uploaded
        if 'image' not in request.files:
            flash('No file uploaded!', 'error')
            return redirect(request.url)

        image = request.files['image']
        secret_key = request.form['secret_key']

        # Check if the file is allowed
        if image.filename == '':
            flash('No file selected!', 'error')
            return redirect(request.url)

        if not allowed_file(image.filename):
            flash('Invalid file format. Only PNG, JPG, and JPEG are allowed.', 'error')
            return redirect(request.url)

        # Save the image temporarily
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)

        # Convert JPG/JPEG to PNG
        if image.filename.lower().endswith(('.jpg', '.jpeg')):
            try:
                image_path = convert_to_png(image_path)
            except Exception as e:
                flash(f'Error converting image: {str(e)}', 'error')
                return redirect(request.url)

        # Decode the message from the image
        try:
            decoded_message = lsb.reveal(image_path)
            print(f"Decoded Message: {decoded_message}")  # Debug statement

            if decoded_message:
                # Split the decoded message into secret key and actual message
                if ':' in decoded_message:
                    decoded_secret_key, actual_message = decoded_message.split(':', 1)
                    if decoded_secret_key == secret_key:
                        return render_template('decode.html', decoded_message=actual_message)
                    else:
                        flash('Invalid secret key!', 'error')
                else:
                    flash('No hidden message found in the image.', 'error')
            else:
                flash('No hidden message found in the image.', 'error')
            return redirect(request.url)
        except Exception as e:
            flash(f'Error decoding the image: {str(e)}', 'error')
            return redirect(request.url)

    return render_template('decode.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)