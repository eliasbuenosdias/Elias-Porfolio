from PIL import Image

def make_blended_wide(input_path, output_path, bg_hex):
    # Convert hex to RGB
    bg_color = tuple(int(bg_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    
    img = Image.open(input_path)
    img = img.convert("RGBA")
    w, h = img.size
    
    # Use 16:9 aspect ratio to match our CSS target
    # Add a small vertical margin for safety
    safe_margin = int(h * 0.1)
    inner_h = h + (2 * safe_margin)
    
    target_aspect = 16/9
    target_w = int(inner_h * target_aspect)
    
    # Create the new canvas with the site's background color
    new_img = Image.new("RGBA", (target_w, inner_h), bg_color + (255,))
    
    # Paste original in the center
    offset_x = (target_w - w) // 2
    offset_y = safe_margin
    new_img.paste(img, (offset_x, offset_y), img)
    
    # Convert back to RGB for final save
    final_img = new_img.convert("RGB")
    final_img.save(output_path)
    print(f"Saved blended image to {output_path} with background {bg_hex}")

# Site theme background is #0F0F0F
theme_bg = "#0F0F0F"

make_blended_wide("recursos/logoGeoGas-dark.png", "recursos/logoGeoGas-wide.png", theme_bg)
make_blended_wide("recursos/whatsAppSDRedirect.png", "recursos/whatsAppSDRedirect-wide.png", theme_bg)
