# 
# Uzdevums: Izmantojot bibliotēku "requests" uzģenerēt Chuck Norris jokus
# https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
# https://api.chucknorris.io/
# 
# 1. Izdrukā 3 nejaušus jokus no Chuck Norris
# 
# 2. Izdrukā 3 nejaušus jokus no Chuck Norris par programmēšanu

import requests
r = requests.get('https://api.chucknorris.io/jokes/random')
r.json()
while True:
    print("\nNejaušo datu ģenerators:")
    print("1. 3 nejaušus jokus no Chuck Norris")
    print("2. 3 nejaušus jokus no Chuck Norris par programmēšanu")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        for i in range(3):
            r = requests.get('https://api.chucknorris.io/jokes/random')
            h = r.json()
            print(h['value'])
    elif choice == "2":
        for i in range(3):
            r = requests.get('https://api.chucknorris.io/jokes/random?category=dev')
            h = r.json()
            print(h['value'])
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")