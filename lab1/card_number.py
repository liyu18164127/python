def check_card_number(card_number):
    digits = []
    while card_number != 0:
        digits = [card_number % 10] + digits
        card_number = card_number // 10
    return check_card_number_str(digits)

def check_card_number_str(string):
    digits = list(map(int, string))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return ((odd_sum + even_sum) % 10 )== 0

def generate_card_number(card):
    from random import randint
    card_types = ["visa", "mastercard"]

    def prefill(t):
        def_length = 16
        if t == card_types[0]:
            return [4], def_length - 1
        elif t == card_types[1]:
            return [5, randint(1, 5)], def_length - 2

    t = card
    initial, rem = prefill(t)
    so_far = initial + [randint(1, 9) for x in range(rem - 1)]
    print(so_far)
    string = ''.join(map(str,so_far))
    return string



assert check_card_number(5082337440657928)
assert not check_card_number_str('4601496706376197')