from sys import argv
import qrcode
import pyotp
import time
import base64

def generate_QR():
    # Generate a new key and save it to a file
    key = pyotp.random_base32()
    with open("secret_key.txt", 'w') as file:
        file.write(key)

    # Create QR for user to scan with Google Authenticator 
    URI = pyotp.totp.TOTP(key).provisioning_uri(name="Seiferco", issuer_name="Project-3 Program")
    qrcode.make(URI).save("qr_code.png")
    
    return

def get_OTP():
    
    # Retrieve the key that was created for TOTP
    with open("secret_key.txt", 'r') as file:
        key = file.read()

    
    # Print current valid TOTP every 30 seconds
    while(1):
        totp = pyotp.TOTP(key)
        print(f"Current OTP: {totp.now()}")
        time.sleep(30)

    return

def main():
    
    command = argv[1]

    if(command == "--generate-qr"):
        generate_QR()

    elif(command == "--get-otp"):
        get_OTP()
    else:
        print("Unknown command arg")

    return 0


if __name__ == "__main__":
    main()


