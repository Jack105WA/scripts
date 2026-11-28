import time

dog = """
          <O>
       0000
       | ||"""
doghappy = """
          :D
       0000
       | ||"""
dogfetch = """
                                <O>
                              0000
                              | ||     Ɛoo3"""
xmas = """
        *
        ^
       ^^^
      ^^^^^^   
    ^^^^^^^^^^
        ||                                                                                """
happy = 0
last_decay = time.time()
print(dog)
print("dog (By Jack105WA)")
while True:
    if time.time() - last_decay >= 5:
        happy = happy - 1
        if happy < 0:
            happy = 0

        last_decay = time.time()
        action = int(input("1. Feed 2. Pet 3. fetch").strip())
    if action == 1:
        print("\033[H\033[J", end="")
        print("Woof!")
        print(doghappy)
        happy = happy + 5
        if happy > 100:
            happy = 100
        print(f"happy:", happy)
    if action == 2:
        print("\033[H\033[J", end="")
        print("Woof!")
        print(dog)
        happy = happy + 1
        if happy > 100:
            happy = 100
        print(f"happy:", happy)
    if action == 3:
        print("\033[H\033[J", end="")
        print("Woof!")
        print(dogfetch)
        happy = happy + 10
        if happy > 100:
            happy = 100
        print(doghappy)
        print(f"happy:", happy)
    if action == 4:
        print("\033[H\033[J", end="")
        print(xmas)
        print('Merry Christmas!')


input()