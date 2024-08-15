from os import system
system("cls")

def sozlar(gap, lst):
    count = 0
    for harf in lst:
        if gap in harf:
            count += 1
    return count


left_hand = [
    {'1', 'Q', 'A', 'Z'},
    {'2', 'W', 'S', 'X'},
    {'3', 'E', 'D', 'C'},
    {'4', 'R', 'F', 'V', '5', 'T', 'G', 'B'}
]


right_hand = [
    {'6', 'Y', 'H', 'N', '7', 'U', 'J', 'M'},
    {'8', 'I', 'K'},
    {'9', 'O', 'L'},
    {'0', 'P', '[', ']', ';', '\'', ',', '.', '/'}
]


soz = input("So'zni kiriting: ").upper()

ls = [sozlar(i, left_hand) for i in soz]


ls1 = [sozlar(i, right_hand) for i in soz]


print("Chap qo'lda ", sum(ls))
print("O'ng qo'lda ", sum(ls1))
