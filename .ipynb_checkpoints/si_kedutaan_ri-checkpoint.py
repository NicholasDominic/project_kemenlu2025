import sys
import traceback as tb

data_kedutaan = {
    "jepang" : {
        "nama" : "Kedutaan Besar RI di Jepang",
        "alamat" : "Tokyo",
        "jam kerja" : "senin - jumat, 09:00 - 17:00 JST"
    }, 

    "singapura" : {
        "nama" : "Kedutaan Besar RI di SG",
        "alamat" : "Singapura",
        "jam kerja" : "senin - jumat, 09:00 - 17:00 GMT+8"
    },

     "amerika" : {
        "nama" : "Kedutaan Besar RI di Amerika",
        "alamat" : "Washington DC",
        "jam kerja" : "senin - jumat, 09:00 - 17:00 GMT+12"
    }
}

def cari_kedutaan(negara): 
    key = negara.lower()

    if key in data_kedutaan:
        data = data_kedutaan[key]
        print("{}".format(data["nama"].upper()))
        print("- Alamat: {}".format(data["alamat"]))
        print("- Jam Kerja: {}".format(data["jam kerja"]))
    else:
        print("Maaf, data belum tersedia.")

def main_app():
    print("====== SISTEM INFORMASI KEDUTAAN RI ======")

    try:
        # a = 1/0
        user_input = input("Masukkan nama negara: " )
        if not user_input:
            print("Negara tidak boleh kosong.")
        else:
            return cari_kedutaan(negara = user_input)
    
    except Exception as e:
        print("Error message: {}".format(e)) # alasan error
        tb.print_exc() # untuk traceback error di line berapa
        print("Exit.")
        # sys.exit()

if __name__ == "__main__": # syntax umum
    main_app()








