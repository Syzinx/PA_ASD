import os
import time
import pwinput
from prettytable import PrettyTable
import math
import json


os.system("cls")

table = PrettyTable()

# MENDEFINISIKAN KELAS PYTHON
class Contacts:
    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.next = None
        self.previous = None

# MENDEFINISIKAN KELAS KONTAKLIST  
class ContactList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def merge_sort(self, contacts):
        if len(contacts) > 1:
            mid = len(contacts) // 2
            left_half = contacts[:mid]
            right_half = contacts[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = 0
            j = 0
            k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i]['name'] < right_half[j]['name']:
                    contacts[k] = left_half[i]
                    i += 1
                else:
                    contacts[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                contacts[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                contacts[k] = right_half[j]
                j += 1
                k += 1

        return contacts

    def sort_contacts(self):
        contacts = []
        current = self.head
        while current:
            contacts.append({'name': current.nama, 'phone': current.no_hp})
            current = current.next

        sorted_contacts = self.merge_sort(contacts)

        table = PrettyTable(['No', 'Nama', 'No. HP'])
        for i, contact in enumerate(sorted_contacts):
            table.add_row([str(i+1), contact['name'], contact['phone']])

        print(table)

    
# MENAMBAHKAN KONTAK   
    def add_contacts(self):
        print("")
        os.system("cls")
        nama = input("MASUKKAN NAMA KONTAK: ")
        no_hp = input("MASUKKAN NOMOR TELEPON: ")

        no_baru = Contacts(nama, no_hp)
        if self.head is None:
            self.head = no_baru
            self.tail = no_baru    
        else:
            no_baru.previous = self.tail
            self.tail.next = no_baru
            self.tail = no_baru
        self.history.append(("Kontak Ditambahkan", nama, no_hp))
        print("")
        print("=== KONTAK BERHASIL DITAMBAHKAN ===")
        print("Mohon Tunggu...")
        time.sleep(3)
        os.system("cls")
# MENGUPDATE KONTAK
    def update_contact(self):
        print("")
        os.system("cls")
        nama = input("MASUKKAN NAMA KONTAK YANG INGIN DIUPDATE: ")
        current = self.head
        while current:
            if current.nama.lower() == nama.lower():
                print("KONTAK YANG AKAN DIUPDATE: ")
                print(f"NAMA: {current.nama}")
                print(f"NO HP: {current.no_hp}")
                new_nama = input("MASUKKAN NAMA BARU (ATAU TEKAN ENTER JIKA TIDAK INGIN DIUBAH): ")
                new_no_hp = input("MASUKKAN NOMOR TELEPON BARU (ATAU TEKAN ENTER JIKA TIDAK INGIN DIUBAH): ", )
                if new_nama:
                    current.nama = new_nama
                if new_no_hp:
                    current.no_hp = new_no_hp
                self.history.append(("Kontak Diupdate", current.nama, current.no_hp))
                print("")
                print("=== KONTAK BERHASIL DIUPDATE ===")
                print("Mohon Tunggu...")
                time.sleep(3)
                os.system("cls")
                return
            current = current.next
        print("")
        print("=== MAAF, KONTAK TIDAK DITEMUKAN ===")
        time.sleep(3)
        os.system("cls")
# MENGHAPUS KONTAK
    def delete_contacts(self):
        print("")
        os.system("cls")
        nama = input("\nMASUKKAN NAMA KONTAK YANG INGIN DIHAPUS: ")
        current = self.head
        while current:
            if current.nama.lower() == nama.lower():
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = current.next
                    current.next.previous = None
                elif current == self.tail:
                    self.tail = current.previous
                    current.previous.next = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                self.history.append(("Kontak Dihapus", current.nama, current.no_hp))
                print("")
                print("=== KONTAK BERHASIL DIHAPUS ===")
                print("Mohon Tunggu...")
                time.sleep(3)
                os.system("cls")
                return
            current = current.next
        print("")
        print("=== MAAF, KONTAK TIDAK DITEMUKAN ===")
        time.sleep(3)
        os.system("cls")
    
# MENAMPILKAN KONTAK
    def display_contacts(contacts):
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact['name']}: {contact['phone']}")
            print()

    def jump_search(self, nama, jump):
        current = self.head
        count = 0
        while current:
            if current.nama.lower().find(nama.lower()) != -1:
                return current
            count += 1
            if count % jump == 0:
                if current.nama.lower() >= nama.lower():
                    break
            current = current.next
        return None
    
    def search_contact(self):
        print("")
        os.system("cls")
        nama = input("MASUKKAN NAMA KONTAK YANG INGIN DICARI: ")
        jump = int(math.sqrt(len(self)))
        result = self.jump_search(nama, jump)
        if not result:
            print("")
            print("MAAF, TIDAK DITEMUKAN KONTAK DENGAN NAMA TERSEBUT")
        else:
            result_list = []
            while result:
                if result.nama.lower().find(nama.lower()) != -1:
                    result_list.append(result)
                result = result.next
            os.system("cls")
            print(">>>> HASIL PENCARIAN KONTAK <<<<")
            print("")
            table = PrettyTable(['Nama', 'No. HP'])
            for contact in result_list:
                table.add_row([contact.nama, contact.no_hp])
            print(table)
            time.sleep(5)
            os.system("cls")

# MENAMPILKAN RIWAYAT        
    def display_history(self):
        os.system("cls")
        print("============== RIWAYAT ANDA ===============".center(70))
        print("===========================================".center(70))
        print("")
        if len(self.history) == 0:
            print("MAAF, TIDAK ADA RIWAYAT ANDA".center(70))
        else:
            for action in self.history:
                print(action[0], "--->", action[1], "-", action[2])
                time.sleep(5)
                os.system("cls")

# Fungsi untuk melakukan registrasi
def register():
    with open("users.json", "r") as f:
        users = json.load(f)
    email = input("Masukkan email: ")
    
# Mencari apakah email sudah terdaftar sebelumnya
    for user in users:
        if email == user["email"]:
            print("Email sudah terdaftar. Silakan login atau gunakan email lain.\n")
            return
    password = pwinput.pwinput("Masukkan password: ")
    phone = input("Masukkan nomor telepon: ")
    user = {"email": email, "password": password, "phone": phone}
    users.append(user)
    with open("users.json", "w") as f:
        json.dump(users, f)
    print("Registrasi berhasil.\n")
    time.sleep(2)
    os.system("cls")

# Fungsi untuk melakukan login
def login():
    while True:
        with open("users.json", "r") as f:
            users = json.load(f)
        email = input("Masukkan email: ")
        password = pwinput.pwinput("Masukkan password: ")
        for user in users:
            if email == user["email"] and password == user["password"]:
                print("Login berhasil.\n")
                time.sleep(2)
                os.system("cls")
                return
        print("Email atau password salah.\n")

# Program utama
def utama():
    while True:
        print(f"Silakan pilih menu yang diinginkan:\n"
        '''
        ||===================================||
        ||               Menu :              ||
        ||===================================||
        ||      1. Login                     ||
        ||      2. Register                  ||
        ||===================================||\n''')

        choice = int(input("Pilih menu: "))
        if choice == 1:
            login()
            main()
        elif choice == 2:
            register()
        else:
            print("Menu tidak tersedia.\n")


# MENU PROGRAM                
def main():
    if __name__ == '__main__':
        print("")
        contacts_list = ContactList()
        while True:
            print("============================================================".center(70))
            print("======== SILAHKAN PILIH MENU YANG INGIN ANDA AKSES =========".center(70))
            print("============================================================".center(70))
            print("""
            +====================================================+
            |           ==== MENU YANG TERSEDIA ====             |
            +====================================================+
            |                (1) TAMBAH KONTAK                   |
            |                (2) HAPUS KONTAK                    |
            |                (3) LIHAT KONTAK                    |
            |                (4) CARI KONTAK                     |
            |                (5) LIHAT HISTORY                   |
            |                (6) UPDATE KONTAK                   |
            +====================================================+
            """)
            print("")
            
            choice = input("SILAHKAN PILIH MENU YANG ANDA INGINKAN (1-6): ")

            if choice == '1':
                contacts_list.add_contacts()
            elif choice == '2':
                contacts_list.delete_contacts()
            elif choice == '3':
                print("=======  DAFTAR KONTAK ANDA  =======")
                contacts_list.sort_contacts()
                print("====================================")
            elif choice == '4':
                contacts_list.search_contact()
            elif choice == '5':
                contacts_list.display_history()
            elif choice == '6':
                contacts_list.update_contact()
            else:
                print("=== MAAF TIDAK ADA PILIHAN, SILAHKAN PILIH ULANG (1-6) ===")

utama()