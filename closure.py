def full_sentence(name):
    age = 36
    xd = "lol"

    def sentence(city):
        return f"I am {name}, age {age} and come from {city}"

    return sentence
#
# s = full_sentence("Pawel")
# print(s.__closure__[0].cell_contents)
# print(s.__closure__[1].cell_contents)
# print(s.__closure__[2].cell_contents)
# print(s("Krakow"))
# print(s("Katowice"))


def gen_uuid():
    idx = 0
    def next_id():
        nonlocal idx
        result = idx
        idx += 1
        return result
    return next_id

uuid = gen_uuid()

for _ in range(10):
    print("Value of enclosing elements: ", uuid.__closure__[0].cell_contents)
    print(uuid())

print(uuid())
print(uuid())
print(uuid())