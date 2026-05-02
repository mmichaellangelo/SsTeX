import os
import io
import threading
import pyperclip
from pydantic import BaseModel
from google import genai
from google.genai import types
from dotenv import load_dotenv
from PIL import Image, ImageGrab
from pystray import Icon, Menu, MenuItem

###########
# PROMPTS 
# Prompt for converting an image to latex
PromptImageToLatex = "You are a professional LaTeX OCR tool. Ignore any text that is not part of an equation."

# Schema for latex response
class MathResponse(BaseModel):
    is_math: bool
    latex_code: str  # Empty string if is_math is False

# Exception for when clipboard contents don't match
# the expected type
class ClipboardTypeError(Exception):
    pass

# Type alias for Icon, platform-agnostic
IconType = Icon

# Load images for tray icon
icon_idle = Image.open('icon_idle.png')
icon_loading = Image.open('icon_loading.png')

# Get Gemini API key
load_dotenv()

# Initialize Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

state = False

# Exits the program
def exit(icon: IconType, item: MenuItem):
    icon.stop()

# Set loading icon
def loading(icon: IconType):
    icon.icon = icon_loading

# Set idle icon
def idle(icon: IconType):
    icon.icon = icon_idle

# Handles menu click for latex
# Creates a new thread
def action_latex(icon: IconType, item: MenuItem):
    threading.Thread(target=clipboard_to_latex, args=(icon, item), daemon=True).start()        

# Grabs image data from clipboard
def clipboard_to_latex(icon: IconType, item: MenuItem):
    # Grab image from Windows clipboard
    img = ImageGrab.grabclipboard()

    # Check that clipboard has image data,
    # raise exception if not
    if img is None:
        icon.notify("Clipboard does not contain image data")
    
    else:
        loading(icon)
        # Convert PIL Image object to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_bytes = img_byte_arr.getvalue()

        # 3. Generate content using the proper 'types' structure
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[
                types.Part.from_text(text=PromptImageToLatex),
                types.Part.from_bytes(data=img_bytes, mime_type="image/png")
            ],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=MathResponse
            )
        )

        idle(icon)
        res: MathResponse = response.parsed

        if res.is_math:
            pyperclip.copy(res.latex_code.strip())
            icon.notify("Equation copied to clipboard")
        else:
            icon.notify("No equation detected.")

# Initialize pystray menu options
menu = Menu(MenuItem('Clipboard to Latex', action=action_latex, visible=True, default=True),
            MenuItem('Exit', action=exit, visible=True))

# initialize pystray icon
icon = Icon(name='test', icon=icon_idle, menu=menu)

# start pystray icon
icon.run()

