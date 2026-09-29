#!/usr/bin/python3

if __name__ == "__main__":
    global annual_salary_input
    annual_salary_input = float(input("Starting annual salary ($): "))

    global t_req
    t_req = 36
  
    def months_to_save(portion_saved_int: int) -> int:
        global annual_salary_input
        annual_salary = annual_salary_input
        total_cost =  1000000
        semi_annual_raise = 0.07

        portion_down_payment = 0.25
        down_payment = portion_down_payment * total_cost
        r = 0.04 / 12
        current_savings = 0

        portion_saved = float(portion_saved_int) / 10000
        monthly_savings = portion_saved * annual_salary / 12
        t = 0

        while current_savings < down_payment - 100: 
            if t % 6 == 0 and t != 0:
                annual_salary += annual_salary * semi_annual_raise
                monthly_savings = portion_saved * annual_salary / 12

            current_savings += monthly_savings + (current_savings * r)
            t += 1

        return t

    def search(p_min: int, p_max: int) -> (int, int):
        global t_req

        p_mid = int((p_min + p_max) / 2)
        t_p_max = months_to_save(p_min)
        t_p_mid = months_to_save(p_mid)
        t_p_min = months_to_save(p_max)
        print(f"{p_min}: {t_p_max}, {p_mid}: {t_p_mid}, {p_max}: {t_p_min}")
        
        if t_req >= t_p_min and t_req <= t_p_mid:
            return (p_mid, p_max)
        elif t_req >= t_p_mid and t_req <= t_p_max:
            return (p_min, p_mid)
        else:
            print("It isn't possible to pay the down payment in 36 months")
            exit()

    p_min = 0
    p_max = 10000
    i = 0

    while months_to_save(p_min) != t_req and months_to_save(p_max) != t_req:
        print(f"i: {i}, p_min: {p_min}, p_max: {p_max}")
        p_min, p_max = search(p_min, p_max)
        i += 1

    if months_to_save(p_min) == t_req:
        print(f"Best savings rate: {p_min / 10000}")
        
    if months_to_save(p_max) == t_req:
        print(f"Best savings rate: {p_max / 10000}")

    print(f"Steps: {i}")
