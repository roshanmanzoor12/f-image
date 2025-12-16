gradio_root = None
REALISTIC_HUMAN_PRESET = {
    "sampler": "dpmpp_2m_karras",
    "steps": 30,
    "cfg": 5.0,
    "scheduler": "karras",
    "resolution": (1024, 1024),

    # Texture preservation
    "denoise": 0.35,

    # Upscale
    "upscale_model": "RealESRGAN_x4plus",
    "upscale_factor": 2,
    "upscale_denoise": 0.25,
}
