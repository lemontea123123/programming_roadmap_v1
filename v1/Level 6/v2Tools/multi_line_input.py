"""
Docstring for v2Tools.multi_line_input

Prompt user to input multi lines input
"""

def multi_line_input(dialog="Input Teks Panjang , Enter dua kali untuk akhiri",batas_kata=30):
    user_input = []
    line =""
    loop = True
    length = 0
    batas = batas_kata

    print("Enter dua kali untuk akhiri")
    print(dialog)
    while loop:
        line = input()

        user_input.append(line)
        if(line==""):
            loop=False

        length = len(line)+length

        if(length>=batas):
            print("Teks sudah melebihi jumlah batas kata")
            break

    paragraph = "\n".join(user_input)
    return paragraph

if(__name__=="__main__"):
    multi_line_input(batas_kata=20)