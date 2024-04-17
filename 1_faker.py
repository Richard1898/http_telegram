# 
# Uzdevums: Izmantojot bibliotēku Faker uzģenerēt fake datus
# https://faker.readthedocs.io/en/master/
# https://faker.readthedocs.io/en/stable/providers.html
# 
# Uzinstalē bibliotēku ievadot terminālī
# > pip install Faker
#
from faker import Faker

while True:
    print("\nNejaušo datu ģenerators:")
    print("1. 5 personu vārdi un uzvārdi")
    print("2. 5 personu vārdi un uzvārdi latviešu valodā")
    print("3. 5 persona vārdi un uzvārdi ar telefona numuru, adresi un personas kodu")
    print("4. Teksts dotā maksimāla garumā") # lietotājs ievada maksimalo garumu
    print("5. 5 Dazādas cenas") # valūtas zīme un summa
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        fake = Faker()
        for a in range(5):
            print(fake.name())
    elif choice == "2":
        fake = Faker('lv_LV')
        for a in range(5):
            print(fake.name())
    elif choice == "3":
        fake = Faker()
        for a in range(5):
            print(fake.name())
            print(fake.address())
            print(fake.phone_number())
            print(fake.ssn())
    elif choice == "4":
        fake = Faker()
        x = int(input("Ievadi skaitli: "))
        for a in range(x):
            print(fake.text())
    elif choice == "5":
        fake = Faker()
        for a in range(5):
            print(fake.pricetag())
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")