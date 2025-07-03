# UPI QR Code Generator 🧾

This is a simple Python project to generate QR codes for UPI payments.  
It supports multiple payment apps like PhonePe, Paytm, and Google Pay.

---

## 🔧 How It Works
- You enter your UPI ID when the program runs.
- The program creates UPI payment URLs for:
  - PhonePe
  - Paytm
  - Google Pay
- Then it creates *QR codes* for each payment app.
- The QR codes are saved as .png files and also displayed on the screen.

---

## 📂 Files in This Project
| File Name              | Purpose                        |
|------------------------|--------------------------------|
| takepaymentonline.py | Main Python script to generate QR codes |
| phonepe_qr.png       | PhonePe QR code image         |
| paytm_qr.png         | Paytm QR code image           |
| google_pay_qr.png    | Google Pay QR code image      |

---

## ▶ How to Run
### 1. Install the Required Libraries
Open your terminal and run:
```bash
pip install qrcode
pip install pillow

2. Run the Python Script in terminal
python takepaymentonline.py

3. Enter your UPI ID when prompted.

4. The QR codes will be saved in your folder and also displayed.
