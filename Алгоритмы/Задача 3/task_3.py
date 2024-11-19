# Создаем класс, представляющий узел в бинарном дереве
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# Создаем класс бинарных деревьев поиска
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    # Функция для добавления нового элемента
    def add(self, data):
        if self.root is None:  # Проверяем, если корень "пустой", то новое значение добавляем в корень
            self.root = Node(data)
            self.size += 1  # Увеличиваем размер дерева
        else:  # Если корень не пустой, то мы идем по дереву, ищем значение None и добавляем новый элемент
            uzel = self.root
            while uzel is not None:
                if data < uzel.data:  # Если новый элемент меньше корня, то идем влево
                    if uzel.left is None:  # Находим значение None, добавляем элемент
                        uzel.left = Node(data)
                        self.size += 1  # Увеличиваем размер дерева
                        break
                    else:
                        uzel = uzel.left
                elif data > uzel.data:  # Если новый элемент больше корня, то идем вправо
                    if uzel.right is None:  # Находим значение None, добавляем элемент
                        uzel.right = Node(data)
                        self.size += 1  # Увеличиваем размер дерева
                        break
                    else:
                        uzel = uzel.right
                else:
                    break

    # Функция для вычисления высоты дерева

    def height(self):     # Если корень "пустой", то возвращаем 0, если нет, то начинаем считать
        if self.root is None:
            return 0
        return self.__height(self.root)


    def __height(self, uzel):
        if uzel is None:
            return 0
        return max(self.__height(uzel.left), self.__height(uzel.right)) + 1     # Возвращается максимальная высота левого и правого поддеревьев +1 (для текущего узла)



    # Функция, которая печатает дерево в красивом виде
    def beautiful_print(self):
        if self.root is None:                                  # Если корень дерева - None, то выводится сообщение об этом
            print('Данное дерево - пустое')
            return

        height = self.height()                                 # Вычмсляем высоту дерева
        result: list[Node | None] = [None] *(2** height)       # Cоздаем список result, который будет хранить узлы дерева на разных уровнях
        result[0] = self.root                                  # Корень дерева - на нулевом уровне
        self.__fill_array(result, self.root.left, 1)           # При помощи функции __fill.array рекурсивно заполняем левое и правое поддеревья
        self.__fill_array(result, self.root.right, 2)
        to_print = []
        for depth in range(height):
            to_print.append([result[2**depth + uzel_index - 1] for uzel_index in range(2 ** depth)])

        to_print_final = []
        max_columns = sum(2**i for i in range(height))
        for depth, uzel_on_depth in enumerate(to_print):
            string_elements_per_depth = [None] * max_columns

            start_step = max_columns // 2 ** (depth + 1)
            step_between = max_columns // 2 ** depth
            for index, uzel in enumerate(uzel_on_depth):
                string_elements_per_depth[
                    start_step + index * (step_between + 1)
                ] = uzel.data if uzel is not None else 'XX'
            to_print_final.append(
                ' '.join(
                    '  ' if elem is None else str(elem).zfill(2) for elem in string_elements_per_depth
                )
            )
        print('\n'.join(to_print_final))


    # Функция, которая заполняет массив узлами дерева и использует индексы для размещения узлов на соответствующих уровнях
    def __fill_array(self, arr: list[Node | None], uzel: Node, index: int) -> None:    # Функция, которая заполняет массив узлами дерева и использует индексы для размещения узлов на соответствующих уровнях
        if arr[index] is not None:
            raise ValueError(f'Должно быть: None {index=}, {uzel}')

        arr[index] = uzel

        if uzel.left is not None:
            self.__fill_array(arr, uzel.left, 2 * index + 1)                         # Левые узлы размещаются по формуле для индексов: 2 * index + 1

        if uzel.right is not None:
            self.__fill_array(arr, uzel.right, 2 * index + 2)                        # Правые узлы размещаются по формуле для индексов: 2 * index + 2



    # Функция, которая инвертирует бинарное дерево
    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, uzel: Node) -> Node:
        if uzel is None:
            return None

        # Инвертируем поддеревья
        uzel.left, uzel.right = uzel.right, uzel.left

        # Рекурсивно инвертируем левое и правое поддеревья
        self.__invert_tree(uzel.left)
        self.__invert_tree(uzel.right)

        return uzel


##### Пример использования #####

tree = BinarySearchTree()
nodes = [13, 2, 1, 4, 11, 25, 20, 33, 28, 36]
for i in nodes:
    tree.add(i)  # Добавляем узлы из списка

print("Дерево до инверсии:")
tree.beautiful_print()
print()

tree.invert()  # Инвертируем дерево

print("Дерево после инверсии:")
tree.beautiful_print()