# Zakaria Kortam
# COMSC 78
# 3/22/2023
#1. Define the tree abstraction through the use of the tree function.
#2. Have the tree function call the is_tree() function that checks if the tree 
# is a list with at least 1 element, otherwise, it's false.
#It also checks each branch by recursively calling itself. If it passes both, it's a tree
# and true is returned.
# 3. The label function brings the label of the tree from the first element.
# 4. The branches function returns a list of the tree branches.
# 5. The count leaves functon recursively and increments the leaves. It first checks
# to see if the tree has other branches. If there are no more branches, then what it 
# is counting is a leaf.
# 6. Othweise, the function recursively calls itself and sums up the results.
# 7. Use the print tree function to print the tree. Call the indent function to indent it
# according to its status as the core, branch, or leaf.

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>> Zakaria Kortam - COMSC 78 >>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

# define the tree abstraction
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + branches

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True 

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# define a function to count the number of leaves in a tree
def count_leaves(tree):
    if not branches(tree):
        return 1
    else:
        return sum([count_leaves(branch) for branch in branches(tree)])

# define a function to print the tree with indentation
def print_tree(tree, indent=0):
    print(' ' * indent + str(label(tree)))
    for branch in branches(tree):
        print_tree(branch, indent + 2)

def main():
    t = tree('Tree Stump', [tree('Left Branch', [tree('Leaf a'), tree('Leaf b')]), tree('Right Branch', [tree('Leaf c')])])
    print_tree(t)
    print('\nTotal number of leaves:', count_leaves(t))
main()
