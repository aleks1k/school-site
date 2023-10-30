import os
import win32com.client

def convert_ppt_to_pptx(directory):
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    
    for filename in os.listdir(directory):
        if filename.endswith(".ppt"):
            full_path = os.path.join(directory, filename)
            print(full_path)
            presentation = powerpoint.Presentations.Open(full_path)
            new_filename = os.path.splitext(filename)[0] + '.pptx'
            new_full_path = os.path.join(directory, new_filename)
            presentation.SaveAs(new_full_path, 24)  # 24 corresponds to pptx format
            presentation.Close()

    powerpoint.Quit()

# Call the function
convert_ppt_to_pptx('D:\Projects\AI\school site\data_files\\2 класс тесты математика')
