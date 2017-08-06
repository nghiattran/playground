import math

def mask_email(email):
    name, domain = email.split('@')

    return name[0] + '*' * 5 + name[-1] + '@' + domain

def mask_phone(phone):
    numbers = [s for i, s in enumerate(phone) if s.isdigit()]
    part_num = math.ceil((len(numbers) - 4) / 3)
    res = ''
    print(numbers)
    for i in range(int(part_num)):
        end = len(numbers) - 4 - i * 3 - 1
        start = max(end - 3, -1)
        res = '*' * (end - start) + '-' + res
    prefix = '+' if phone[0] == '+' else ''
    return prefix + res + phone[-4:]



print(mask_email('nghiattran3@gmail.com'))
print(mask_phone('+14104225954'))
print(mask_phone('+1(410) 422 5954'))
print(mask_phone('(333)456-7890'))