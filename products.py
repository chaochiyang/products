products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q': # quit
		break
	price = input('請輸入商品價格：')
	p = []
	p.append(name)
	p.append(price)     # 7~9行  可簡化--> p = [name , price ]
	products.append(p)  #將 小清單p[] 放入 大清單products[]之中
print(products)

products[0][0]
