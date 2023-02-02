import sys 
n = int(sys.stdin.readline()) # 1 <= N <= 26

nodes = [
    sys.stdin.readline().rstrip().split()
    for _ in range(n)
]

# make tree 
tree = {}

for p, l, r in nodes :
    tree[p] = [l, r]

# 전위 순회 (Preorder Traversal)
def preorder(root) :
    if root != '.' :
        print(root, end = '')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위 순회 (Inorder Traversal)
def inorder(root) :
    if root != '.' :
        inorder(tree[root][0])
        print(root, end= '')
        inorder(tree[root][1])

# 후위 순회 (Post Traversal)
def postorder(root) :
    if root != '.' :
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')