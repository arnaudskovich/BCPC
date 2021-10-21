from re import compile, search


def numberOfSimilarStartings(list, current):
    similarStartings = 0
    c_p = compile(r"^"+current)
    for search in list:
        if c_p.match(search):
            similarStartings += 1
    return similarStartings


def enterSearchesAndFindSimilars():
    # getting number of searches will be done
    n = 0
    n_p = compile(r"^\d+$")
    s_p = compile(r"^[a-z]{1,32}$")
    inputs = []
    while n == 0:
        n_inp = input("Enter number of searches will be done: ")
        if n_p.match(n_inp):
            int_n_inp = int(n_inp)
            if int_n_inp >= 0 and int_n_inp <= 100:
                n = int_n_inp
    # getting searches
    i = 1
    while n > 0:
        s_inp = input("Enter search "+str(i)+": ")
        if s_p.match(s_inp):
            print(numberOfSimilarStartings(inputs, s_inp))
            inputs.append(s_inp)
            n -= 1
            i += 1


enterSearchesAndFindSimilars()
