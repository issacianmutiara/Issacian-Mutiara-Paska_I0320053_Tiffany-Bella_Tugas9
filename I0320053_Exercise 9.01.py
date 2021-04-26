import sys

#mendefinisikan array konstan

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

def main():
    # meminta user untuk memasukkan nomor hari
    nohari = int(input('Masukkan nomor hari [1..7]: '))

    if (nohari < 1) or (nohari > 7):
        print('Tidak ada hari ke-%s"%nohari')
        sys.exit(1)

    print('Hari ke-%d adalah %s'%(nohari,DAYS[nohari-1]))

if __name__=="__main__":
    main()