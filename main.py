import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import requests
from bs4 import BeautifulSoup
import os
import re 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class ImageDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("InstantGallery")
        self.geometry("600x500") 
        self.iconbitmap("logo.ico")
        
        self.download_folder = ""
        self.is_downloading = False
        
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = ctk.CTkFrame(self, corner_radius=10)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ctk.CTkLabel(main_frame, text="Image Downloader", 
                    font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(20, 30))
        
        ctk.CTkLabel(main_frame, text="Search Query:", font=ctk.CTkFont(size=14)).pack(pady=(10, 5))
        
        self.query_entry = ctk.CTkEntry(main_frame, width=500, height=40, 
                                        placeholder_text="Enter search term...")
        self.query_entry.pack(pady=5)
        
        self.folder_button = ctk.CTkButton(main_frame, text="Select Download Folder", 
                                        command=self.select_folder, width=250)
        self.folder_button.pack(pady=(30, 0))
        
        self.folder_label = ctk.CTkLabel(main_frame, text="No folder selected", 
                                        font=ctk.CTkFont(size=11), text_color="gray")
        self.folder_label.pack(pady=5)
        
        self.download_button = ctk.CTkButton(main_frame, text="Download Images", 
                                            command=self.start_download, width=200, height=45,
                                            fg_color="#2ecc71", hover_color="#27ae60",
                                            font=ctk.CTkFont(size=15, weight="bold"))
        self.download_button.pack(pady=(30, 10))
        

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.download_folder = folder
            self.folder_label.configure(text=folder if len(folder) < 60 else f"...{folder[-57:]}", 
                                        text_color="white")
    
    def start_download(self):
        query = self.query_entry.get().strip()
        num_images = 20 
        
        if not query or not self.download_folder:
            messagebox.showwarning("Error", "Please provide a query and a folder.")
            return
        
        if self.is_downloading: return

        self.is_downloading = True
        self.download_button.configure(state="disabled", text="Downloading...")
        
        threading.Thread(target=self.download_images, args=(query, num_images), daemon=True).start()
    
    def download_images(self, query, num_images):
        try:
            # FIX: Sanitize the query to remove invalid Windows characters for folder/file names
            clean_name = re.sub(r'[<>:"/\\|?*]', '', query).strip()
            if not clean_name: clean_name = "downloaded_images"

            url = f"https://www.google.com/search?q={query}&tbm=isch"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            
            self.update_status("Fetching image links...", "yellow")
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img')
            
            # Use the clean_name for the directory
            search_folder = os.path.join(self.download_folder, clean_name.replace(" ", "_"))
            os.makedirs(search_folder, exist_ok=True)
            
            downloaded = 0
            for img in img_tags:
                if downloaded >= num_images: break
                
                img_url = img.get('src') or img.get('data-src')
                if not img_url or not img_url.startswith('http'): continue
                
                try:
                    img_data = requests.get(img_url, headers=headers, timeout=10).content
                    # Use clean_name for the file as well
                    file_path = os.path.join(search_folder, f"{clean_name}_{downloaded+1}.jpg")
                    
                    with open(file_path, 'wb') as f:
                        f.write(img_data)
                    
                    downloaded += 1
                    self.update_status(f"Downloaded {downloaded} images...", "yellow")
                except:
                    continue
            
            self.update_status("✅ Done!", "green")
            messagebox.showinfo("Success", f"Downloaded {downloaded} images to:\n{search_folder}")
            
        except Exception as e:
            self.update_status("❌ Error", "red")
            messagebox.showerror("Error", f"Folder Error: {str(e)}")
        finally:
            self.is_downloading = False
            self.download_button.configure(state="normal", text="Download Images")
    
    def update_status(self, text, color):
        self.after(0, lambda: self.status_label.configure(text=text, text_color=color))

if __name__ == "__main__":
    ImageDownloaderApp().mainloop()