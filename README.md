
### `README.md`

```markdown
# Steganography Web Application

A web application for encoding and decoding secret messages in images using steganography. Built with **Python**, **Flask**, and **Stegano**.

---

## Features

1. **Encode a Message**:
   - Hide a secret message inside an image.
   - Supports PNG, JPG, and JPEG formats.
   - Uses a secret key for added security.

2. **Decode a Message**:
   - Extract a hidden message from an image.
   - Requires the same secret key used during encoding.

3. **Dark Mode / Light Mode**:
   - Toggle between dark and light themes.
   - Theme preference is saved in the browser.

4. **Image Preview**:
   - Preview the uploaded image before encoding or decoding.

5. **File Size Validation**:
   - Restrict file uploads to 5MB or less.

6. **Copy to Clipboard**:
   - Copy the decoded message to the clipboard with one click.

7. **Download Encoded Image**:
   - Download the encoded image after hiding the message.

8. **Responsive Design**:
   - Works seamlessly on desktop, tablet, and mobile devices.

---

## Technologies Used

- **Backend**:
  - Python
  - Flask (Web Framework)
  - Stegano (Steganography Library)
  - Pillow (Image Processing)

- **Frontend**:
  - HTML5
  - CSS3 (Flexbox, Animations)
  - JavaScript (Dark Mode, Image Preview, Copy to Clipboard)
  - Font Awesome (Icons)

- **Other Tools**:
  - Git (Version Control)
  - Pip (Dependency Management)

---

## Setup Instructions

### Prerequisites

1. **Python 3.x**:
   - Download and install Python from [python.org](https://www.python.org/).

2. **Pip**:
   - Pip is included with Python. Ensure it's installed by running:
     ```bash
     pip --version
     ```

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/steganography_app.git
   cd steganography_app
   ```

2. **Create a Virtual Environment** (Optional but Recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Folder Structure

```
steganography_app/
├── app.py                  # Main Flask application
├── requirements.txt        # List of dependencies
├── config.py               # Configuration settings
├── uploads/                # Folder for uploaded images
├── templates/              # HTML templates
│   ├── index.html          # Home page
│   ├── encode.html         # Encode page
│   └── decode.html         # Decode page
├── static/                 # Static files (CSS, JS, images)
│   ├── css/
│   │   └── styles.css      # Custom CSS styles
│   ├── js/
│   │   └── script.js       # Custom JavaScript
│   └── images/             # Static images (e.g., logos)
└── README.md               # Project documentation
```

---

## Usage

1. **Encode a Message**:
   - Go to the **Encode** page.
   - Upload an image (PNG, JPG, or JPEG).
   - Enter a message and a secret key.
   - Click **Encode**.
   - Download the encoded image.

2. **Decode a Message**:
   - Go to the **Decode** page.
   - Upload the encoded image.
   - Enter the secret key used during encoding.
   - Click **Decode**.
   - View the hidden message.

---

## Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Encode Page
![Encode Page](screenshots/encode.png)

### Decode Page
![Decode Page](screenshots/decode.png)

---

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. 

---

## Acknowledgments

- **Flask**: For the web framework.
- **Stegano**: For the steganography library.
- **Font Awesome**: For the icons.

---

## Contact

For questions or feedback, feel free to reach out:

- **Name**: Sugnana Murthy GM
- **Email**: sugveer1@gmail.com
- **GitHub**: [CU22BCA033A](https://github.com/CU22BCA033A)

