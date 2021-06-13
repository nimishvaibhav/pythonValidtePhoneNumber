import re

def validate_phone_number():
    number = '9865475590'
    match = re.search(r'^[789]\d{9}$', number)
    print(match)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    validate_phone_number()

