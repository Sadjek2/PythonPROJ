

class Slivik:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.first_element = None
        self.last_element = None
        self.size = 0

    def __str__(self):
        elements = []
        current = self.first_element
        while current:
            elements.append(current.value)
            current = current.next
        return "[" + ', '.join(str(e) for e in elements) + "]"

    def append(self, value):
        new_node = self.Node(value)
        if self.first_element is None:
            self.first_element = new_node
            self.last_element = new_node
        else:
            self.last_element.next = new_node
            self.last_element = new_node
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.first_element
        for _ in range(index):
            current = current.next
        return current.value

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            removed_value = self.first_element.value
            self.first_element = self.first_element.next
            if self.first_element is None:
                self.last_element = None
            self.size -= 1
            return removed_value

        current = self.first_element
        for _ in range(index - 1):
            current = current.next
        removed_value = current.next.value
        current.next = current.next.next
        if current.next is None:  # если удаляем последний элемент
            self.last_element = current
        self.size -= 1
        return removed_value

    def extend(self, other):
        if not isinstance(other, Slivik):
            raise TypeError("Argument must be of type Slivik")
        if other.first_element is None:
            return
        if self.first_element is None:
            self.first_element = other.first_element
            self.last_element = other.last_element
        else:
            self.last_element.next = other.first_element
            self.last_element = other.last_element
        self.size += other.size

    def sort(self):
        if self.size <= 1:
            return

        # Преобразуем список в массив для сортировки
        array = []
        current = self.first_element
        while current:
            array.append(current.value)
            current = current.next

        # Сортируем массив
        array.sort()

        # Преобразуем отсортированный массив обратно в список
        self.first_element = None
        self.last_element = None
        self.size = 0
        for value in array:
            self.append(value)

# Пример использования
FMR = Slivik()
FMR.append('домой хачу(((')
FMR.append('все будет хорошо')
FMR.append('привет мир')
print(FMR)  # Вывод: [домой хачу((((, все будет хорошо, привет мир]

print(FMR.get(1))  # Вывод: все будет хорошо

FMR.remove(0)  # Удаляем первый элемент
print(FMR)  # Вывод: [все будет хорошо, привет мир]

# Создаем другой список
FMR2 = Slivik()
FMR2.append('добавим это')
FMR2.append('и это')
FMR.extend(FMR2)  # Сложение списков
print(FMR)  # Вывод: [все будет хорошо, привет мир, добавим это, и это]

FMR.sort()  # Сортировка
print(FMR)  # Вывод: [все будет хорошо, добавим это, и это, привет мир]