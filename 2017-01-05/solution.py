from TreeNode import TreeNode

tree = TreeNode(
    1,
    TreeNode(2,
             TreeNode(3,
                      TreeNode(4),
                      TreeNode(5)
                      ),
             TreeNode(6)
             ),
    TreeNode(7,
             TreeNode(8),
             TreeNode(9,
                      TreeNode(10)
                      )
             )
)


def serialize(root):
  result = ""

  result += "{} {} {}".format(
    root.value,
    serialize(root.left) if root.left else "_",
    serialize(root.right) if root.right else "_",
  )
  
  return result

print serialize(tree)
