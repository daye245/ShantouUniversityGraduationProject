import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# 1. 设置数据：日期和对应的计划事件
data = [
    ("2025-12-26", "开题报告"),
    ("2026-03-04", "中期检查"),
    ("2026-04-19", "毕业论文定稿"),
    ("2026-04-26", "抄袭检测"),
    ("2026-05-03", "指导老师评阅"),
    ("2026-05-06", "毕业答辩")
]

# 2. 解析日期和标签
dates = [datetime.strptime(d, "%Y-%m-%d") for d, l in data]
names = [l for d, l in data]

# 3. 设置绘图样式
fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
# ax.set_title("未来发展计划时间线", fontsize=16, pad=20)

# 设置线条高度（交错显示，避免重叠）
levels = np.tile([2, 2, 3, 2, 1, 3], int(np.ceil(len(dates)/6)))[:len(dates)]

# 4. 绘制主轴线
ax.axhline(0, color="black", linewidth=2, zorder=1)

# 5. 绘制垂直垂直杆（茎）
ax.vlines(dates, 0, levels, color="skyblue")
ax.scatter(dates, np.zeros_like(dates), c="navy", zorder=3, s=50) # 轴上的点

# 6. 添加文字标注
for i, (date, name) in enumerate(zip(dates, names)):
    ax.annotate(f"{date.strftime('%Y-%m')}\n{name}", 
                xy=(date, levels[i]),
                xytext=(0, 5 if levels[i] > 0 else -5), 
                textcoords="offset points",
                ha="center", 
                va="bottom" if levels[i] > 0 else "top",
                fontsize=10,
                fontproperties='SimHei') # 使用黑体支持中文

# 7. 格式化细节
ax.get_yaxis().set_visible(False) # 隐藏Y轴
plt.xticks(rotation=45)
# 移除边框
for spine in ["left", "top", "right"]:
    ax.spines[spine].set_visible(False)

plt.show()
# input("按回车键退出...") # 强制让程序停在这里