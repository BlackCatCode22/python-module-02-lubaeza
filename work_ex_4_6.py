def computepay(hours, rate):
  if hours > 40:
    reg = rate*hours
    otp = (hours - 40.0)*(rate*0.5)
    pay = reg + otp
    return pay #not included in video, I was getting "none"
  else:
    pay = hours*rate
    return pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hours)
fr = float(rate)

xp = computepay(fh,fr)

print("Pay: ", xp)

