#!/usr/bin/env python3
"""
更精确的图片外圈白色背景去除脚本
"""

from PIL import Image, ImageOps, ImageChops
import os
import numpy as np

def remove_outer_white_background(image_path, output_path, tolerance=15, border_ratio=0.05):
    """
    精确去除图片外圈的白色背景，保留内部的白色
    
    Args:
        image_path: 输入图片路径
        output_path: 输出图片路径
        tolerance: 颜色容差
        border_ratio: 外圈区域的比例（相对于图片尺寸）
    """
    # 打开图片
    img = Image.open(image_path)
    
    # 如果是 RGB 图像，转换为 RGBA
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    width, height = img.size
    pixels = np.array(img)
    
    # 计算外圈区域的边界
    border_width = int(width * border_ratio)
    border_height = int(height * border_ratio)
    
    # 创建掩码
    mask = np.zeros((height, width), dtype=np.uint8)
    
    # 定义外圈区域
    mask[:border_height, :] = 1  # 顶部
    mask[-border_height:, :] = 1  # 底部
    mask[:, :border_width] = 1  # 左侧
    mask[:, -border_width:] = 1  # 右侧
    
    # 处理外圈区域的白色像素
    for y in range(height):
        for x in range(width):
            if mask[y, x] == 1:
                r, g, b, a = pixels[y, x]
                if r > 255 - tolerance and g > 255 - tolerance and b > 255 - tolerance:
                    pixels[y, x] = [r, g, b, 0]
    
    # 保存处理后的图像
    processed_img = Image.fromarray(pixels)
    processed_img.save(output_path)
    print(f"处理完成: {output_path}")

def resize_image(image_path, output_path, size_percentage=50):
    """
    按比例缩小图片
    
    Args:
        image_path: 输入图片路径
        output_path: 输出图片路径
        size_percentage: 缩小比例，默认 50%
    """
    img = Image.open(image_path)
    
    # 计算新尺寸
    width, height = img.size
    new_width = int(width * size_percentage / 100)
    new_height = int(height * size_percentage / 100)
    
    # 缩小图片
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # 保存图像
    resized_img.save(output_path)
    print(f"缩小完成: {output_path}")

def smooth_edges(image_path, output_path, blur_radius=1):
    """
    平滑图片边缘
    
    Args:
        image_path: 输入图片路径
        output_path: 输出图片路径
        blur_radius: 模糊半径
    """
    img = Image.open(image_path)
    
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # 分离 alpha 通道
    r, g, b, a = img.split()
    
    # 对 alpha 通道进行模糊处理
    a = a.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # 重新合并
    img = Image.merge('RGBA', (r, g, b, a))
    img.save(output_path)
    print(f"边缘平滑完成: {output_path}")

if __name__ == "__main__":
    from PIL import ImageFilter
    
    # 图片路径
    images = [
        ("images/doubao-voice.jpg", "images/doubao-voice-processed-v2.png"),
        ("images/fanqie-novel-audiobook.jpg", "images/fanqie-novel-audiobook-processed-v2.png"),
        ("images/jianying-text-to-speech.jpg", "images/jianying-text-to-speech-processed-v2.png")
    ]
    
    # 处理每张图片
    for input_path, output_path in images:
        if os.path.exists(input_path):
            # 先去除外圈白色背景
            temp_path1 = f"{os.path.splitext(output_path)[0]}_nobg.png"
            remove_outer_white_background(input_path, temp_path1, tolerance=15, border_ratio=0.08)
            
            # 然后缩小图片
            temp_path2 = f"{os.path.splitext(output_path)[0]}_resized.png"
            resize_image(temp_path1, temp_path2, size_percentage=50)
            
            # 最后平滑边缘
            smooth_edges(temp_path2, output_path, blur_radius=1)
            
            # 删除临时文件
            os.remove(temp_path1)
            os.remove(temp_path2)
        else:
            print(f"文件不存在: {input_path}")
    
    print("\n所有图片处理完成！")
