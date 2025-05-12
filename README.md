# CS_370_project-3
Note: Unable to test this with anything else besides IOS
To run this program you must start by 
1. Installing all the dependecies ithin "requirements.txt".

To create a QR code containing the URI follow these steps: 
1. In the command line enter: python ./submission --generate-qr
2. Referesh your working directory and open the file "qr_code.png"
3. Scan the qr code with Google Authenticator (GA)
Note: This will create your secret key in the working directory under "secret_key.txt"

To print the current GA OTP follow these steps:
1. In the command line enter: python ./submission --get-otp
2. This will print the current OTP every 30 seconds until user exits via CTRL+C or kills the program.
