# 作業:密碼重設程式
# password: 'a123456'
# 讓使用者輸入密碼,最多3次

password = 'a123456'  #答案設在前面,以後要更改才不用到處改
i = 3
while i > 0:
	pwd = input('請輸入密碼: ')
	if password != pwd:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會')
	else:						#簡化
		print('登入成功!')
		break

