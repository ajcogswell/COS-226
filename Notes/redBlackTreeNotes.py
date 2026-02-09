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
# Remove:
#   double black:
#       when sibling is red, rotate and recolor
#       when sibling is black, recolor sibling and parent
#       when sibling is black and parent is red, rotate and recolor
#       when sibling is black and parent is black, rotate and recolor
# 