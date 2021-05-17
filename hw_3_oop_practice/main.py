from hw_3_oop_practice.house_sale import House, Realtor, Human


if __name__ == '__main__':

    house1 = House(40, 15000)
    house2 = House(165, 60000)
    house3 = House(150, 20000)

    realtor = Realtor('Jan', 0.20, [house1, house2, house3])
    person = Human('Anna', 34, 20000)

    person.info()
    person.make_money()
    realtor.info_houses()
    person.buy_house(house2)
    realtor.info_houses()
    person.buy_house(house3)
    realtor.info_houses()
    person.buy_house(house1)
    realtor.give_discount()
    realtor.sold_house(house1)
    realtor.info_houses()

