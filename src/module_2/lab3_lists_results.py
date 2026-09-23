results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad"]
print(results)
results.extend(["Bowser", "Donkey Kong Jr."])
results.remove("Bowser")
print(results)
results.insert(0, "Bowser")
print(results.index("Mario"))
results.reverse()
print(results)