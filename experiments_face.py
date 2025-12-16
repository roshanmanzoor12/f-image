import cv2
import extras.face_crop as cropper


# =========================
# LOAD IMAGE (for face detection only)
# =========================
img = cv2.imread('lena.png')

if img is None:
    raise ValueError("Image not found or path is incorrect")


# =========================
# FACE DETECTION (NOT CROPPING OUTPUT)
# =========================
# We detect face but DO NOT replace full image
face_detected = cropper.crop_image(img) is not None


# =========================
# SKIN + FULL BODY PROMPT ENHANCER
# =========================
def enhance_human_fullbody_realism(prompt: str, negative_prompt: str):
    """
    Forces full body human generation with ultra-realistic skin textures
    while preventing face-only or cropped outputs.
    """

    full_body_tokens = (
        "full body shot, head to toe visible, "
        "entire human body in frame, standing pose, "
        "realistic body proportions"
    )

    skin_tokens = (
        "ultra realistic human skin texture, "
        "visible skin pores, "
        "subsurface scattering, "
        "micro skin details, "
        "fine body hair, "
        "natural skin imperfections, "
        "real DSLR photo"
    )

    lighting_tokens = (
        "soft natural light, "
        "cinematic shadows, "
        "realistic light falloff"
    )

    negative_tokens = (
        "close up, face closeup, headshot, cropped body, "
        "plastic skin, smooth skin, waxy, airbrushed, "
        "cgi, cartoon, anime, doll body, beauty filter"
    )

    if full_body_tokens not in prompt:
        prompt = f"{prompt}, {full_body_tokens}"

    if skin_tokens not in prompt:
        prompt = f"{prompt}, {skin_tokens}"

    if lighting_tokens not in prompt:
        prompt = f"{prompt}, {lighting_tokens}"

    if negative_tokens not in negative_prompt:
        negative_prompt = f"{negative_prompt}, {negative_tokens}"

    return prompt, negative_prompt


# =========================
# EXAMPLE USAGE
# =========================
if __name__ == "__main__":
    prompt = "28 year old woman wearing casual clothes"
    negative_prompt = "low quality, blurry"

    prompt, negative_prompt = enhance_human_fullbody_realism(
        prompt, negative_prompt
    )

    print("FINAL FULL BODY PROMPT:\n", prompt)
    print("\nFINAL NEGATIVE PROMPT:\n", negative_prompt)

