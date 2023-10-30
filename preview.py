import win32com.client


presentation_path = 'D:\Projects\AI\school site\data_files\\2 класс тесты математика\умножение и деление на 2.ppt'
preview_path = 'D:\Projects\AI\school site\\2.png'

# Function to convert first slide of .ppt to image
def convert_ppt_to_image(ppt_path, output_path):
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    presentation = powerpoint.Presentations.Open(ppt_path)
    
    # Export first slide to image
    presentation.Slides[0].Export(output_path, "PNG")
    
    presentation.Close()
    powerpoint.Quit()

# Try to convert the provided .ppt file
try:
    convert_ppt_to_image(presentation_path, preview_path)
except Exception as e:
    error_message = str(e)
    print(error_message)

