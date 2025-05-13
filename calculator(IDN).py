print('selamat datang di calculator sederhana')
print('\nsilahkan pilih operasi yang anda inginkan: ')
print('1.perjumlahan (+)')
print('2.perkurangan (-)')
print('3.perkalian (*)')
print('4.pembagian (/)')
print('5.perpangkatan (**)')
operasi = int(input('\nOperasi yang di pilih(silahkan masukan angka): '))
angka1 = int(input('masukan angka pertama: '))
angka2 = int(input('masukan angka kedua: '))

if operasi == 1:
    hasil = angka1 + angka2
    mtk = 'Penjumlahan'
    print('Maka hasil penjumlahan', angka1,'+',angka2,'=',hasil)
 
elif operasi == 2:
    hasil= angka1 - angka2
    mtk = 'Perkurangan'
    print('Maka hasil perkurangan', angka1,'-',angka2,'=',hasil)
   
elif operasi == 3:
    hasil = angka1 * angka2
    mtk = 'Perkalian'
    print('Maka hasil perkalian', angka1,'*',angka2,'=',hasil)
    
elif operasi == 4:
    hasil = angka1 / angka2
    mtk = 'Pembagian'
    print('Maka hasil pembagian', angka1,'/',angka2,'=',hasil)
    
elif operasi == 5:
    hasil = angka1 ** angka2
    mtk = 'Perpangkatan'
    
else:
    print('operasi yang anda masukan salah')

print('maka bilangan binarynya:', format(int(hasil), '08b'))
