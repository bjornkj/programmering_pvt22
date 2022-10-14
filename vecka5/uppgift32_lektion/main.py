from vecka5.uppgift32_lektion.pwstrength import compute_strength


def main():
    passwd = input("password>")
    pw_strength = compute_strength(passwd)
    print(f"Password strength: {pw_strength}")


if __name__ == '__main__':
    main()
