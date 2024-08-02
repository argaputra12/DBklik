# Pertanyaan 1
# Kafe saya mulai laris, jadi saya menambah meja dan staf sehingga orang-orang dapat memiliki
# pengalaman lebih baik.
# Di kafe ada dua kasir: satu untuk pesanan dibawa pulang (take away), dan satu untuk pesanan
# makan di tempat (dine in). Semua pesanan digabungkan menjadi satu daftar untuk dapur.
# Pesanan diproses dengan sistem siapa cepat dia dapat (first come first serve).
# Baru-baru ini, beberapa pelanggan mengeluh bahwa orang yang memesan setelah mereka
# mendapatkan makanan terlebih dahulu.
# Untuk menyelidiki keluhan mereka, suatu sore saya duduk di belakang kasir dengan laptop
# saya dan membuat tiga daftar urutan, masing-masing untuk:
# - Pesanan dibawa pulang atau take-out saat dimasukkan ke dalam sistem dan diberikan ke
# dapur.
# - Pesanan makan di tempat saat dimasukkan ke dalam sistem dan diberikan ke dapur.
# - Setiap pesanan pelanggan (dari salah satu kasir) seperti yang diselesaikan oleh dapur.
# Masing-masing daftar urutan tersebut dilambangkan dengan array.
# Dengan tiga array tersebut, tulis metode/fungsi untuk mengecek apakah semua pesanan
# diproses sesuai prinsip siapa cepat dia dapat. Semua makanan harus keluar dalam
# urutan yang sama yang diminta pelanggan.
# Angka dibawah ini melambangkan nomor pesanan pelanggan.
# Sebagai contoh,
# Pesanan ambil: [1, 3, 5]
# Pesanan makan di tempat: [2, 4, 6]
# Pesanan yang dilayani: [1, 2, 4, 6, 5, 3]
# tidak sesuai dan tidak valid, karena pesanan 3 masuk sebelum pesanan 5 tetapi pesanan 5
# dilayani terlebih dahulu.
# Tetapi,
# Pesanan ambil: [17, 8, 24]
# Pesanan makan di tempat: [12, 19, 2]
# Pesanan yang dilayani: [17, 8, 12, 19, 24, 2]`
# valid karena sesuai prinsip siapa cepat dia dapat.

# Catatan: Nomor pesanan bersifat acak. Mereka tidak harus dalam urutan yang meningkat.

# Contoh Input 1
# Pesanan ambil: [1, 3, 5]
# Pesanan makan di tempat: [2, 4, 6]
# Pesanan yang dilayani: [1, 2, 4, 6, 5, 3]

# Contoh Output 1
# False

# Contoh Input 2
# Pesanan ambil: [17, 8, 24]
# Pesanan makan di tempat: [12, 19, 2]
# Pesanan yang dilayani: [17, 8, 12, 19, 24, 2]

# Contoh Output 2
# True

class Order:
    def __init__(self, take_out, dine_in, served):
        self.take_out = take_out
        self.dine_in = dine_in
        self.served = served

    def check_order(self):
        take_out_index = 0
        dine_in_index = 0
        take_out_len = len(self.take_out)
        dine_in_len = len(self.dine_in)
        served_len = len(self.served)

        print(f"Take out: {self.take_out}")
        print(f"Dine in: {self.dine_in}")
        print(f"Served: {self.served}")

        for i in range(served_len):
            # check if take out order is right
            if take_out_index < take_out_len and self.served[i] == self.take_out[take_out_index]:
                take_out_index += 1
            # check if dine in order is right
            elif dine_in_index < dine_in_len and self.served[i] == self.dine_in[dine_in_index]:
                dine_in_index += 1
            else:
                return False
            
        # check if all take out and dine in orders are served
        if take_out_index != take_out_len or dine_in_index != dine_in_len:
            return False
        
        return True 

def input_order():
    take_out = list(map(int, input("Pesanan ambil: ").split()))
    dine_in = list(map(int, input("Pesanan makan di tempat: ").split()))
    served = list(map(int, input("Pesanan yang dilayani: ").split()))

    order = Order(take_out, dine_in, served)

    return order
    
def main():
    
    # Test cases
    # Pesanan ambil: [1, 3, 5]
    # Pesanan makan di tempat: [2, 4, 6]
    # Pesanan yang dilayani: [1, 2, 4, 6, 5, 3]
    order = Order([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3])
    print(order.check_order())
    
    # Pesanan ambil: [17, 8, 24]
    # Pesanan makan di tempat: [12, 19, 2]
    # Pesanan yang dilayani: [17, 8, 12, 19, 24, 2]
    order = Order([17, 8, 24], [12, 19, 2], [17, 8, 12, 19, 24, 2])
    print(order.check_order())

    # Pesanan ambil: [3, 2, 1]
    # Pesanan makan di tempat: [6, 5, 4]
    # Pesanan yang dilayani: [3, 6, 5, 4, 2, 1]
    order = Order([3, 2, 1], [6, 5, 4], [3, 6, 5, 4, 2, 1])
    print(order.check_order())

    order = input_order()
    print(order.check_order())

if __name__ == "__main__":
    main()
