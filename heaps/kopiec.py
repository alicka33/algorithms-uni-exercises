from math import ceil


class Kopiec():

    def __init__(self, root, numbers_of_leafs):
        self.table = []
        self.numbers_of_leafs = numbers_of_leafs
        self.table.append(root)

    def push(self, value):
        self.table.append(value)

        now_index = len(self.table)
        father_index = ceil((now_index-1)/self.numbers_of_leafs)

        while self.table[now_index-1] > self.table[father_index-1] and (now_index > 0 and father_index > 0):
            self.table[now_index-1], self.table[father_index-1] = self.table[father_index-1], self.table[now_index-1]
            now_index = father_index
            father_index = ceil((now_index-1)/self.numbers_of_leafs)

    def pop_root(self):
        last_element = self.table.pop(-1)
        self.table[0] = last_element

        def key_max(index):
            return self.table[index]

        now_index = 0

        sons_index = []
        for i in range(self.numbers_of_leafs):
            if (self.numbers_of_leafs*now_index)+i+1 < len(self.table):
                sons_index.append((self.numbers_of_leafs*now_index)+i+1)
        max_son_index = max(sons_index, key=key_max)

        flaga = True
        while flaga:
            if self.table[now_index] < self.table[max_son_index]:
                self.table[now_index], self.table[max_son_index] = self.table[max_son_index], self.table[now_index]
                now_index = max_son_index
                sons_index = []
                for i in range(self.numbers_of_leafs):
                    if (self.numbers_of_leafs*now_index)+i+1 < len(self.table):
                        sons_index.append((self.numbers_of_leafs*now_index)+i+1)
                if sons_index == []:
                    break
                else:
                    max_son_index = max(sons_index, key=key_max)
            else:
                flaga = False

    def show(self):
        to_show = []
        number_of_values = 1
        now_start_index = 0
        flaga = True
        while flaga:
            now_stop_index = now_start_index+number_of_values
            if now_stop_index > len(self.table):
                now_stop_index = len(self.table)
                flaga = False
            to_show.append(self.table[now_start_index:now_stop_index])
            now_start_index = now_start_index+number_of_values
            number_of_values = number_of_values * self.numbers_of_leafs

        # print(to_show)
        for line in to_show:
            to_print = ""
            for node_value in line:
                to_print += "%03d" % node_value
                to_print += "   "
            print(to_print)


lista = [25, 12, 11, 8, 10, 6, 9, 6, 7, 9, 3, 5, 4, 3]
# lista = [6, 7, 9, 3, 5, 4, 3, 25, 12, 11, 8, 10]
kop = Kopiec(lista[0], 4)
for num in range(1, len(lista)):
    kop.push(lista[num])
kop.show()
# kop = Kopiec(lista, 4)
# kop.show()
