class Nigiri:
    top = ""
    base = "しゃり"
    category = "にぎり"
    price = 0

    def show_attributes(self):
        print("top: {}, base: {}, category: {}".format(
            self.top, self.base, self.category))
        print("price: {}円".format(self.price))


class Katuso(Nigiri):
    top = "かつお"
    topping = "生姜とねぎ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))


k1 = Katuso()
k1.show_attributes()
