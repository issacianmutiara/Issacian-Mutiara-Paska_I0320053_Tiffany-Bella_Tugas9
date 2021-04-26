#mendefinisikan array asosiatif
import sys
DICT = {
        'one'   : 'satu',
        'two'   : 'dua',
        'three' : 'tiga',
        'four'  : 'empat',
        'five'  : 'lima',
        'six'   : 'enam',
        'seven' : 'tujuh',
        'eight' : 'delapan',
        'nine'  : 'sembilan',
        'ten'   : 'sepuluh'
        # ...
        }
def main():
    #meminta user to input a word in english
    word = input('masukkan kata in english : ')

    if not (word in DICT.keys()):
        print("'%s' the word can not found in dict" %word)
        sys.exit(1)

    print("the '%s' meaning is '%s'"% (word, DICT[word]))

if __name__== '__main__':
    main()

