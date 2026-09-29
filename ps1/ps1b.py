#!/usr/bin/python3

if __name__ == "__main__":
    annual_salary = float(input("Starting annual salary ($): "))
    portion_saved = float(input("Portion of salary to be saved (0-1): "))
    total_cost = float(input("Cost of your dream home ($): "))
    semi_annual_raise = float(input("Semi-annual raise (0-1): "))

    portion_down_payment = 0.25
    down_payment = portion_down_payment * total_cost
    monthly_savings = portion_saved * annual_salary / 12
    r = 0.04 / 12
    current_savings = 0
    t = 0
    
    while current_savings < down_payment:
        if t % 6 == 0 and t != 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_savings = portion_saved * annual_salary / 12

        current_savings += monthly_savings + (current_savings * r)
        t += 1
        print(t, monthly_savings, current_savings)

    print(f"Months to save up: {t}")
