marks={
    "Chandan":90,
    "Hari":54,
    "Rohan":87,
    98:"chanddd"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Chandan":96,"Renuka":67})
print(marks.get("Chandan2")) # prints none
print(marks["Chandan2"]) # taking error