def computepay(hours, rate) :
   return hours * rate
def invalid_input() :
   print("Input Numeric Value")
while True :
   try :
      regular_rate = float(input("Hourly rate in dollars: "))
      break
   except :
      invalid_input()
      continue
while True :
   try :
      regular_hours = float(input("Regular Hours Worked: "))
      break
   except :
      invalid_input()
      continue
while True :
   try :
      overtime_hours = float(input("Overtime hours worked :"))
      break
   except :
      invalid_input()
      continue
overtime_rate = regular_rate * 1.5

regular_pay = computepay(regular_hours, regular_rate)
overtime_pay = computepay(overtime_hours, overtime_rate)
total_pay = regular_pay + overtime_pay

print("PAY : ", total_pay)
