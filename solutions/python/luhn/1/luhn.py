class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        temp = self.card_num.replace(" ", "")
        if len(temp) <= 1 or not temp.isnumeric():
            return False
        temp = [int(item) for item in temp]
        reversed_card_num = list(reversed(temp))
        for i in range(1, len(reversed_card_num), 2):
            reversed_card_num[i] = reversed_card_num[i] * 2
            if reversed_card_num[i] > 9:
                reversed_card_num[i] = reversed_card_num[i] - 9
        return sum(reversed_card_num) % 10 == 0