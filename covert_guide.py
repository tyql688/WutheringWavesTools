import os
from pathlib import Path

import cv2
from PIL import Image


def convert_image_format(input_path, output_path, output_format, quality=80, size_limit=5 * 1024 * 1024):
    # 使用 Pillow 来打开图像并获取格式信息
    with Image.open(input_path) as img:
        # 获取图像的实际格式
        image_format = img.format
        file_size = os.path.getsize(input_path)
        # 如果图像已经是 JPG 格式，跳过转换
        if file_size <= size_limit and image_format == 'JPEG':
            print(f"文件{file_size:.2f} {input_path} 已经是 JPG 格式，跳过转换")
            return
    # 读取图片
    img = cv2.imread(input_path)
    if img is None:
        print(f"无法读取图像文件，检查路径是否正确！{input_path}")
        return
    # 保存图片为新的格式
    cv2.imwrite(output_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    print(f"图片已成功转换为 {output_format} 格式并保存到 {output_path}")


def batch_convert_images(input_dir, output_dir, output_format):
    # 检查输入和输出目录是否存在
    if not os.path.exists(input_dir):
        print(f"输入目录 {input_dir} 不存在！")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 批量转换目录中的所有图片
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        if os.path.isfile(input_path):
            # 获取文件扩展名
            name, ext = os.path.splitext(filename)
            # 定义输出路径
            output_path = os.path.join(output_dir, f"{name}.{output_format.lower()}")
            # 转换格式
            try:
                convert_image_format(input_path, output_path, output_format)
            except Exception as e:
                print(f"转换 {input_path} 失败：{e}")


if __name__ == "__main__":
    MAIN_PATH = Path(__file__).parents[0] / 'resource'

    GUIDE_PATH = MAIN_PATH / 'pic/guide'
    # 小沐XMu 攻略库
    XMU_GUIDE_PATH = GUIDE_PATH / 'XMu'
    # Moealkyne 攻略库
    MOEALKYNE_GUIDE_PATH = GUIDE_PATH / 'Moealkyne'
    # 金铃子攻略组 攻略库
    JINLINGZI_GUIDE_PATH = GUIDE_PATH / 'JinLingZi'
    # 結星 攻略库
    JIEXING_GUIDE_PATH = GUIDE_PATH / 'JieXing'

    GUIDE_PATH_LIST = [XMU_GUIDE_PATH, MOEALKYNE_GUIDE_PATH, JINLINGZI_GUIDE_PATH, JIEXING_GUIDE_PATH]

    for guide_path in GUIDE_PATH_LIST:
        batch_convert_images(guide_path, guide_path, 'jpg')

    print(GUIDE_PATH)
