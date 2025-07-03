# Import the qrcode library
import qrcode

# -----------------------------------------------
# Step 1: Take the UPI ID as input from the user
# -----------------------------------------------
upi_id = input("Enter your UPI ID: ")

# -----------------------------------------------------
# Step 2: Define payment URLs for different apps
# Format of UPI link: upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE
# You can change 'Recipient%20Name' and 'mc' (merchant code) if needed
# -----------------------------------------------------
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# -----------------------------------------------
# Step 3: Create QR codes for each payment app
# -----------------------------------------------
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# ----------------------------------------------------------
# Step 4: Save the QR codes as image files (optional step)
# ----------------------------------------------------------
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# ----------------------------------------------------------
# Step 5: Display the QR codes (optional step)
# You may need to install the Pillow library for image display:
# Run in terminal: pip install Pillow
# ----------------------------------------------------------
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()