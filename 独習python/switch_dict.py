rank = '甲'

msg = {
    '甲':'大変良い',
    '乙':'良い',
    '丙':'頑張れ'
}

if rank in msg:
    print(msg[rank])
else:
    print('???')