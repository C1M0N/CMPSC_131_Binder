def get_weekly_pay(working_hours: float, hourly_pay: float) -> float:
    if working_hours <= 40:
        pay = hourly_pay * working_hours
        return pay
    else:
        pay =(working_hours - 40) * 1.5 * hourly_pay + 40 * hourly_pay
        return pay


def discount(price: float, discount_rate: float) -> float:
    discount_price = price * discount_rate * 0.01
    return discount_price


def get_final_cost(first_cloth_price: float, second_cloth_price: float) -> float:
    if first_cloth_price == second_cloth_price:
        final_cost = first_cloth_price * 2
        return final_cost
    elif first_cloth_price > second_cloth_price:
        final_cost = first_cloth_price + discount(second_cloth_price, 50)
        return final_cost
    elif first_cloth_price < second_cloth_price:
        final_cost = discount(first_cloth_price, 50) + second_cloth_price
        return final_cost