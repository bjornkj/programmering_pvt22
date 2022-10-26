def split_reg(reg_no: str) -> tuple[str, int]:
    letter_part = reg_no[:3]
    number_part = int(reg_no[3:])
    return letter_part, number_part


EXEMPEL = "1,2,3,5,100"


def text_to_list_of_num(text: str) -> list[int]:
    res = []
    for num in text.split(","):
        res.append(int(num))

    return res


def text_to_list(text: str) -> list[int]:
    return list(map(int, text.split(',')))


def text_to_list2(text: str) -> list[int]:
    return [int(n) for n in text.split(',')]


def main():
    user_text = input(">")
    nums = text_to_list(user_text)
    print(f"Första talet: {nums[0]}")
    print(f"Sista talet: {nums[-1]}")
    print(f"Summan av talen: {sum(nums)}")
    print(f"Talen baklänges: {', '.join(map(str, nums[::-1]))}")


if __name__ == '__main__':
    # print(split_reg("ABC123"))
    print(text_to_list_of_num(EXEMPEL))
    print(text_to_list(EXEMPEL))
    print(text_to_list2(EXEMPEL))
    main()
