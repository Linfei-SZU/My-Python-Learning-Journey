# 城市空气质量指数分析
aqi= [65, 78, 82, 95, 108, 72, 88, 115, 92, 102]#输入对应数据
print("近期空气质量指数:", aqi)

# 计算平均空气质量指数
average = sum(aqi) / len(aqi)
print(f"平均空气质量指数: {average}")

# 最高和最低空气质量指数
print(f"最高空气质量指数: {max(aqi)}, 最低空气质量指数: {min(aqi)}")

# 统计超过平均空气质量指数的天数
count = 0
for aqi in aqi:
    if aqi > 100:
        count += 1#给满足大于100的天数计数，每次加一

print(f"超过平均空气质量指数的天数: {count}")