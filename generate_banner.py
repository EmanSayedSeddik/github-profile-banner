#!/usr/bin/env python3
"""
Code Portrait Digital Art Generator for GitHub Profile Banner
Converts a portrait photo into ASCII/code character composition
with matrix-style programming symbols and neon terminal frame
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path
import urllib.request

# Configuration
BANNER_WIDTH = 1200
BANNER_HEIGHT = 400
CHAR_WIDTH = 8
CHAR_HEIGHT = 14
BACKGROUND_COLOR = (10, 10, 15)
PRIMARY_COLOR = (255, 255, 255)  # White
ACCENT_COLOR = (100, 220, 220)   # Cyan-teal

# Code characters for ASCII art (weighted by visual density)
CODE_CHARS = {
    'dense': ['█', '▓', '▒', '@', '#', '%', '$', '&', '*', 'M', 'W', 'm', 'w'],
    'medium': ['[', ']', '{', '}', '(', ')', '/', '\\', '|', '=', '+', '-', ':', ';', '1', '0', 'x'],
    'light': ['.', ',', '\'', '`', '^', '~', '_', ' ', ' ']
}

def download_image(url):
    """Download image from URL"""
    try:
        urllib.request.urlretrieve(url, 'temp_portrait.jpg')
        return Image.open('temp_portrait.jpg')
    except Exception as e:
        print(f"Could not download image: {e}")
        return None

def load_or_download_image(image_path):
    """Load image from file or URL"""
    if isinstance(image_path, str) and image_path.startswith('http'):
        return download_image(image_path)
    return Image.open(image_path) if Path(image_path).exists() else None

def image_to_ascii(image_path, width, height):
    """Convert image to ASCII art with varying density"""
    img = load_or_download_image(image_path)
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return None
    
    # Convert to grayscale
    img = img.convert('L')
    
    # Resize to match character grid
    aspect_ratio = img.height / img.width
    new_width = width
    new_height = int(width * aspect_ratio * 0.55)  # Adjust for character aspect ratio
    img = img.resize((new_width, new_height))
    
    # Get pixel data
    pixels = np.array(img)
    
    # Normalize pixel values (0-1)
    pixels_norm = pixels / 255.0
    
    # Create ASCII art based on brightness
    ascii_art = []
    for row in pixels_norm:
        ascii_row = []
        for pixel in row:
            # Select character based on brightness
            if pixel > 0.8:
                char = CODE_CHARS['light'][int(pixel * len(CODE_CHARS['light']) * 0.9)]
            elif pixel > 0.5:
                char = CODE_CHARS['medium'][int(pixel * len(CODE_CHARS['medium']) * 0.9)]
            else:
                char = CODE_CHARS['dense'][int((1 - pixel) * len(CODE_CHARS['dense']) * 0.9)]
            ascii_row.append(char)
        ascii_art.append(''.join(ascii_row))
    
    return ascii_art

def create_neon_gradient_border(draw, width, height, border_width=4):
    """Create glowing neon gradient border (green -> cyan -> purple)"""
    # Outer glow effect with multiple layers
    colors_gradient = [
        (0, 200, 100, 30),      # Transparent green
        (0, 200, 150, 50),      # Green to cyan
        (0, 180, 220, 80),      # Cyan
        (100, 150, 255, 60),    # Cyan to purple
        (150, 100, 255, 40),    # Purple
    ]
    
    # Draw outer glow layers
    for i, (r, g, b, a) in enumerate(colors_gradient):
        offset = border_width + i * 2
        # Top line
        draw.line([(offset, offset), (width - offset, offset)], fill=(r, g, b), width=2)
        # Bottom line
        draw.line([(offset, height - offset), (width - offset, height - offset)], fill=(r, g, b), width=2)
        # Left line
        draw.line([(offset, offset), (offset, height - offset)], fill=(r, g, b), width=2)
        # Right line
        draw.line([(width - offset, offset), (width - offset, height - offset)], fill=(r, g, b), width=2)
    
    # Draw inner bright border
    bright_border = border_width - 1
    draw.rectangle(
        [(bright_border, bright_border), (width - bright_border, height - bright_border)],
        outline=(100, 255, 200),
        width=2
    )

def draw_traffic_lights(draw, x, y):
    """Draw macOS-style traffic light dots"""
    colors = [(255, 89, 89), (255, 192, 61), (91, 197, 84)]  # Red, Yellow, Green
    radius = 5
    spacing = 12
    for i, color in enumerate(colors):
        cx = x + i * spacing
        draw.ellipse([(cx - radius, y - radius), (cx + radius, y + radius)], fill=color)

def generate_banner(image_path, output_path='banner.png'):
    """Generate the complete code portrait banner"""
    print("Generating code portrait banner...")
    
    # Create base image
    banner = Image.new('RGB', (BANNER_WIDTH, BANNER_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(banner, 'RGBA')
    
    # Try to load a monospace font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 10)
    except:
        try:
            font = ImageFont.load_default()
        except:
            font = None
    
    # Convert image to ASCII
    ascii_art = image_to_ascii(image_path, 
                               BANNER_WIDTH // CHAR_WIDTH, 
                               BANNER_HEIGHT // CHAR_HEIGHT)
    
    if ascii_art is None:
        print("Failed to convert image to ASCII")
        return False
    
    # Scale ASCII art to fit banner
    start_x = 30
    start_y = 40
    char_spacing_x = 7
    char_spacing_y = 12
    
    # Draw ASCII art on banner
    for row_idx, row in enumerate(ascii_art[:BANNER_HEIGHT // char_spacing_y]):
        y = start_y + row_idx * char_spacing_y
        if y > BANNER_HEIGHT - 30:
            break
        for col_idx, char in enumerate(row[:BANNER_WIDTH // char_spacing_x]):
            x = start_x + col_idx * char_spacing_x
            if x > BANNER_WIDTH - 30:
                break
            # Alternate between white and cyan for variety
            color = PRIMARY_COLOR if col_idx % 3 else ACCENT_COLOR
            draw.text((x, y), char, font=font, fill=color)
    
    # Add sparse background code elements
    import random
    random.seed(42)
    bg_chars = ['0', '1', 'x', '{', '}', '[', ']', '(', ')', ';', ':', '|']
    for _ in range(15):
        x = random.randint(0, BANNER_WIDTH)
        y = random.randint(0, BANNER_HEIGHT)
        char = random.choice(bg_chars)
        draw.text((x, y), char, font=font, fill=(50, 80, 100))
    
    # Draw neon gradient border with rounded corners
    create_neon_gradient_border(draw, BANNER_WIDTH, BANNER_HEIGHT)
    
    # Draw terminal title bar
    title_bar_height = 25
    draw.rectangle([(0, 0), (BANNER_WIDTH, title_bar_height)], fill=(30, 30, 40))
    draw.line([(0, title_bar_height), (BANNER_WIDTH, title_bar_height)], fill=(100, 255, 200), width=1)
    
    # Draw traffic lights
    draw_traffic_lights(draw, 15, title_bar_height // 2)
    
    # Add terminal title text
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
    except:
        title_font = font
    
    draw.text((60, 7), "profile.art", font=title_font, fill=(100, 200, 200))
    
    # Save banner
    banner.save(output_path, 'PNG')
    print(f"✓ Banner saved to {output_path}")
    print(f"  Size: {BANNER_WIDTH}x{BANNER_HEIGHT} (3:1 aspect ratio)")
    print(f"  Style: Code portrait with neon terminal frame")
    return True

if __name__ == '__main__':
    # Default: Use the portrait image URL or local file
    # You can modify this path to point to your image
    image_input = 'portrait.jpg'  # Replace with actual image path or URL
    
    # Check if image exists locally
    if not Path(image_input).exists():
        print(f"Note: Image file '{image_input}' not found.")
        print("Please provide a portrait image file as 'portrait.jpg' in the same directory.")
        print("\nUsage:")
        print("  1. Place your portrait image as 'portrait.jpg'")
        print("  2. Run: python3 generate_banner.py")
        print("  3. Banner will be generated as 'banner.png'")
    else:
        generate_banner(image_input)
