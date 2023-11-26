def computepay(hours, rate):
    return hours * rate

regular_rate = float(input("Hourly rate in dollars: "))
regular_hours = float(input("Regular hours worked: "))
overtime_hours = float(input("Overtime hours worked: "))

regular_pay = computepay(regular_hours, regular_rate)
overtime_pay = computepay(overtime_hours, regular_rate * 1.5)
total_pay = regular_pay + overtime_pay

print(f"This pay period you earned: ${total_pay:.2f}")
