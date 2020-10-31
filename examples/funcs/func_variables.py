def process():
    print("Function process()")

p = process

p()
process()

print(id(p), id(process))