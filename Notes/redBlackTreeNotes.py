## Red/Black Tree Notes

# BST
# - All nodes are Red or Black
# 'None' are Black
# Root is Black
# Nodes are added as red nodes
# All paths to the bottom have the same number of black nodes
# No red node has a red child
#
#
# AVL vs. Red/Black
#
# AVL:
# Rotates frequently on insert/remove
# more balanced
#
# Red/Black
# Does not rotate often
# Less balanced
#
# If we're editing our trees more frequently, Red/Black trees are better.
# If we're not editing our trees frequently but searching is more important, AVL trees are better.
#
#
# Add:
#   double red:
#       when uncle and aunt is red
#       uncle and parent and grandparent change color
#       check at grandparent for new double red rotation
#   when uncle is black:
#       when currNode is innerChild:
#           rotate at parent to make currNode outerChild
#       when currNode is outerChild:
#           rotate so currNode is pulled up
#           recolor parent and grandparent
#
# Remove(currNode):
#   Binary search tree remove
#   -one or no child:
#       if we delete a red node:
#           do nothing
#       if we delete a black node:
#           if the child was red, recolor the child to black
#       if we delete a black node and the replacement is black:
#           it becomes a double black node
#           fixRemove(nodeRemoved)
#
# fixRemove(currNode):
#   if sibling is red:
#       swap colors between sibling and parent
#       rotate at parent, pulling double black down
#       call fix-remove again
#   if sibling has two black children:
#       sibling becomes red
#   if parent was red, change to black
#       finish
#   if parent was black, parent becomes double black
#       fixRemove(currNode.parent)
#   if sibling had one red node child and child node is on inside:
#       swap sibling and inner child
#       rotate on sibliong to pull inner child up
# if red child on outside sibling:
#       swap color of parent & sibling
#       rotate at parent to pull double black down
#       change outer child to black
