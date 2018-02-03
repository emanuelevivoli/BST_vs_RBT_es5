
# NODO ALBERO BINARIO DI RICERCA


class abr_Node:

    # COSTRUTTORE
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

    def get(self):
        return self.key

    def set(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if (self.left != None):
            children.append(self.left)
        if (self.right != None):
            children.append(self.right)
        return children

# ALBERO BINARIO DI RICERCA

class ABR:
    A = ''
    h_ins = 0

    # COSTRUTTORE
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = abr_Node(key)

    # INSERIMENTO RICORSIVO
    def insert(self, key):
        self.h_ins = 0
        if self.root is None:
            self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        self.h_ins += 1
        if key <= currentNode.key:
            if currentNode.left is not None:
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = arn_Node(key)
                currentNode.left.p = currentNode
        elif key > currentNode.key:
            if currentNode.right is not None:
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = arn_Node(key)
                currentNode.right.p = currentNode

    # INSERIMENTO ITERATIVO
    def insert_ite(self, key):
        self.h_ins = 0
        self.insert_(abr_Node(key))

    def insert_(self, z):
        y = None
        x = self.root
        while x is not None:
            self.h_ins += 1
            y = x
            if x.key > z.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

    # CANCELLAZIONE
    def delete(self, key):
        if self.root is None:
            return False
        else:
            x = self.searchNode(self.root, key)
            return self.deleteNode(x) if x else x

    def deleteNode(self, z):
        if z.left is None:
            self.trapianto(z, z.right)
        elif z.right is None:
            self.trapianto(z, z.left)
        else:
            y = self._minimum(z.right)
            if y.p != z:
                self.trapianto(y, y.right)
                y.right = z.right
                y.right.p = y
                self.trapianto(z, y)
                y.left = z.left
                y.left.p = y
        return True

    # TROVA
    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if currentNode is None:
            return False
        elif key == currentNode.key:
            return True
        elif key < currentNode.key:
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)

    # CERCA
    def search(self, key):
        return self.searchNode(self.root, key)

    def searchNode(self, x, key):
        if x is None or x.key == key:
            return x
        elif key < x.key:
            return self.searchNode(x.left, key)
        else:
            return self.searchNode(x.right, key)

    # ATTRAVERSAMENTO
    def inorder(self):
        def _inorder(v):
            if v is None:
                return
            if v.left is not None:
                _inorder(v.left)
            print v.key
            if v.right is not None:
                _inorder(v.right)

        _inorder(self.root)

    def preorder(self):
        def _preorder(v):
            if v is None:
                return
            print v.key
            if v.left is not None:
                _preorder(v.left)
            if v.right is not None:
                _preorder(v.right)

        _preorder(self.root)

    def postorder(self):
        def _postorder(v):
            if v is None:
                return
            if v.left is not None:
                _postorder(v.left)
            if v.right is not None:
                _postorder(v.right)
            print v.key

        _postorder(self.root)

    # MINIMO
    def minimum(self):
        if self.root is None:
            return None
        else:
            return self._minimum(self.root)

    def _minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    # MASSIMO
    def maximum(self):
        if self.root is None:
            return None
        else:
            return self._maximum(self.root)

    def _maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    # SUCCESSORE
    def successor(self, x):
        if x.right is not None:
            return self._minimum(x.right)
        y = x.p
        while y is not None and x is y.right:
            x = y
            y = y.p
        return y

    # PREDECESSORE
    def predecessor(self, x):
        if x.left is not None:
            return self._maximum(x.left)
        y = x.p
        while y is not None and x is y.left:
            x = y
            y = y.p
        return y

    # TRAPIANTO
    def trapianto(self, u, v):
        if u.p is None:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    # SERIALIZZAZIONE RICORSIVA
    def pre_string(self, x):
        if x is not None:
            self.A += str(x.key) + " ["
            self.pre_string(x.left)
            self.A += ", "
            self.pre_string(x.right)
            self.A += "]"
        else:
            self.A += "_"

