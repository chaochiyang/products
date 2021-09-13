import os #import 作業系統來溝通

if os.path.isfile('products.csv'):    # 請問OS有沒有這個檔案or地址
	print('yes! 找到檔案')
else:
	print('找不到檔案....')

#讀取檔案
products = []
with open('products.csv','r',encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:      
			continue 				# header 不儲存，直接跳過這一回合
		name, price = line.strip().split(',')   # 先用strip去掉換行符號，再split用,當作切割的標準
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱：')
	if name == 'q': # quit
		break
	price = input('請輸入商品價格：')
	products.append([name , price])  #將 小清單p[] 放入 大清單products[]之中
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0],'的價格:',p[1])

# 寫入檔案
with open('products.csv','w',encoding = 'utf-8') as f :
	f.write('商品,價格\n') #寫入欄位名稱
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')