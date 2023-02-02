# 전위 순회(Preorder traversal) : 부모->왼쪽->오른쪽
# 중위 순회(Inorder traversal)  : 왼쪽->부모->오른쪽
# 후위 순회(Postorder traversal): 왼쪽->오른쪽->부모

# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며
# 알파벳 순서대로 주어지는 것은 아님
# 항상 A가 루트 노드가 된다.
# 자식노드가 없는 경우에는 .으로 표현

import sys 
n = int(sys.stdin.readline()) # 1<= N <= 26

nodes = [
    sys.stdin.readline().rstrip().split()
    for _ in range(n)
]

# 트리를 dictionary를 사용하여 표현 
tree = {}

for p, l, r in nodes :
    tree[p] = [l, r]

# Preorder Traversal
def preorder(root) :
    if root !='.' :
        print(root, end ='') # root
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right

def inorder(root) :
    if root != '.' :
        inorder(tree[root][0]) # left
        print(root, end ='') # root
        inorder(tree[root][1]) # right

def postorder(root) :
    if root != '.' :
        postorder(tree[root][0]) # left
        postorder(tree[root][1]) # right
        print(root, end ='') # root 

preorder('A')
print()
inorder('A')
print()
postorder('A')