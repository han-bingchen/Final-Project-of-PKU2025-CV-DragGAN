# 前言

对 [PTI 的原始仓库](https://github.com/danielroich/PTI) 进行了一些调整，以适配自己的电脑环境，此仓库及其所有代码仅用于非商业/研究目的

# 配置过程

整体上按照官方流程即可，具体配置与参数说明请见官方 readme ，使用流程如下
- 运行 `align_data.py` ，在主函数修改要编辑的图像，将其裁剪到 1024×1024
- 运行 `run_pti.py` ，将输入图像放到 `./input` 文件夹，输出 `.pt` 格式的模型与 latent code
- 运行 `pt2pkl.py` ，将 `.pt` 格式的模型转换为 `.pkl` 
