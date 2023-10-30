import os
import win32com.client
from transliterate import translit
import re

base_dir = 'D:\Projects\AI\school site\data_files'
output_html_path = 'D:\Projects\AI\school site\output.html'

def sanitize_filename(filename):
    # Transliterate to English
    filename = translit(filename, reversed=True)
    # Replace spaces with underscores and remove non-alphanumeric characters
    filename = re.sub(r'\W+', '', filename)
    return filename

def convert_ppt_to_image(ppt_path, output_dir):
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    presentation = powerpoint.Presentations.Open(ppt_path)
    
    # Create an image name from the ppt file name
    image_name = sanitize_filename(os.path.splitext(os.path.basename(ppt_path))[0]) + '.png'
    image_path = os.path.join(output_dir, image_name)

    # Export first slide to image
    presentation.Slides[0].Export(image_path, "PNG")
    
    presentation.Close()
    powerpoint.Quit()
    
    return image_path

html_content = []

# Walk through all subdirectories
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.ppt'):
            ppt_path = os.path.join(root, file)
            
            # Convert to image and get the path of the generated image
            image_path = convert_ppt_to_image(ppt_path, base_dir)
            
            # Create HTML content
            html_code = f'''
            <article>
                <h4>Тест "{os.path.splitext(file)[0]}"</h4>
                <img src="{image_path}" alt="Превью теста">
                <p>Тест для проверки навыков табличного умножения.</p>
                <a href="{ppt_path}" class="download-btn">Скачать</a>
            </article>
            '''
            html_content.append(html_code)

# Write the generated HTML content to a file
with open(output_html_path, 'w', encoding='utf-8') as f:
    for item in html_content:
        f.write("%s\n" % item)
