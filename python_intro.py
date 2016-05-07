print("djangogirls")
if 3 > 2:
	print("Çalışıyor")


if 5 > 2:
	print("5 gerçekten de 2'den büyüktür")
else:
	print("2 5'den büyük değildir")
	
name = "ayşe"
if name == "ayşe":
    print("Selam ayşe")

    def hi():
    	print("Nasılsın?")
    	print("Selam")
    hi()

    def hi(name):
        if name == 'ayşe':
            print('Selam ayşe!')
        elif name == 'Zeynep':
            print('Selam Zeynep!')
        else:
            print('Selam yabancı!')

hi("Zeynep")

girls = ["Seda", "Berna", "Ebru"]
for name in girls:
	hi(name)
	print("Sıradaki")
