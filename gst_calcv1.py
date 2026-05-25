ac_cost = 30_000
old_gst = 28 / 100 # Calculating actual value for 28%
new_gst = 18 / 100
# This is a comment
old_total_cost = ac_cost + (ac_cost * old_gst)
new_total_cost = ac_cost + (ac_cost * new_gst)

total_savings = old_total_cost - new_total_cost

print(f"The Cost Saving of a AC at Rs.{ac_cost} with reduction in GST from {old_gst * 100:.2f}% to {new_gst * 100}%\
 is Rs.{total_savings} ")
