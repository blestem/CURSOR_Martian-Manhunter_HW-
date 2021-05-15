from hw_3_oop_practice.house_sale import house2, house3, house1, person, realtor


if __name__ == '__main__':
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