#!/usr/bin/env python3
"""
创建一个简单的 J 图标作为 favicon
"""

from PIL import Image, ImageDraw, ImageFont

def create_favicon():
    # 创建一个 16x16 的图标
    width = 16
    height = 16
    
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 使用蓝色背景
    draw.rectangle([0, 0, width, height], fill=(0, 123, 255, 255))
    
    # 尝试绘制 J 字母
    try:
        # 尝试使用默认字体
        font = ImageFont.truetype("arial.ttf", 10)
    except IOError:
        # 如果没有找到字体，使用默认字体
        font = ImageFont.load_default()
    
    # 绘制白色的 J 字母
    draw.text((3, 2), "J", font=font, fill=(255, 255, 255, 255))
    
    # 保存为 favicon.ico
    img.save("favicon.ico")
    print("favicon.ico 创建成功！")
    
    # 同时创建一个 32x32 的版本
    img32 = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    draw32 = ImageDraw.Draw(img32)
    draw32.rectangle([0, 0, 32, 32], fill=(0, 123, 255, 255))
    
    try:
        font32 = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font32 = ImageFont.load_default()
    
    draw32.text((7, 5), "J", font=font32, fill=(255, 255, 255, 255))
    img32.save("favicon-32x32.png")
    print("favicon-32x32.png 创建成功！")

if __name__ == "__main__":
    create_favicon()
