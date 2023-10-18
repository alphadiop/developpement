
import itertools as it
x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c']
liste = list(zip(x,y))
liste_zip = list(map(len, ['abc', 'de', 'fghi']))




if __name__ == "__main__":
    print(f"liste : {liste}")
    print(f"liste_zip : {liste_zip}")