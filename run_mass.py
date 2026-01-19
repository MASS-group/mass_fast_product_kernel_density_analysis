# -*- coding: utf-8 -*-
import subprocess
import os

def run_mass(
        input_file,
        output_file,
        dim=2,
        method=3,
        n_x=300,
        k_type_x=1,
        b_x_ratio=1.0,
        n_y=300,
        k_type_y=1,
        b_y_ratio=1.0
):
    """
    调用 mass_pkdv.exe 生成 product kernel density。

    参数：
    - input_file: 输入数据文件路径
    - output_file: 输出文件路径
    - dim: 数据维度 (默认 2)
    - method: 算法方法 0:SCAN 1:SLAM 2:MASS_CR 3:MASS_OPT 4:RQS_kd 5:RQS_range
    - n_x, n_y: x, y 方向离散分辨率
    - k_type_x, k_type_y: 核函数类型 1:Epanechnikov 2:Triangular 3:Uniform
    - b_x_ratio, b_y_ratio: 带宽比例
    """

    # 获取 exe 文件的绝对路径
    exe_path = os.path.join(os.path.dirname(__file__), "bin", "mass_pkdv.exe")
    exe_path = os.path.abspath(exe_path)

    if not os.path.exists(exe_path):
        raise FileNotFoundError(f"mass_pkdv.exe not found at: {exe_path}")

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    # 设置 exe 的工作目录为 exe 所在目录，解决 QGIS 下 crash 问题
    cwd = os.path.dirname(exe_path)

    # 构造命令行参数
    cmd = [
        exe_path,
        input_file,
        output_file,
        str(dim),
        str(method),
        str(n_x),
        str(k_type_x),
        str(b_x_ratio),
        str(n_y),
        str(k_type_y),
        str(b_y_ratio)
    ]

    # 调用 exe
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=cwd,
            check=True
        )
        print(f"mass_pkdv finished successfully. Output saved to: {output_file}")
        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr)
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print("Error running mass_pkdv:", e)
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)
        raise

# ==============================
# 命令行模式调用
# ==============================
if __name__ == "__main__":
    # 默认示例数据
    input_file = os.path.join(os.path.dirname(__file__), "data", "UK_LD_Crime")
    input_file = os.path.abspath(input_file)
    output_file = os.path.join(os.path.dirname(__file__), "data", "plugin_output.txt")
    output_file = os.path.abspath(output_file)

    run_mass(input_file, output_file)
