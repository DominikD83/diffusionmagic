from typing import Any

import gradio as gr

from backend.computing import Computing
from backend.generate import Generate
from backend.stablediffusion.stable_diffusion_types import StableDiffusionType
from frontend.web.depth_to_image_ui import get_depth_to_image_ui
from frontend.web.image_inpainting_ui import get_image_inpainting_ui
from frontend.web.image_to_image_ui import get_image_to_image_ui
from frontend.web.instruct_pix_to_pix_ui import get_instruct_pix_to_pix_ui
from frontend.web.settings_ui import get_settings_ui
from frontend.web.text_to_image_ui import get_text_to_image_ui
from models.configs import DiffusionMagicSettings
from utils import DiffusionMagicPaths

compute = Computing()
generate = Generate(compute)


def diffusionmagic_web_ui(settings: DiffusionMagicSettings) -> gr.Blocks:
    model_id = settings.model_settings.model_id
    stable_diffusion_type = StableDiffusionType.base
    if "inpainting" in model_id:
        stable_diffusion_type = StableDiffusionType.inpainting
    elif "depth" in model_id:
        stable_diffusion_type = StableDiffusionType.depth2img
    elif "instruct-pix2pix" in model_id:
        stable_diffusion_type = StableDiffusionType.instruct_pix2pix

    with gr.Blocks(
        css=DiffusionMagicPaths.get_css_path(),
        title="DiffusionMagic",
    ) as diffusion_magic_ui:
        gr.HTML("<center><H3>DiffusionMagic</H3></center>")
        with gr.Tabs():
            if stable_diffusion_type == StableDiffusionType.base:
                with gr.TabItem("Text to image"):
                    get_text_to_image_ui(generate.diffusion_text_to_image)
                with gr.TabItem("Image to image"):
                    get_image_to_image_ui(generate.diffusion_image_to_image)
            elif stable_diffusion_type == StableDiffusionType.inpainting:
                with gr.TabItem("Image Inpainting"):
                    get_image_inpainting_ui(generate.diffusion_image_inpainting)
            elif stable_diffusion_type == StableDiffusionType.depth2img:
                with gr.TabItem("Depth to Image"):
                    get_depth_to_image_ui(generate.diffusion_depth_to_image)
            elif stable_diffusion_type == StableDiffusionType.instruct_pix2pix:
                with gr.TabItem("Instruct Pix to Pix"):
                    get_instruct_pix_to_pix_ui(generate.diffusion_pix_to_pix)
            with gr.TabItem("Settings"):
                get_settings_ui()
    return diffusion_magic_ui
