
user_info = {"First_name": "Faisal", "Last_name": "Porag", "age": 25, "Position": "Assistant Manager" }

print(user_info)

print(user_info["First_name"])
print(user_info["Last_name"])
print(user_info["Position"])


month_convertion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}

print(month_convertion["Feb"])
print(month_convertion.get("Feb"))
print(month_convertion.get("Febs", "Not a valid key"))