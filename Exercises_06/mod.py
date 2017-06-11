#Reviewing module
class Mod:

	def call_review(self):
		import review
		user = review.Review("basile")
		return user.print_name()

	def call_holla(self):
		import holla
		return holla.username()

mod = Mod()
print mod.call_review()
print mod.call_holla()
