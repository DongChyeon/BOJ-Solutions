def preorder(node):
    print(node[0], end='')
    if node[1] != '.':
        preorder(tree[ord(node[1]) - 65])
    if node[2] != '.':
        preorder(tree[ord(node[2]) - 65])
        
def inorder(node):
    if node[1] != '.':
        inorder(tree[ord(node[1]) - 65])
    print(node[0], end='')
    if node[2] != '.':
        inorder(tree[ord(node[2]) - 65])
        
def postorder(node):
    if node[1] != '.':
        postorder(tree[ord(node[1]) - 65])
    if node[2] != '.':
        postorder(tree[ord(node[2]) - 65])
    print(node[0], end='')

# 2차원 리스트를 사용한 트리 구성 [[루트, 왼쪽, 오른쪽]]
n = int(input())
tree = [[] for _ in range(n)]

for _ in range(n):
    command = input().split()
    tree[ord(command[0]) - 65].append(command[0])
    tree[ord(command[0]) - 65].append(command[1])
    tree[ord(command[0]) - 65].append(command[2])
   
preorder(tree[0])
print()
inorder(tree[0])
print()
postorder(tree[0])
