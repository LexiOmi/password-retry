# 作業:密碼重設程式
# password: 'a123456'
# 讓使用者輸入密碼,最多3次

password = 'a123456'  #答案設在前面,以後要更改才不用到處改
i = 3
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼: ')
	if password != pwd:	
		print('密碼錯誤!')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('沒機會嘗試了,要鎖帳號了~')

	else:						#簡化
		print('登入成功!')
		break

