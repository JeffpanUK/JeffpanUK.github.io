#!/usr/bin/env python3
"""
去掉图片外圈白色背景的脚本
"""

from PIL import Image, ImageOps
import os

def remove_white_background(image_path, output_path, tolerance=10):
    """
    去掉图片的白色背景
    
    Args:
        image_path: 输入图片路径
        output_path: 输出图片路径
        tolerance: 颜色容差，数值越大，允许的颜色差异越大
    """
    # 打开图片
    img = Image.open(image_path)
    
    # 如果是 RGB 图像，转换为 RGBA
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # 获取像素数据
    pixels = img.getdata()
    
    # 创建新的像素数据
    new_pixels = []
    for pixel in pixels:
        # 检查像素是否接近白色
        r, g, b, a = pixel
        if r > 255 - tolerance and g > 255 - tolerance and b > 255 - tolerance:
            # 将白色背景设置为透明
            new_pixels.append((255, 255, 255, 0))
        else:
            new_pixels.append(pixel)
    
    # 创建新图像
    img_without_bg = Image.new('RGBA', img.size)
    img_without_bg.putdata(new_pixels)
    
    # 保存图像
    img_without_bg.save(output_path)
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

if __name__ == "__main__":
    # 图片路径
    images = [
        ("images/doubao-voice.jpg", "images/doubao-voice-processed.png"),
        ("images/fanqie-novel-audiobook.jpg", "images/fanqie-novel-audiobook-processed.png"),
        ("images/jianying-text-to-speech.jpg", "images/jianying-text-to-speech-processed.png")
    ]
    
    # 处理每张图片
    for input_path, output_path in images:
        if os.path.exists(input_path):
            # 先去掉白色背景
            temp_path = f"{os.path.splitext(output_path)[0]}_nobg.png"
            remove_white_background(input_path, temp_path)
            
            # 然后缩小图片
            resize_image(temp_path, output_path, size_percentage=50)
            
            # 删除临时文件
            os.remove(temp_path)
        else:
            print(f"文件不存在: {input_path}")
    
    print("\n所有图片处理完成！")
