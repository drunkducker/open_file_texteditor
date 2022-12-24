import subprocess
def open_file(filename):
    subprocess.run(["gedit", filename])
def handle_open_file_intent(self, message):
    # Extract the filename from the message
    filename = message.data.get("filename")
    
    # Open the file in a text editor
    open_file(filename)
    
    # Send a response back to the user
    self.speak_dialog("file.opened", {"filename": filename})
