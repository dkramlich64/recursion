import turtle
MINIMUM_BRANCH_LENGTH = 5
def build_tree(t, branch_length, shorten_by, angle):
  if branch_length > MINIMUM_BRANCH_LENGTH:
    if branch_length <= (MINIMUM_BRANCH_LENGTH * 2):
      t.color('#008000')
      print('green')
    else:
      t.color('#333300')
      print('dark brown')
    t.forward(branch_length)
    new_length = branch_length - shorten_by
    t.left(angle)
    build_tree(t, new_length, shorten_by, angle)
    t.right(angle * 2)
    build_tree(t, new_length, shorten_by, angle)
    t.left(angle)
    if branch_length <= (MINIMUM_BRANCH_LENGTH * 2):
      t.color('#008000')
      print('green')
    else:
      t.color('#333300')
      print('dark brown')
    t.backward(branch_length)
    print(branch_length)
tree = turtle.Turtle()
tree.speed(9)
tree.setheading(90)
tree.color('#333300')
build_tree(tree, 50, 5, 15)
turtle.mainloop()
