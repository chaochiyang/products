products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q': # quit
		break
	price = input('請輸入商品價格：')
	products.append([name , price])  #將 小清單p[] 放入 大清單products[]之中
print(products)

for p in products:
	print(p[0],'的價格:',p[1])
	