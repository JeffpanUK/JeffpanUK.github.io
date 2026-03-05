#!/usr/bin/env python3
"""
将用户提供的图片转换为 favicon.ico 文件
"""

from PIL import Image
import os

def convert_to_favicon(input_path, output_path):
    try:
        # 打开图片
        img = Image.open(input_path)
        
        # 调整图片尺寸为 16x16 和 32x32
        sizes = [16, 32, 48, 64, 128, 256]
        
        # 创建一个列表，包含不同尺寸的图片
        images = []
        for size in sizes:
            # 缩小图片
            resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
            # 转换为 RGBA 格式（支持透明）
            if resized_img.mode != 'RGBA':
                resized_img = resized_img.convert('RGBA')
            images.append(resized_img)
        
        # 保存为 favicon.ico
        images[0].save(output_path, format='ICO', save_all=True, append_images=images[1:], quality=100)
        
        # 同时保存一个 32x32 的 PNG 版本
        img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
        if img_32.mode != 'RGBA':
            img_32 = img_32.convert('RGBA')
        img_32.save('favicon-32x32.png', format='PNG', quality=100)
        
        print(f"成功转换为 favicon.ico 文件，包含 {len(sizes)} 种尺寸")
        print("同时创建了 favicon-32x32.png 文件")
        
    except Exception as e:
        print(f"转换失败: {e}")

if __name__ == "__main__":
    input_file = "favicon-new.jpg"
    output_file = "favicon.ico"
    
    if os.path.exists(input_file):
        convert_to_favicon(input_file, output_file)
    else:
        print(f"文件不存在: {input_file}")
