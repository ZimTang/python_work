# 使用任意数量的关键字实参
def build_userProfile(first, last, **user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info


user_profile = build_userProfile('stephen', 'curry', location='cq', friend=['green'])
print(user_profile)
