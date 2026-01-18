# 前言

对 [DragDiffusion 的原始仓库](https://github.com/Yujun-Shi/DragDiffusion) 进行了一些调整，以适配自己的电脑环境，此仓库及其所有代码仅用于非商业/研究目的，具体调整如下
- 更改了 `environment.yaml` 文件，加入 `https://mirrors.aliyun.com/pypi/simple` 以解决相关库找不到的问题
- 更改了 `lora_utils.py` `ui_utils.py` `run_drag_diffusion.py` ，调整 vae 的读取路径为 `./model_name/vae` ，而非原先的 `./model_name`
- 将 `demo.queue().launch(share=True, debug=True)` 调整为 `share=False` ，禁用共享链接，因为我是 Windows 系统

# 配置过程

整体上按照官方流程即可，而后调整 `gradio` 版本（参考 [Train Lora Error · Issue #77 · Yujun-Shi/DragDiffusion](https://github.com/Yujun-Shi/DragDiffusion/issues/77)）

```
pip install -U gradio==3.50.2
```

同时，请确保环境中的 `pytorch` 是 GPU 版本而非 CPU 版本，不然训练会很慢

最后运行 `python drag_ui.py` 以启动

配置与使用过程中可能遇到一些问题

Q1： 配置环境时，安装 `tb-lightly` 失败

虽然我在 `environment.yaml` 加入了相应链接，但是尚未测试更改后能否正常配置（因为我是在报错后，让 ide 里的 ai 帮我配置的），如果还是不行，可以先删掉其中的  `tb-lightly` 库这一行，而后单独安装

```
python -m pip install tb-nightly -i https://mirrors.aliyun.com/pypi/simple
```

---

Q2：运行 `python drag_ui.py` 报错 `Could not create share link` 

这是我一开始遇到的问题，更改文件后应该遇不到了，具体如下

```
Could not create share link. Missing file: C:\Users\35722\anaconda3\envs\dragdiff\lib\site-packages\gradio\frpc_windows_amd64_v0.2.

Please check your internet connection. This can happen if your antivirus software blocks the download of this file. You can install manually by following these steps:


1. Download this file: https://cdn-media.huggingface.co/frpc-gradio-0.2/frpc_windows_amd64.exe
2. Rename the downloaded file to: frpc_windows_amd64_v0.2
3. Move the file to this location: C:\Users\35722\anaconda3\envs\dragdiff\lib\site-packages\gradio
```

但是当我把这个文件下载下来并重命名，又报错

```
Could not create share link. Please check your internet connection or our status page: https://status.gradio.app
```

上网搜索后发现这通常是没有权限导致的，可以chmod +x frpc_linux_amd64_v0.2，但这个指令是对于 Linux 系统的，而我是windows系统，同时这个文件重命名后不能带 `.exe` 后缀（否则仍会报错找不到），所以干脆不让创建共享链接了

---

Q3： 训练 LoRA 过程报错 `TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。`

请检查你的网页 `UI` 底下 `Base Model Config` 一栏，如果用的是下面这些默认的模型（需要在线连接），可能是由于网络连接问题导致的，可以考虑下载模型到本地的 `local_pretrained_models` 文件夹

```
runwayml/stable-diffusion-v1-5
gsdf/Counterfeit-V2.5
stablediffusionapi/anything-v5
SG161222/Realistic_Vision_V2.0
```

下载模型后，请确保文件夹结构类似于这样（不一定完全一样，但是不要单独下载一个 `.safetensors` 文件，而是要保持文件夹结构）

```
local_pretrained_models/stable-diffusion-v1-5/
├── model_index.json
├── unet/
│   ├── config.json
│   └── diffusion_pytorch_model.safetensors
├── vae/
│   ├── config.json
│   └── diffusion_pytorch_model.safetensors
├── text_encoder/
│   ├── config.json
│   └── model.safetensors
├── scheduler/
│   └── scheduler_config.json
└── tokenizer/
    ├── tokenizer_config.json
    └── vocab.json
```

下载后，应该能在 `Base Model Config` 中看到本地模型的选项，把 `Diffusion Model Path` 和 `VAE choice` 都选为本地模型

此外训练 LoRA 过程还可能出现各种千奇百怪的错误，请等待命令行出现具体的报错提示后，向 ai 询问或者上网搜索，一切正常的话，在点击 `Train LoRA` 后，应该能在网页 `UI` 看到训练进度条