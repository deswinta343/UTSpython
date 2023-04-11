#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

# membuat koneksi ke database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="DB_SALES_V3922014"
)

# membuat kursor
cursor = db.cursor()

# query SQL untuk melakukan select
sql = "SELECT * FROM Stok_Barang"

# mengeksekusi query SQL
cursor.execute(sql)

# mengambil semua baris hasil query
results = cursor.fetchall()

# menampilkan data
for data in results:
    print(data)

# menutup koneksi ke database
db.close()


# In[2]:


# Membuat function insert
def insert_data():
    pil = 1 # menginsialisasikan nilai awal variabel pil dengan 1
    while pil==1: # membuat perulangan while apabila pil==1 maka kode dibawah ini akan dijalankan 
        #inputkan id barang
        id_barang = input("Masukkan ID Barang: ")
        crs.execute(f"SELECT * FROM stok_barang WHERE id_barang='{id_barang}'")
        #perintah disimpan dalam variabel
        result = crs.fetchone()
        #melakukan identifikasi data
        if result is not None:
            print("Masukkan ID Barang yang lain.")
            continue #user menginputkan data stok
        nama = input("Masukkan Nama Barang:")
        harga = int(input("Masukkan Harga Barang:"))
        stok_awal = int(input("Masukkan Stok Awal Barang:"))
        barang_masuk = int(input("Masukkan Jumlah Barang Masuk:"))
        barang_keluar = int(input("Masukkan Jumlah Barang Keluar:"))
        #menghitung stok akhir
        stok_akhir = stok_awal + barang_masuk - barang_keluar
        print(f"Stok Akhir Barang adalah {stok_akhir}")
        crs.execute(f"INSERT INTO stok_barang (id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir)         VALUES ('{id_barang}', '{nama_barang}', {harga_barang}, {stok_awal}, {barang_masuk}, {barang_keluar}, {stok_akhir})")
        # memasukkan data ke tabel
        db.commit() 
        #perubahan disimpan
        print("Data Berhasil")
        pil = int(input("Masukkan data lagi? 1.Ya \n 0. Tidak: "))


# In[3]:


# Fungsi untuk menampilkan data
def show_data():
    crs.execute("SELECT * FROM Stok_Barang")
    result = crs.fetchall() 
    #mengambil semua baris data
    for row in result: 
        #menggunakan perulangan for untuk setiap row
        id_barang = row[0]
        nama_barang = row[1]
        stok_awal = row[2]
        barang_masuk = row[3]
        barang_keluar = row[4]
        stok_akhir = row[5]
        # menampilkan data 
        print(f"ID Barang: {id_barang}\nNama Barang: {nama_barang}        \nStok Awal: {stok_awal}\nJumlah Barang Masuk: {barang_masuk}\nJumlah Barang Keluar: {barang_keluar}\nStok Akhir: {stok_akhir}\n")


# In[4]:


# Fungsi untuk mengupdate data
def update_data():
    pil = 1
    while pil == 1:
        crs.execute("SELECT * FROM Stok_Barang")
        result = crs.fetchall()
        for row in result: 
            #menggunakan perulangan for
            id_barang = row[0]
            nama_barang = row[1]
            print(f"ID Barang: {id_barang}\nNama Barang: {nama_barang}\n")
            #user menginputkan data yang akan diupdate :
        id_barang = input("Masukkan ID Barang yang ingin diupdate: ") 
        barang_masuk = input("Masukkan jumlah barang masuk: ") 
        barang_keluar = input("Masukkan jumlah barang keluar: ") 
        #mengambil dari table stok_barang berdasrkan id_barang
        crs.execute(f"SELECT stok_akhir FROM stok_barang WHERE id_barang = '{id_barang}'") 
        result = crs.fetchone()
        if result is None: 
            #jika query data barang berdasarkan id tidak ditemukan maka muncul error 
            print("ID Barang tidak ditemukan")
            continue # melanjutkan ke input id barang
        stok_akhir = result[0] + int(barang_masuk) - int(barang_keluar) 
        #menghitung stok akhir barang
        crs.execute(f"UPDATE stok_barang SET stok_awal='{result[0]}', barang_masuk = '{barang_masuk}', barang_keluar = '{barang_keluar}', stok_akhir = '{stok_akhir}' WHERE id_barang = '{id_barang}'")
        db.commit() # menyimpan perubahan pada database
        pil = int(input("Update data lagi? 1.Ya \n 0. Tidak: "))


# In[5]:


# Fungsi untuk menghapus data
def delete_data():
    pil = 1
    while pil == 1:
        
        crs.execute("SELECT * FROM Stok_Barang") 
        #mengambil data barang
        result = crs.fetchall()
        for row in result: 
            #menggunakan perulangan for
            idbarang = row[0]
            nama = row[1]
            print(f"ID Barang: {id_barang}\nNama Barang: {nama_barang}\n")

        idbarang_masuk = input("Masukkan ID Barang yang ingin dihapus: ") # meminta inputan id yang ingin dihapus
        # mengeksekusi query mengambil data dari table stok barang berdasarkan id barang
        crs.execute(f"SELECT stok_akhir FROM stok_barang WHERE id_barang = '{idbarang_masuk}'")
        res = crs.fetchone()
        if res is None: 
            #jika id barang tidak ada maka akan menampilkan error
            print(f"ID Barang {idbarang_masuk} tidak ditemukan")
            continue
        #menghapus data barang berdasarkan id barang
        crs.execute(f"DELETE FROM stok_barang WHERE id_barang = '{idbarang_masuk}'")
        db.commit()
        print("Hapus Data Berhasil")
        pil = int(input("Hapus data lagi? 1.Ya \n 0. Tidak: ")) # menanyakan apakah ingin menghapus data lagi atau tidak


# In[6]:


#cari data
def cari_data():
    pil = 1
    while pil==1: #menggunakan perulangan while
        keyword = input("Masukkan kata kunci: ") 
        #input keyword
        
        #mencari data barang dengan nama berdasarkan keyword
        crs.execute(f"SELECT * FROM stok_barang WHERE nama_barang LIKE '%{keyword}%'")
        result = crs.fetchall()
        if result:
            for row in result: 
                # menampikan data barang menggunakan perulangan for
                idbarang = row[0]
                nama = row[1]
                stok1 = row[2]
                barangIn = row[3]
                barangOut = row[4]
                stok2 = row[5]
            print(f"ID Barang: {id_barang}\nNama Barang: {nama_barang}            \nStok Awal: {stok_awal}\nJumlah Barang Masuk: {barang_masuk}\nJumlah Barang Keluar: {barang_keluar}\nStok Akhir: {stok_akhir}")
        else:
            # jika data tidak ditemukan
            print("Data tidak ditemukan") # menampilkan pesan error
        # meminta input dari user untuk mencari data lagi atau tidak
        pil = int(input("Cari data lagi? 1.Ya \n 0. Tidak: "))


# In[ ]:


import mysql.connector

# membuat koneksi ke database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="DB_SALES_V3922014"
)

# membuat kursor
cursor = db.cursor()


cursor.execute("USE DB_SALES_V3922014")

# membuat function main untuk menjalankan program utama berdasarkan algoritma yang telah diberikan
def main():
    choice = 1
    while choice==1: 
        #menggunakan perulangan while
        # menampilkan pilihan menu
        print("1. Insert DATA\n2. Tampilkan DATA\n3. Update DATA\n4. Hapus DATA\n5. Cari DATA\n0. Keluar")
        menu = int(input("Pilih Menu: \n")) # meminta inputan dari user untuk pilihan menu
        if menu == 1: # jika user memilih 1 maka function insert_data() akan dijalankan
            insert_data()
        elif menu == 2: # jika user memilih 2 maka show_data()) akan dijalankan
            show_data()
        elif menu == 3: # jika user memilih 3 maka update_data()akan dijalankan
            update_data()
        elif menu == 4: # jika user memilih 4 maka hapus_data() akan dijalankan
            delete_data()
        elif menu == 5: # jika user memilih 5 maka cari_data()akan dijalankan
            cari_data()
        elif menu == 0: # jika user memilih 0 maka exit() akan dijalankan dan keluar program
            exit()
        else: # jika pilihan invalid maka akan menampilkan pesan error
            print("Lanjutkan")
        choice = int(input("Mau keluar?\n1. Kembali ke menu\n0. Keluar\n Masukkan pilihan: ")) 
        #meminta inputan user ingin keluar atau tidak
main()


# In[ ]:





# In[ ]:




