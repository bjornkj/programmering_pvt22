

def compute_strength2(pw: str) -> int:
    strength = 0

    has_alpha = False
    has_num = False
    has_special_char = False
    for c in pw:
        if c.isalpha():
            has_alpha = True
        elif c.isnumeric():
            has_num = True
        elif c in "#%&+_-":
            has_special_char = True
        else:
            return 0

    if len(pw) > 10:
        strength += 1
    if has_alpha and has_num:
        strength += 1
    if has_special_char:
        strength += 1

    return strength


def has_number(pw: str) -> bool:
    for c in pw:
        if c.isnumeric():
            return True
    return False


def has_alpha(pw: str) -> bool:
    for c in pw:
        if c.isalpha():
            return True
    return False


def has_special_char(pw: str) -> bool:
    for c in pw:
        if c in "#%&+_-":
            return True
    return False


def only_valid_char(pw: str) -> bool:
    for c in pw:
        if not (c.isalpha() or c.isnumeric() or (c in "#%&+_-")):
            return False
    return True


def compute_strength(pw: str) -> int:
    strength = 0
    if len(pw) > 10:
        strength += 1
    if has_number(pw) and has_alpha(pw):
        strength += 1
    if has_special_char(pw):
        strength += 1
    if not only_valid_char(pw):
        return 0
    return strength

if __name__ == '__main__':
    print("kasjdfhkjlh".upper())
    a = 123
    print(type("hej"))
    print(type(12))
    print(type(12.4))
