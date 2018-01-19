from decimal import Decimal, ROUND_DOWN

# This app is to caluclate my weekly earnings without tax included.

class WeeklyPay():

	def __init__(self, p_rate, h_worked, layover=0):
		self.p_rate 	= p_rate
		self.h_worked 	= h_worked
		self.layover	= layover

	def pay_rate(self):

		p_rate = self.p_rate
		h_worked = self.h_worked
		layover = self.layover
		# hours less then 44
		if h_worked <= 44:
			sum_h_worked = h_worked * p_rate
			# Hours less then 44 hours
		else:
			regular_h = p_rate * 44
			print(regular_h)
			ot_hours = h_worked % 44
			print(ot_hours)
			over_time = p_rate * 1.5 * ot_hours
			print(over_time)
			sum_h_worked = regular_h + over_time
			
			
		def lay_over(self):

			layover = self.layover

			if layover == 0:
				return 0
			# Standard rate of $50 per day layover.
			if layover >= 1:
				base_rate = layover * 50
				return base_rate

		sum_h_worked = sum_h_worked + lay_over(self)
		return f"{round(sum_h_worked, 2)} is you weekly Pay!\n{lay_over(self)} is your layover."

user_pay = float(input("Insert your pay: "))
user_hour = float(input("Insert hours work : "))
user_layover = int(input("input if applicable: "))

WP = WeeklyPay

my_user = WP(user_pay, user_hour, user_layover)
print(my_user.pay_rate())
