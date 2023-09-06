from PIL import Image
import os


def convert_png_to_jpg(input_path, output_path):
    # 创建输出目录
    os.makedirs(output_path, exist_ok=True)

    # 遍历输入目录中的所有文件
    for i, filename in enumerate(os.listdir(input_path), start=1):
        if filename.endswith(".png"):
            # 打开 PNG 图像
            png_image = Image.open(os.path.join(input_path, filename))

            # 将 PNG 图像转换为 JPEG 图像
            jpg_image = png_image.convert("RGB")

            # 构建输出文件路径
            output_filename = f"{i}.jpg"
            output_filepath = os.path.join(output_path, output_filename)

            # 保存 JPEG 图像
            jpg_image.save(output_filepath, "JPEG")

            print(f"Converted {filename} to {output_filename}.")


# 设置输入和输出路径
input_path = r"D:\BaiduNetdiskDownload\sd-webui-aki\sd-webui-aki-v4.1\outputs\Cyber_+"
output_path = r"D:\BaiduNetdiskDownload\sd-webui-aki\sd-webui-aki-v4.1\outputs\batch-processing"

# 调用函数进行转换
convert_png_to_jpg(input_path, output_path)
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
