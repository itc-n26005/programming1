def show_message(num=0):

  def decolate(func):
    if num == 0:
      flag = "Red"
    else:
      flag = "Blue"

    print("=== flag: ", flag)
    func()
    print("====")

  def show_selection(num=num):
    if num == 0:
      print("Selection is ", num, "which may be the default")
    else:
      print("Your choice is ", num)

  decolate(show_selection)

show_message(0)
show_message(1)
