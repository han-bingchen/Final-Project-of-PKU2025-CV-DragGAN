
# 前言

对 [DragGAN 的原始仓库](https://github.com/XingangPan/DragGAN) 进行了一些调整，以适配较新的环境，此仓库及其所有代码仅用于非商业/研究目的，具体调整如下
- 更改了 `requirements.txt` 文件，这里参考了 [DragGAN：简介，安装，使用！-CSDN](https://blog.csdn.net/s_develop/article/details/132414315)
- 更改了 `bias_act.py` `filtered_lrelu.py` `upfirdn2d.py` ，以支持 `-std=c++17` 
- 更改了 `legacy.py` ，因为自定义模型是在 numpy 版本更高环境下创建的，引用了 `numpy._core` 模块，但当前环境（draggan）使用 numpy 1.23.5，其中 `numpy._core` 不存在


# 配置过程

以 Windows 系统为例，先搞个 conda 环境并激活

```
conda create -n draggan python=3.10.6
conda activate draggan
```

而后按照 `requirements.txt` 安装需要的库

```
pip install -r requirements.txt
```

使用下面的指令下载预训练模型

```
python scripts/download_model.py
```

而后尝试运行一下

```
python visualizer_drag.py checkpoints/stylegan2_dogs_1024_pytorch.pkl
```

---

你可能会发现下面的报错

```
AttributeError: module 'distutils' has no attribute '_msvccompiler'
```

这是通常是因为 `setuptools` 更新后， `distutils` 模块的 `msvccompiler` 属性被移除或不再支持，可以尝试进行降级

```
pip install setuptools==72.1.0
```

---

如果一切正常，应该会输出这样的东西

```
Setting up PyTorch plugin "bias_act_plugin"... Done.
Setting up PyTorch plugin "upfirdn2d_plugin"... Done.
```

注意，如果你的 GUI 窗口长时间未响应，可能不是因为模型加载速度慢，而是因为 set up 这两个 plugin 过程中失败了，需要切回终端检查一下

