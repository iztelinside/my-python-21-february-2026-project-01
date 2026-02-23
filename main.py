
# number = 100
# text = "Hello World!"
# print(number)
# print(text)
# for i in text:
#     # print(i)
#     if i == '!':
#         print(i)
#     elif i == 'b':
#         print(i)

listNumbers = [100, 60, 70, 80, 500]
print(listNumbers)
print(len(listNumbers))
print(max(listNumbers))
print(min(listNumbers))
print(sum(listNumbers))
print(listNumbers[0])
print(listNumbers[-1])
print(listNumbers[2])
listNumbers.append(1000)
print(listNumbers)
listNumbers.remove(500)
print(listNumbers)
print(sum(listNumbers))
listNumbers[2] = True
print(listNumbers)
listNumbers[3] = "Hello World"
print(listNumbers)
print(len(listNumbers))

listNumbers.insert(2, 105)
print(listNumbers)

# len = int(input("Enter the length of the list: "))
# element_list = []
# i = 0
# while i < len:
#     string = input("Enter the element #"+ str(i+1)+ ":")
#     element_list.append(string)
#     # element_list.append(element_list[i])
#     i += 1
# print(element_list)
textSlogan = "Power is nothing without control"
slogan = textSlogan.split(" ")
print(slogan)
i = 0
for i in range(len(slogan)):
    slogan[i] = slogan[i].capitalize()
print(slogan)

