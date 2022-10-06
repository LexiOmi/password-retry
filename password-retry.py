# 作業:密碼重設程式
# password: 'a123456'
# 讓使用者輸入密碼,最多3次

i = 3
while i > 0:
	password = input('請輸入密碼: ')
	if password != 'a123456':
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會')
	elif password == 'a123456':
		print('登入成功!')
		break



