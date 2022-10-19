import paddlehub as hub
import os
from PIL import Image
module = hub.Module(name="ernie_vilg")
run_count = len(os.listdir('ernievilg_output'))//2+11
outpath = f'ernievilg_output/{run_count:04}'
"""
def generate_image(
          text_prompts:str,
          style: Optional[str] = "油画", # '油画','水彩','粉笔画','卡通','儿童画','蜡笔画','探索无限'
          topk: Optional[int] = 6,
          output_dir: Optional[str] = 'ernievilg_output')
"""
def make_grid(imgs):
    size = 512 // 2
    target = Image.new('RGB', (size*3, size*2))
    for i, img in enumerate(imgs):
        hor = size * (i % 3)
        ver = size * (i // 3)
        target.paste(img.resize((size, size)), (hor, ver, hor+size, ver+size))
    return target


# prompts = "胖虎调戏大白鼠，饥荒"
# prompts = "一名僧人，螃蟹螃蟹，佛礼"
# prompts = "老虎老虎在饥荒的世界里调戏小老鼠小老鼠"
# prompts = "肥羊把牛吹上了天"
prompts='肥羊吹了一口气就上天了'
# prompts = "大师，螃蟹在石头上，寺庙门口，大雪，烟雾缭绕"
# prompts = "蟹六跪而三螯，"
# prompts = "慧远大师"
# prompts = "肥羊杵着拐杖在大街上跳舞"
results = module.generate_image(text_prompts=prompts, style="探索无限", output_dir=outpath)
make_grid(results).save(f"ernievilg_output/grid-{run_count:04}.png")