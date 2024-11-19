# Создаем класс, который будет описывать узел дерева. В этом классе будет конструктор
# Нам пригодится значение узла, цвет узла (red/black), левый и правый дочерние узлы и родительский узел

class Node:
  def __init__(self, data, color='red'):
    self.data = data
    self.color = color
    self.left = None
    self.right = None
    self.parent = None

# Создаем класс для красно-черного дерева. В данном классе реализуем конструктор, метод вставки узла, балансировки, обход дерева и вывод на экран (печать)

class RedBlackTree:
  def __init__(self):
    self.null = Node(data = None, color = 'black')   # Создали черный лист null
    self.root = self.null                            # Создали корень дерева

  def insert(self, data):                            # Функция, реализующая вставку
    new_node = Node(data)                            # Создаем новый узел
    new_node.left = self.null                        # Новый левый дочерний узел (null)
    new_node.right = self.null                       # Новый правый дочерний узел (null)
    self._new_uzel(new_node)                       # Вставляем новый узел
    self._balance(new_node)                       # Балансировка после вставки, исправляем дерево, восстанавливаем свойства кчд

  def _new_uzel(self, new_node):                   # Вставка узла (как в бинарное дерево поиска)
        current = self.root                          # В качестве текущего узла берем корень
        parent = None

        while current != self.null:                  # Пока текущий узел не принял значение null, ищем место для нового узла
            parent = current
            if new_node.data < current.data:         # Если значение нового узла меньше значения текущего узла, то идем влево. Если нет, то - вправо
                current = current.left
            else:
                current = current.right

        new_node.parent = parent                     # Для нового узла устанавливаем родителя

        if parent is None:                           # Если дерево пустое, то новый узел становится корнем
            self.root = new_node
        elif new_node.data < parent.data:            # Если новый узел меньше, чем родитель, то новый узел ставим налево. Если нет, то - направо
            parent.left = new_node
        else:
            parent.right = new_node

  def _balance(self, new_node):                                              # Функция, которая реализует балансировку после вставки
        while new_node != self.root and new_node.parent.color == 'red':         # Пока новый узел не является корнем и родитель - красный, выполняем действия цикла (нужно проверить разные ситуации)
            if new_node.parent == new_node.parent.parent.left:                  # Если родитель - это левое поддерево
                uncle = new_node.parent.parent.right                            # Дядей мы делаем правое поддерево и рассматриваем два случая
                if uncle.color == 'red':                                        # Случай 1: дядя красный
                    new_node.parent.color = 'black'                             # Родителя и дядю перекрашиваем в черный, дедушку - в красный
                    uncle.color = 'black'
                    new_node.parent.parent.color = 'red'
                    new_node = new_node.parent.parent                           # Теперь новый узел - это дедушка
                else:                                                           # Случай 2: дядя черный
                    if new_node == new_node.parent.right:                       # Если новый узел - это правое поддерево
                        new_node = new_node.parent                              # Поднимаемся к родителю и делаем левый поворот
                        self._left_rotate(new_node)
                    new_node.parent.color = 'black'                             # Перекрашиваем родителя - в черный, дедушку - в красный. И делаем правый поворот
                    new_node.parent.parent.color = 'red'
                    self._right_rotate(new_node.parent.parent)
            else:                                                               # В противном случае, когда родитель - правое поддерево
                uncle = new_node.parent.parent.left                             # Дядей мы делаем правое поддерево и рассматриваем два случая
                if uncle.color == 'red':                                        # Случай 1: дядя красный
                    new_node.parent.color = 'black'
                    uncle.color = 'black'
                    new_node.parent.parent.color = 'red'
                    new_node = new_node.parent.parent
                else:                                                           # Случай 2: дядя черный
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self._right_rotate(new_node)
                    new_node.parent.color = 'black'
                    new_node.parent.parent.color = 'red'
                    self._left_rotate(new_node.parent.parent)

        self.root.color = 'black'                                               # Корень всегда черный

  def _left_rotate(self, x):                         # Функция, реализующая поворот налево
        y = x.right                                  # Присваиваем у правый дочерний узел
        x.right = y.left                             # Левый дочерний у становится правым дочерним х
        if y.left != self.null:                      # Если левый дочерний не равен null, то устанавливаем родителя для нового дочернего узла х
            y.left.parent = x
        y.parent = x.parent

        if x.parent is None:                         # Если х - корень, то теперь корнем становится у
            self.root = y
        elif x == x.parent.left:                     # Если х - левый потомок , то у станет левым потомком родителя
            x.parent.left = y
        else:                                        # Если х - правый потомок, то у становится правым потомком родителя
            x.parent.right = y

        y.left = x                                   # х будет левым дочерним узлом у, а у становится родителем х
        x.parent = y

  def _right_rotate(self, y):                        # Функция, реализующая поворот направо
        x = y.left                                   # Присваиваем х левый дочерний узел
        y.left = x.right                             # Правый дочерний х становится левым дочерним у
        if x.right != self.null:                     # Если правый дочерний не равен null, то устанавливаем родителя для нового дочернего узла у
            x.right.parent = y
        x.parent = y.parent

        if y.parent is None:                        # Если у - корень, то теперь корнем становится х
            self.root = x
        elif y == y.parent.right:                   # Если у - правый потомок , то х станет правым потомком родителя
            y.parent.right = x
        else:                                       # Если у - левый потомок, то х становится левым потомком родителя
            y.parent.left = x

        x.right = y                                 # у будет правым дочерним узлом х, а х становится родителем у
        y.parent = x

  def height(self):                                 # Функция, вычисляющая высоту дерева
        def _height(node):                          # Если узел - это null, то высота = 0. Если нет, то к максимальной высоте левого/правого поддеревьев добавляем 1
            if node == self.null:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)                   # Возвращаем высоту дерева, начиная с корня

  def __zapolnenie(self, result, node, index):      # Заполнение узлов по уровням
        if node != self.null:                       # Если узел не null, то мы сохраняем его на текущем индексе, затем заполняем левое и правое поддеревья
            result[index] = node
            self.__zapolnenie(result, node.left, 2 * index + 1)
            self.__zapolnenie(result, node.right, 2 * index + 2)

  def beautiful_print(self):        # Функция для красивого вывода нашего дерева
        if self.root == self.null:  # Если корень дерева - null, то выводится сообщение об этом
            print('Данное дерево - пустое')
            return

        height = self.height()  # Вычисляем высоту дерева
        result = [None] * (2 ** height)  # Создаем список result, который будет хранить узлы дерева на разных уровнях
        result[0] = self.root  # Корень дерева - на нулевом уровне
        self.__zapolnenie(result, self.root.left, 1)  # Заполняем левое поддерево
        self.__zapolnenie(result, self.root.right, 2)  # Заполняем правое поддерево

        to_print = []
        for depth in range(height):
            to_print.append([result[2 ** depth + node_index - 1] for node_index in range(2 ** depth)])

        to_print_final = []
        max_columns = sum(2 ** i for i in range(height))
        for depth, nodes_on_depth in enumerate(to_print):
            string_elements_per_depth = [None] * max_columns

            start_step = max_columns // 2 ** (depth + 1)
            step_between = max_columns // 2 ** depth
            for index, node in enumerate(nodes_on_depth):
                if node is not None:
                    string_elements_per_depth[
                        start_step + index * (step_between + 1)
                    ] = f"{node.data}({node.color[0].upper()})"  # Добавляем цвет узла
                else:
                    string_elements_per_depth[start_step + index * (step_between + 1)] = 'XX'
            to_print_final.append(
                ' '.join(
                    '  ' if elem is None else str(elem).zfill(2) for elem in string_elements_per_depth
                )
            )
        print('\n'.join(to_print_final))

##### Пример использования #####

rbt = RedBlackTree()
data_list = [17, 3, 18, 100, 2, 8, 11, 37]

for data in data_list:
  rbt.insert(data)

# Печать дерева
rbt.beautiful_print()

