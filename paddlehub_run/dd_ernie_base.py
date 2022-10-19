import paddlehub as hub

module = hub.Module(name="disco_diffusion_ernievil_base")
text_prompts = ["孤舟蓑笠翁，独钓寒江雪。"]
# 生成图像, 默认会在disco_diffusion_ernievil_base_out目录保存图像
# 返回的da是一个DocumentArray对象，保存了所有的结果，包括最终结果和迭代过程的中间结果
# 可以通过操作DocumentArray对象对生成的图像做后处理，保存或者分析
module.generate_image(text_prompts=text_prompts, artist='齐白石', output_dir='./disco_diffusion_ernievil_base_out/')
# da = module.generate_image(text_prompts=text_prompts, artist='齐白石', output_dir='./disco_diffusion_ernievil_base_out/')
# 手动将最终生成的图像保存到指定路径
# da[0].save_uri_to_file('disco_diffusion_ernievil_base_out-result.png')
# 展示所有的中间结果
# da[0].chunks.plot_image_sprites(skip_empty=True, show_index=True, keep_aspect_ratio=True)
# 将整个生成过程保存为一个动态图gif
# da[0].chunks.save_gif('disco_diffusion_ernievil_base_out-result.gif', show_index=True, inline_display=True, size_ratio=0.5)