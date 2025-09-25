import hashlib

input = ""

with open("./input") as f:
    input = f.readline()
input = input.replace("\n", "")
i = 0
while True:
    x = input + str(i)
    h = hashlib.new("md5")
    h.update(x.encode("UTF-8"))
    result = h.hexdigest()
    if result.startswith("000000"):
        break
    i += 1
print(i)
