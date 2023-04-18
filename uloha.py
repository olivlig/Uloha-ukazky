#!/usr/bin/env python3
slovicka="ahoj cau ahojte teba oni maju pavuky ryba mnau rizoto dvere kniha pradlo boruvky noha zaklinadlo ona mojko slivka a"
slovicka=slovicka.split(" ")

najdene=False

import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("--test", default=False, const=True, nargs="?", type=str, help="test the function on wordlist of all english words (~5MB in size)")
parser.add_argument("--two", default=False, const=True, nargs="?", type=str, help="two words mode")
parser.add_argument("--word", default="ahojcautebaoniazaklinadlo", type=str, help="string to be checked")
#import regex





najdene=False



def rekurzia(slovko,slovnik,zoznam=[]):
    global najdene
    dlzka=len(slovko)
    #zoznam=zoznam.copy()
    if slovko=="":
        return True,zoznam
    vysledok= False
    for i in range(1,len(slovko)+1):
        if najdene:
            return True,zoznam
        print(zoznam)
        if slovko[:i] in slovnik:
            zoznam.append(slovko[:i])
            if slovko[i:]=="":
                najdene=True
            vysledok,zoznam=rekurzia(slovko[i:],slovnik,zoznam)
    if vysledok:
        return True,zoznam
    else:
        if zoznam!=[]:
            zoznam.pop()
        return False,zoznam
#najdene= False;rekurzia("aahojacauzaklinadloaaaa",slovicka,[])





def dve_slova(slovko, slonik):
    for i in range(1,len(slovko)):
        print((slovko[:i] in slonik) and (slovko[i:] in slonik))
        print(slovko[:i]+"+"+slovko[i:])


def lepsia(slovko,slovnik):
    slovo_dlzka=len(slovko)
    for i in range(1,len(slovko)):
        if (slovko[:i] in slovnik) and (slovko[i:] in slovnik):
            return True,[slovko[:i],slovko[i:]]
    return False,[]




def main(args):
    if args.two:
        return lepsia(args.word,slovicka)

    global najdene
    najdene=False
    return rekurzia(args.word,slovicka)




if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    words = main(args)
    if words!=None:
        if words[0]:
            print("given string is concatenation of following strings:\n"+"\n".join(words[1]))
        else:
            print("given string is not concatenation of strings from dictionary")

