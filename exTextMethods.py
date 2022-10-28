text ="Python es un lenguaje de propósito general con un uso muy extendido. Esto hace que aunque algunos lenguajes tienen mejor posición, como es el caso de R en tecnologías de Data Science y Machine Learning, Python permite abarcar proyectos de una manera mucho más rápida y eficiente por lo que si eres desarrollador, ingeniero o científico de datos no deberías perder más tiempo y comenzar especializarte en Python o al menos conocer sus bondades."
secondVar=text[250:300]
thirdVar = secondVar[2:10]

print(text.upper()) #.1
print(text[20:30]) #.2
print(text[150:210].lower()) #.3
print(secondVar.upper())#.4
print(thirdVar.lower())
print(secondVar,   thirdVar)#.5


# 1- Show all text in uppercase.
# 2- Display the text from position 20 to 30.
# 3- Display the text from position 150 to 210 in lowercase.
# 4- Create a second variable containing the previous text from position 250 to 300 and display it on the screen in uppercase.
# 5- Create a third variable containing the text of the second variable from position 2 to 10, and convert it to lowercase and display it on the screen using the concatenation of the second and third variables.

