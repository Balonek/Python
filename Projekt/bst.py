from collections import deque
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import Qt

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self, update_description_callback=None):
        self.root = None
        self._size = 0
        self._depth = 0
        self.update_description = update_description_callback

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            self._size += 1
            self._depth = 1
            self.update_description()
            return

        current = self.root
        parent = None
        current_depth = 1

        while current is not None:
            parent = current
            if x < current.key:
                current = current.left
            else:
                current = current.right
            current_depth += 1

        if x < parent.key:
            parent.left = Node(x)
        else:
            parent.right = Node(x)

        self._size += 1
        if current_depth > self._depth:
            self._depth = current_depth
        self.update_description()

    def search(self, x):
        current = self.root
        while current is not None and current.key != x:
            if x < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def remove(self, x):
        current = self.root
        parent = None
        current_depth = 1
        is_deepest_node = False

        while current is not None and current.key != x:
            parent = current
            if x < current.key:
                current = current.left
            else:
                current = current.right
            current_depth += 1

        if current is None:
            return

        if current_depth == self._depth:
            is_deepest_node = True

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            else:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None

            del current

            if is_deepest_node:
                self._depth -= 1
            self._size -= 1
            self.update_description()
            return

        if current.left is not None and current.right is not None:
            successor = current.right
            successor_parent = current
            successor_depth = current_depth + 1

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
                successor_depth += 1

            current.key = successor.key

            if successor_parent == current:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right

            if successor_depth == self._depth and successor.right is None:
                self._depth -= 1

            del successor
            self._size -= 1
            self.update_description()
            return
        child = current.left if current.left is not None else current.right
        if parent is None:
            self.root = child
        else:
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child

        del current
        if is_deepest_node and child is None:
            self._depth -= 1
        self._size -= 1
        self.update_description()

    def _clear_recursive(self, node):
        if node:
            self._clear_recursive(node.left)
            self._clear_recursive(node.right)
            del node

    def clear(self):
        self._clear_recursive(self.root)
        self.root = None
        self._size = 0
        self._depth = 0
        self.update_description()

    def size(self):
        return self._size

    def depth(self):
        return self._depth

    def minimum(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.key

    def maximum(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.key

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.key
            yield from self._inorder(node.right)

    def _preorder(self, node):
        if node:
            yield node.key
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def _postorder(self, node):
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.key

    def inorder(self):
        return list(self._inorder(self.root))

    def preorder(self):
        return list(self._preorder(self.root))

    def postorder(self):
        return list(self._postorder(self.root))

    def visualize(self, scene):
        if self.root is None:
            scene.clear()
            return

        scene.clear()

        queue = deque()
        queue.append((self.root, 400, 50))

        current_level = 0
        nodes_in_current_level = 1
        nodes_processed = 0

        pt_diff_y = 70
        pt_diff_x = 100

        while queue:
            node, x, y = queue.popleft()

            circle_size = 40
            circle_r = circle_size // 2

            nodecolor = QBrush(Qt.white)
            black_pen = QPen(Qt.black)
            black_pen.setWidth(2)

            scene.addEllipse(x - circle_r, y - circle_r, circle_size, circle_size, black_pen, nodecolor)

            text_item = scene.addText(str(node.key))
            text_item.setDefaultTextColor(Qt.black)

            rect_text = text_item.boundingRect()
            text_item.setPos(x - rect_text.width() / 2, y - rect_text.height() / 2)

            child_decreasing_space = pt_diff_x // (current_level + 1)

            if node.left:
                child_x = x - child_decreasing_space
                child_y = y + pt_diff_y
                scene.addLine(x, y + circle_r, child_x, child_y - circle_r, black_pen)
                queue.append((node.left, child_x, child_y))

            if node.right:
                child_x = x + child_decreasing_space
                child_y = y + pt_diff_y
                scene.addLine(x, y + circle_r, child_x, child_y - circle_r, black_pen)
                queue.append((node.right, child_x, child_y))

            nodes_processed += 1
            if nodes_processed == nodes_in_current_level:
                current_level += 1
                nodes_in_current_level *= 2
                nodes_processed = 0
