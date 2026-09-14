import os
from datetime import datetime
import allure

def capture_screenshot(driver, name="error_screenshot"):
    artifacts_dir = "artifacts"
    os.makedirs(artifacts_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(artifacts_dir, f"{name}_{timestamp}.png")
    
    driver.save_screenshot(file_path)
    
    allure.attach.file(
        source=file_path,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )
    return file_path