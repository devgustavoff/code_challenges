class Luhn:

    def __init__(self, card_num):
        self.isValid = Luhn.luhny_bin(card_num)

    def valid(self):
        return self.isValid

    @staticmethod
    def luhny_tune(num):
        return dbl - 9 if (dbl := 2 * num) > 9 else dbl

    @staticmethod
    def luhny_bin(num):
        num = num.replace(" ", "")

        if not num.isdigit():
            return False

        total = 0

        for pos, ltr in enumerate(num[::-1]):
            if not pos % 2:
                total += int(ltr)
            else:
                total += Luhn.luhny_tune(int(ltr))
            pos += 1

        return pos > 1 and not total % 10