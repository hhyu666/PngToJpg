import os
from PIL import Image


def convert_png_to_jpg(input_path, output_path, prefix=""):
    # 创建输出目录
    os.makedirs(output_path, exist_ok=True)

    # 遍历输入目录中的所有文件和文件夹
    count = 1
    for filename in os.listdir(input_path):
        filepath = os.path.join(input_path, filename)

        if os.path.isfile(filepath) and filename.endswith(".png"):
            # 打开 PNG 图像
            png_image = Image.open(filepath)

            # 将 PNG 图像转换为 JPEG 图像
            jpg_image = png_image.convert("RGB")

            # 构建输出文件路径
            new_filename = f"{prefix}{count}.jpg"  # 设置新的文件名
            output_filepath = os.path.join(output_path, new_filename)

            # 保存 JPEG 图像
            jpg_image.save(output_filepath, "JPEG")

            print(f"Converted {filename} to {new_filename}.")
            count += 1

        elif os.path.isdir(filepath):
            # 构建新的前缀
            new_prefix = f"{prefix}{count}_"

            # 构建子目录路径
            new_output_path = os.path.join(output_path, f"{prefix}{count}")

            # 递归调用函数处理子目录
            convert_png_to_jpg(filepath, new_output_path, new_prefix)

            count += 1
# 设置输入和输出路径
input_path = r"D:\BaiduNetdiskDownload\sd-webui-aki\sd-webui-aki-v4.1\outputs\txt2img-images"
output_path = r"D:\BaiduNetdiskDownload\sd-webui-aki\sd-webui-aki-v4.1\outputs\batch-processing"

# 调用函数进行转换
convert_png_to_jpg(input_path, output_path)