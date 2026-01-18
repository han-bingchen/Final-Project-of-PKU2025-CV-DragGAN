import pickle
import torch
import argparse
from configs import paths_config, global_config


def load_generators(model_id, image_name):
    with open(paths_config.stylegan2_ada_ffhq, 'rb') as f:
        old_G = pickle.load(f)['G_ema'].to(global_config.device)

    with open(f'{paths_config.checkpoints_dir}/model_{model_id}_{image_name}.pt', 'rb') as f_new:
        new_G = torch.load(f_new).to(global_config.device)

    return old_G, new_G


def export_updated_pickle(new_G, image_name):
    print("Exporting large updated pickle based off new generator and ffhq.pkl")
    with open(paths_config.stylegan2_ada_ffhq, 'rb') as f:
        d = pickle.load(f)

    # 确保模型在 CPU 上并处于评估模式
    if 'G' in d:
        d['G'] = d['G'].eval().requires_grad_(False).cpu()
    d['G_ema'] = new_G.eval().requires_grad_(False).cpu()
    if 'D' in d:
        d['D'] = d['D'].eval().requires_grad_(False).cpu()
    # 保留其他字段不变

    with open(f'{paths_config.checkpoints_dir}/stylegan2_custom_{image_name}.pkl', 'wb') as f:
        pickle.dump(d, f)


if __name__ == "__main__":
    # model_ZWBSAUDJOQWG_xiangzi.pt 对应的 model_id 是 ZWBSAUDJOQWG， image_name 是 xiangzi
    model_id = "ZWBSAUDJOQWG"
    image_name = "xiangzi"
    generator_type = image_name
    old_G, new_G = load_generators(model_id, generator_type)
    export_updated_pickle(new_G, image_name)
    print("Done exporting updated pickle.")