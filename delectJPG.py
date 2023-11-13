import os

folder_path = r"D:\BaiduNetdiskDownload\ai\sd-webui-aki\sd-webui-aki-v4.4\outputs\txt2img-images\10-13"  # 替换为你要删除 PNG 文件所在文件夹的路径

def delete_jpg_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"{file_path} 文件删除成功！")

delete_jpg_files(folder_path)
