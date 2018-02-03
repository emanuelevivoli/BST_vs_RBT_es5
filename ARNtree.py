from ABRtree import *


RED = True
BLACK = False


# NODO ALBERO ROSSO NERO


class arn_Node(abr_Node):

    def __init__(self, key):
        abr_Node.__init__(self, key)
        self.color = RED



class ARN(ABR):

    # COSTRUTTORE
    def __init__(self):
        self.NIL = arn_Node(None)
        self.NIL.color = BLACK
        self.root = self.NIL

    def setRoot(self, key):
        self.root = arn_Node(key)
        self.root.color = BLACK
        self.root.p = self.NIL
        self.root.right = self.NIL
        self.root.left = self.NIL

    # ROTAZIONE DX
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.NIL:
            y.right.p = x
        y.p = x.p
        if x.p is self.NIL:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y

    # ROTAZIONE SX
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.p = x
        y.p = x.p
        if x.p is self.NIL:
            self.root = y
        elif x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.left = x
        x.p = y

    # INSERIMENTO
    def insert(self, key):
        self.h_ins = 0
        if self.root is self.NIL:
            self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        self.h_ins += 1
        if key <= currentNode.key:
            if currentNode.left is not self.NIL:
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = arn_Node(key)
                currentNode.left.p = currentNode
                currentNode.left.right = self.NIL
                currentNode.left.left = self.NIL
                self.insert_fixup(currentNode.left)
        elif key > currentNode.key:
            if currentNode.right is not self.NIL:
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = arn_Node(key)
                currentNode.right.p = currentNode
                currentNode.right.right = self.NIL
                currentNode.right.left = self.NIL
                self.insert_fixup(currentNode.right)

    def insert_fixup(self, z):
        while z.p.color is RED:
            if z.p is z.p.p.left:
                y = z.p.p.right
                if y.color is RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z is z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color is RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z is z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.left_rotate(z.p.p)
        self.root.color = BLACK

    # LISTA
    def in_list(self, x, A):
        if x is not self.NIL:
            self.in_list(x.left, A)
            A.append(x.key)
            self.in_list(x.right, A)

    def pre_list(self, x, A):
        if x is not self.NIL:
            A.append(x.key)
            self.pre_list(x.left, A)
            self.pre_list(x.right, A)

    def post_list(self, x, A):
        if x is not self.NIL:
            self.post_list(x.left, A)
            self.post_list(x.right, A)
            A.append(x.key)

    # SERIALIZZAZIONE
    def pre_string(self, x):
        if x != self.NIL and x is not None:
            self.A += str("R:" if x.color else "B:")+str(x.key)+" ["
            self.pre_string(x.left)
            self.A += ", "
            self.pre_string(x.right)
            self.A += "]"
        else:
            self.A += "_"

    # INSERIMENTO FIX_UP
    # ( riordina l'albero per mantenere le proprieta )



    # CANCELLAZIONE
    def delete(self, key):
        return False

    def deleteNode(self, z):
        return False
