class Permutation:
    def __init__(self, pairs):
        """
        :param pairs: this is a dictionary. The keys should be 1, 2, ... n, as should the values, non-repeating.
        """
        self.pairs = pairs

    def __str__(self):
        first_line = ""
        n = 1
        for pair in self.pairs:
            first_line += str(n) + " "
            n +=1
        second_line = ""
        n = 1
        for pair in self.pairs:
            second_line += str(self.pairs[n]) + " "
            n += 1
        return first_line + "\n" + second_line

    def act(self, number):
        return self.pairs[number]

    def __mul__(self, other):
        pairs = {}
        for key in self.pairs:
            pairs[key] = self.pairs[other.pairs[key]]
        return Permutation(pairs)

a = Permutation({1:2, 2:4, 3:8, 4:3, 5:1, 6:7, 7:5, 8:6})
print(a, "\n")
b = Permutation({1:4, 2:6, 3:1, 4:7, 5:2, 6:3, 7:8, 8:7})
print(b, "\n")

print(a*b)



