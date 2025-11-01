#!/usr/bin/env python3
"""
Generate ModelIt! K12 Newsletter Hero Images with Google Gemini
Uses gemini-2.5-flash-image (Nano Banana) - FREE and VERIFIED WORKING
"""

import sys
import os
import base64
from dotenv import load_dotenv
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

load_dotenv('C:/Users/MarieLexisDad/.env')

# Check for google-generativeai library
try:
    import google.generativeai as genai
except ImportError:
    print("Installing google-generativeai...")
    import subprocess
    subprocess.check_call(['pip', 'install', '-q', 'google-generativeai'])
    import google.generativeai as genai

# Configure API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("ERROR: GOOGLE_API_KEY not found in .env")
    exit(1)

genai.configure(api_key=api_key)

# Create output directory
output_dir = Path('C:/Users/MarieLexisDad/modelitk12-newsletter/assets/images')
output_dir.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("GENERATING MODELIT! K12 NEWSLETTER HERO IMAGES")
print("=" * 80)
print("Using: Google Gemini 2.5 Flash Image (Nano Banana)")
print("Method: Official Google AI API - FREE")
print()

# Initialize model
model = genai.GenerativeModel('gemini-2.5-flash-image')

# Newsletter hero prompts
heroes = {
    "week1-hero": """Create a vibrant, photorealistic image of a modern middle school science classroom:

SUBJECTS:
- 4-5 diverse students (ages 11-14: African American, Latino, Asian, Caucasian)
- Students are excited, engaged, collaborating
- Some pointing at screens, others discussing animatedly

TECHNOLOGY:
- Tablets and laptops on desks
- Screens showing colorful biological cell models
- Interactive molecular pathway diagrams visible on displays
- Clear technology integration in learning

SETTING:
- Bright modern classroom
- Natural sunlight from large windows
- Clean, contemporary educational environment
- Professional but inviting atmosphere

COLOR PALETTE:
- Navy blue (#030C3C) and bright blue (#0F6ACE) accents
- Natural classroom colors (wood, whites, neutrals)
- Colorful scientific visualizations on screens
- Warm, inspiring lighting

MOOD: Inspiring, collaborative, future-ready science education
STYLE: Professional educational photography, natural lighting, high quality, 16:9 wide format
FOCUS: Students actively engaged with computational biology tools""",

    "week2-hero": """Create a professional scientific research image:

MAIN ELEMENT:
- Large professional monitor/display showing Cell Collective platform
- Screen displays intricate biological network diagrams
- Colorful interactive cellular models with nodes and connections
- Complex systems biology visualizations clearly visible

NETWORK VISUALIZATION:
- Interconnected pathways with blue, teal, and cyan nodes
- Molecular interactions shown as connecting lines
- Scientific precision and sophistication
- Multiple biological components in network

SETTING:
- Clean modern research laboratory or workspace
- Professional scientific environment
- Subtle research equipment in soft focus background
- Contemporary, cutting-edge aesthetic

COLOR PALETTE:
- Navy blue (#030C3C) and bright blue (#0F6ACE) dominant
- Light blue (#38aefd) accents in visualizations
- Professional scientific color scheme
- Clean whites and modern grays

MOOD: Cutting-edge research, scientific innovation, systems biology
STYLE: Professional scientific photography, soft lighting, high-tech aesthetic, 16:9 wide format
FOCUS: Cell Collective platform interface showcasing biological complexity"""
}

results = []

for hero_id, prompt in heroes.items():
    print(f"\nGenerating: {hero_id}...")
    print(f"Prompt: {prompt[:100]}...")

    try:
        # Generate image
        response = model.generate_content(prompt)

        print(f"  Response received, checking for image data...")

        # Check if image was generated
        if not response.candidates or len(response.candidates) == 0:
            print(f"[FAILED] No candidates in response")
            print(f"  Response: {response}")
            continue

        candidate = response.candidates[0]
        print(f"  Got candidate, checking content...")

        # Extract image data
        if not hasattr(candidate, 'content') or not candidate.content.parts:
            print(f"[FAILED] No content.parts in response")
            print(f"  Candidate: {candidate}")
            continue

        print(f"  Found {len(candidate.content.parts)} parts")

        image_saved = False
        for i, part in enumerate(candidate.content.parts):
            print(f"  Part {i}: {type(part).__name__}")

            if hasattr(part, 'inline_data') and part.inline_data:
                print(f"    Found inline_data!")
                # Save image - get binary data
                image_data = part.inline_data.data

                if not image_data or len(image_data) == 0:
                    print(f"[FAILED] inline_data.data is empty!")
                    continue

                filepath = output_dir / f"{hero_id}.jpg"

                with open(filepath, 'wb') as f:
                    f.write(image_data)

                print(f"[SUCCESS] Saved {filepath} ({len(image_data)/1024:.1f} KB)")
                results.append(hero_id)
                image_saved = True
                break

        if not image_saved:
            print(f"[FAILED] No inline_data with content found in any part")

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

print(f"\n\n{'=' * 80}")
print(f"GENERATION COMPLETE")
print(f"{'=' * 80}")
print(f"Generated: {len(results)}/2 images")
print(f"Output: {output_dir}")
print()

if len(results) == 2:
    print("[COMPLETE] Both newsletter hero images generated!")
    print(f"   - Week 1: {output_dir / 'week1-hero.jpg'}")
    print(f"   - Week 2: {output_dir / 'week2-hero.jpg'}")
else:
    print(f"[WARNING] Only {len(results)}/2 images generated successfully")

print("\nNext steps:")
print("1. Review images in assets/images/")
print("2. Commit changes to Git")
print("3. Push to GitHub to rebuild newsletter")
