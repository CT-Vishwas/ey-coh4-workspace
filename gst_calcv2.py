# Input Section
ac_cost = float(input("Enter the AC Price: "))
old_gst = float(input("Enter old GST Rate: ")) / 100 # Calculating actual value for 28%
new_gst = float(input("Enter new GST Rate: ")) / 100

# Logic or calculation
old_total_cost = ac_cost + (ac_cost * old_gst)
new_total_cost = ac_cost + (ac_cost * new_gst)

total_savings = old_total_cost - new_total_cost

# Output
print(f"The Cost Saving of a AC at Rs.{ac_cost} with reduction in GST from {old_gst * 100:.2f}% to {new_gst * 100}%\
 is Rs.{total_savings} ")
