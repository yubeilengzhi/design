import random


def getPrime(lower, upper):
    """

    :param lower: 区间最小值
    :param upper: 区间最小值
    :return: 区间内所有的质数
    """
    for num in range(lower, upper + 1):
        # 素数大于 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                # print(num)
                return num

# A. 系统设置阶段 KGC
KGC = {}
# 获取大质数 p 1009
p = getPrime(999, 1050)
# 程序很难表示无穷大 ，用 （-1000，1000） 作为范围
K_SN = random.randrange(-1000,1000) # SNS
K_UE = random.randrange(-1000,1000) # UES
K_MD = random.randrange(-1000,1000) # MDS
x = random.randrange(-1000,1000)




# 生成两个单向哈希函数
H1 = hash((0,1))
print(H1)





# B. 注册阶段
ID_UE_i = 1
ID_SN_j = 2
ID_MD_i = 3

# 服务网络注册
KGC['ID_SN_j'] = ID_SN_j
S_j = random.randint(-1000,1000)
# print(S_j)
KGC['S_j'] = S_j

T_S_j = S_j
Chebu_SN_j = T_S_j*(K_SN or ID_SN_j)%p
# print(Chebu_SN_j)
KGC['Chebu_SN_j'] = Chebu_SN_j

print(KGC)

# 设备注册
SC = {} # UEI 的智能卡 SC
KGC['ID_UE_i'] = ID_UE_i
U_i = random.randint(-1000,1000)
KGC['U_i'] = U_i
K_UE_i = random.randint(-1000,1000)
KGC['K_UE_i'] = K_UE_i
T_U_i = U_i
Chebu_UE_i = T_U_i*(K_UE_i or ID_UE_i) % p
KGC['Chebu_UE_i'] = Chebu_UE_i
# KGC 将信息加载到 SC 中
SC['ID_UE_i'] = KGC['ID_UE_i']
SC['Chebu_UE_i'] = KGC['Chebu_UE_i']
SC['U_i'] = KGC['U_i']

print(KGC)
# hash 函数运算





# MTC 设备注册
m_g = random.randint(-1000,1000)
K_mdg = random.randint(-1000,1000)
m_i = random.randint(-1000,1000)
K_mdi = random.randint(-1000,1000)
KGC['ID_MD_i'] = ID_MD_i
KGC['m_g'] = m_g
KGC['K_mdg'] = K_mdg
KGC['m_i'] = m_i
KGC['K_mdi'] = K_mdi
T_MG = m_g
T_MI = m_i
GID = 1
KGC['GID'] = GID
Chebu_MD_g = T_MG*(K_mdg or GID) % p
KGC['Chebu_MD_g'] = Chebu_MD_g
Chebu_MD_i = T_MI*(K_mdi or GID or ID_MD_i) % p
KGC['Chebu_MD_i'] = Chebu_MD_i

print(KGC)

SC['ID_MD_i'] = ID_MD_i
SC['GID'] = GID
SC['Chebu_MD_g'] = Chebu_MD_g
SC['Chebu_MD_i'] = Chebu_MD_i
SC['m_g'] = m_g
SC['m_i'] = m_i
# 哈希运算





# 终端认证和秘钥协议
Chebu_U_i_1 = T_U_i*(K_SN or ID_SN_j) % p
Chebu_U_i_2 = T_U_i*(K_UE or ID_UE_i) % p
x_i = random.randint(-1000,1000)
T_x_i = x_i
Chebu_x_i = T_x_i*(K_SN or ID_SN_j) % p
K_1 = T_x_i*(T_S_j*(K_SN or ID_SN_j)%p) % p
K_2 = T_U_i*(T_S_j*(K_SN or ID_SN_j)%p) % p
# 哈希运算





# 加密
ENC_K1 = K_1
E_1 = ENC_K1*(ID_UE_i or T_U_i*(K_SN or ID_SN_j) % p or T_U_i * (K_UE_i or ID_UE_i) % p or T_U_i*(K_UE or ID_UE_i) % p)

print('E_1',E_1)

# SN_j 工作方式
K_1_n = T_S_j*(T_x_i*(K_SN or ID_SN_j) % p) % p

K_2_n = T_S_j*(T_U_i*(K_SN or ID_SN_j) % p) % p

print('K_1_n:{},K_2_n:{}'.format(K_1_n,K_2_n))




