# Code Portrait Banner Generator

Transform your portrait photo into a stunning **matrix-style ASCII/code character composition** for your GitHub profile.

## 🎨 Features

✨ **Code Portrait Digital Art**
- Dense monospace programming symbols (brackets, slashes, binary digits, operators)
- Characters form the silhouette of face, hijab/hair, and shoulders
- Brightness and density follow the original photo's light and shadow

🖼️ **Terminal Frame Design**
- Glowing neon gradient border (green → cyan → purple)
- macOS-style traffic light dots (red, yellow, green)
- Thin title bar with "profile.art" label
- Professional terminal window aesthetic

🌈 **Color Scheme**
- White and soft cyan-teal character tones
- Dark background with sparse, faint background code elements
- High contrast, minimalist design

📐 **Perfect for GitHub**
- Wide banner aspect ratio: **3:1** (1200×400 pixels)
- Suitable for GitHub profile README banners
- Professional and eye-catching

## 🚀 Quick Start

### Prerequisites
```bash
pip install Pillow numpy
```

### Usage

1. **Place your portrait image** in the same directory as the script:
   ```
   portrait.jpg
   generate_banner.py
   ```

2. **Run the generator:**
   ```bash
   python3 generate_banner.py
   ```

3. **Output** is saved as `banner.png` (1200×400 pixels)

### Using with GitHub Profile

Add the banner to your GitHub profile README:

```markdown
![Profile Banner](banner.png)
```

Or in your profile repository (`EmanSayedSeddik/EmanSayedSeddik`):

```markdown
<img src="banner.png" alt="Profile Banner" width="100%">
```

## 🎛️ Customization

Edit `generate_banner.py` to adjust:

- **Colors**: Modify `PRIMARY_COLOR`, `ACCENT_COLOR`, `BACKGROUND_COLOR`
- **Code characters**: Edit `CODE_CHARS` dictionary for different symbols
- **Banner size**: Change `BANNER_WIDTH`, `BANNER_HEIGHT`
- **Character density**: Adjust `CHAR_WIDTH`, `CHAR_HEIGHT`
- **Border glow**: Modify `create_neon_gradient_border()` colors

## 📋 Requirements

- Python 3.7+
- Pillow (PIL)
- NumPy

## 📸 Image Requirements

- **Format**: JPG, PNG, or any PIL-supported format
- **Aspect ratio**: Any (script will auto-adjust)
- **Resolution**: 500×500px or higher recommended
- **Content**: Portrait or headshot photos work best

## 🔧 Advanced Usage

### Custom image path:
```python
generate_banner('path/to/your/image.jpg', 'custom_output.png')
```

### Download from URL:
```python
generate_banner('https://example.com/portrait.jpg')
```

## 💡 Tips

- **Best results** with high-contrast portraits (good lighting on face, darker background)
- **Close-ups** work better than full-body shots
- **Test different** background code character densities
- **Experiment** with color schemes for your personal brand

## 📄 License

Free to use and modify for personal GitHub profiles.

---

**Created with** ✨ for GitHub profiles
