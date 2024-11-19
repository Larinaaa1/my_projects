class Node():
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def get_last(self):
          iter = self.head
          if iter is not None:
              while iter.next is not None:
                  iter = iter.next
              return iter
          return None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.get_last()
            last.next = new_node
        self.size += 1

    def __print_list(self, node):
        print(node.data, end=" ")
        if node.next is not None:
            self.__print_list(node.next)

    def print_list(self):
        if self.head is not None:
            self.__print_list(self.head)


    def reverse(self):
      if self.head is None:    # Проверяем, пустой у нас список или нет. Если пустой, то возврящаем None
        return None
      else:                    # Если не пустой, то идем дальше
        pred = None            # Предыдущему изначально устанавливаем None
        iter = self.head       # iter указывает на первый элемент
        follow = iter.next     # follow указывает на второй элемент
        while iter is not None:   # Пока не дошли до конца списка, начинаем менять направление ссылок
          iter.next = pred
          pred = iter
          iter = follow
          if follow is not None:
            follow = follow.next
        self.head = pred           # head начинает указывать на последний элемент списка (хвост стал головой)

##### ПРОВЕРКА #####

# Выводим первоначальный список
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)

l.print_list()

# Выводим перевернутый список
l.reverse()
l.print_list()
