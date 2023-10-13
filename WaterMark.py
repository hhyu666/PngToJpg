import os
from PIL import Image, ImageDraw, ImageFont

def convert_png_to_jpg(input_path, output_path, prefix=""):
    # 创建输出目录
    os.makedirs(output_path, exist_ok=True)

    # 获取目标文件夹中已存在的文件名列表
    existing_files = set(os.listdir(output_path))

    # 遍历输入目录中的所有文件和文件夹
    count = 1
    for filename in sorted(os.listdir(input_path)):
        filepath = os.path.join(input_path, filename)

        if os.path.isfile(filepath) and filename.endswith(".png"):
            # 检查文件名是否已存在于目标文件夹中
            new_filename = f"{prefix}{count}.png"  # 设置新的文件名（带前缀）

            if new_filename in existing_files:
                print(f"Skipped {filename} as it already exists in the target folder.")
                continue

            # 打开 PNG 图像
            png_image = Image.open(filepath)

            # 打开水印图像
            watermark = Image.open(watermark_path).convert("RGBA")

            # 添加水印
            jpg_image = png_image.copy()
            watermark_width, watermark_height = watermark.size
            x = jpg_image.width - watermark_width - 1  # 水印右侧保留 10 像素空白
            y = jpg_image.height - watermark_height - 1  # 水印底部保留 10 像素空白
            jpg_image.paste(watermark, (x, y), mask=watermark)

            # 构建输出文件路径
            output_filepath = os.path.join(output_path, new_filename)

            # 保存图像
            jpg_image.save(output_filepath)

            print(f"Watermark added to {filename} and saved as {new_filename}.")
            count += 1

        elif os.path.isdir(filepath):
            # 构建子目录路径
            subdir_name = os.path.basename(filepath)
            new_output_path = os.path.join(output_path, subdir_name)

            # 递归调用函数处理子目录
            convert_png_to_jpg(filepath, new_output_path, prefix="")

            # 重置计数器
            count = 1

input_path = r"D:\BaiduNetdiskDownload\ai\sd-webui-aki\sd-webui-aki-v4.4\outputs\txt2img-images"
output_path = r"D:\BaiduNetdiskDownload\ai\sd-webui-aki\sd-webui-aki-v4.4\outputs\batch-processing"
watermark_path = r"D:\BaiduNetdiskDownload\ai\sd-webui-aki\sd-webui-aki-v4.4\outputs\water2.png"

# 调用函数进行转换
# convert_images(input_path, output_path)
convert_png_to_jpg(input_path,output_path)
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
