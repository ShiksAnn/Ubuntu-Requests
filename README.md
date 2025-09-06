# Ubuntu-Requests
# 🌍 Ubuntu Image Fetcher

> *"I am because we are."* — Ubuntu Philosophy  

The **Ubuntu Image Fetcher** is a Python program that embraces the Ubuntu values of **community, respect, and sharing**.  
It connects to the wider web, respectfully fetches shared images, and organizes them for later appreciation.  

---

## ✨ Features
- 📥 Fetches images from the internet using URLs  
- 📂 Automatically organizes them in a `Fetched_Images/` folder  
- 🛡️ Handles errors gracefully (no crashes on bad connections)  
- 🔁 Prevents duplicate filenames  
- 🌐 Supports fetching multiple URLs in one run  

---

## 🛠️ Technologies Used
- **Python **  
- [`requests`](https://docs.python-requests.org/en/latest/) → For fetching images  
- `os` → For directory & file handling  
- `urllib.parse` → For extracting filenames from URLs  

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Ubuntu_Requests.git
cd Ubuntu_Requests
2. Install Dependencies
bash
Copy code
pip install requests
3. Run the Program
bash
Copy code
python ubuntu_image_fetcher.py


🖼️ Example Usage
Terminal Output

pgsql
Copy code
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separated by spaces): 
https://example.com/ubuntu-wallpaper.jpg https://example.com/logo.png

✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

✓ Successfully fetched: logo.png
✓ Image saved to Fetched_Images/logo.png

Connection strengthened. Community enriched.
Folder Structure

**Structure**
Copy code
Ubuntu_Requests/
│
├── ubuntu_image_fetcher.py
├── README.md
└── Fetched_Images/
    ├── ubuntu-wallpaper.jpg
    └── logo.png
