height = [74,74,72,72,73,69,69,71,76,71]
for i in range(len(height)):
    height[i] = height[i]*0.0254
print(height)
print('3 chiều cao đầu tiên',height[:3])
print('3 chiều cao cuối cùng',height[-3:])
print('chiều cao trung bình',sum(height)/len(height))
print('chiều cao lớn nhất',max(height))
print('chiều cao nhỏ nhất',min(height))
height.sort()
print(height)
height.reverse()
print(height)