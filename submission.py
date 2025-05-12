from sys import argv
import qrcode
import pyotp

def generate_QR(key):

    URI = pyotp.totp.TOTP(key).provisioning_uri(name="Seiferco", issuer_name="Project-3 Program")
    qrcode.make(URI).save("qr_code.png")
    
    return

def get_OTP():

    return

def main():
    key = pyotp.random_base32()
    
    command = argv[1]

    if(command == "--generate-qr"):
        generate_QR(key)

    elif(command == "--get-otp"):
        get_OTP()
    else:
        print("Unknown command arg")

    return 0


if __name__ == "__main__":
    main()


